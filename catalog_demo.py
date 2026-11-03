"""Synthetic catalog-cleanup sample. No files, accounts or network access."""


def clean_catalog(rows):
    result, changes, flags, seen = [], [], [], set()
    sku_names = {}
    for line, source in enumerate(rows, start=2):
        row = dict(source)
        for column in ("sku", "name"):
            if not isinstance(row[column], str):
                raise TypeError("SKU and name must be text; no implicit conversion")
            value = row[column].strip()
            if value != row[column]:
                changes.append((line, column, "trimmed outer whitespace"))
            row[column] = value
            if value.startswith(("=", "+", "-", "@")):
                flags.append((line, column, "formula-like text; review before spreadsheet use"))
        key = tuple(sorted(row.items()))
        if key in seen:
            changes.append((line, "row", "removed exact duplicate"))
            continue
        seen.add(key)
        if row["sku"] in sku_names and sku_names[row["sku"]] != row["name"]:
            flags.append((line, "sku", "same identifier has different names; retained both"))
        sku_names[row["sku"]] = row["name"]
        result.append(row)
    return result, changes, flags


if __name__ == "__main__":
    source = [
        {"sku": "00123", "name": "  Blue mug  "},
        {"sku": "00123", "name": "  Blue mug  "},
        {"sku": "00007", "name": " 茶杯 "},
        {"sku": "00888", "name": "=1+1"},
        {"sku": "00123", "name": "Red mug"},
    ]
    cleaned, changes, flags = clean_catalog(source)
    assert len(cleaned) == 4
    assert cleaned[0] == {"sku": "00123", "name": "Blue mug"}
    assert cleaned[1] == {"sku": "00007", "name": "茶杯"}
    assert cleaned[2]["name"] == "=1+1"
    assert len(flags) == 2
    assert source[0]["name"] == "  Blue mug  "
    assert clean_catalog(cleaned)[0] == cleaned
    try:
        clean_catalog([{"sku": 123, "name": "Mug"}])
        raise AssertionError("numeric identifier should have been rejected")
    except TypeError:
        pass
    print("PASS: 8 checks; 5 input rows, 4 output rows, 2 review flags.")

