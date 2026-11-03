# A catalog cleanup that refuses to guess

A product identifier such as `00123` is text, even when every character is a digit. Converting it to an integer produces `123`: the original identifier has changed. Adding zeros later is a guess unless the catalog specification defines the width.

The [runnable example](../catalog_demo.py) deliberately accepts text identifiers and rejects numeric ones. It trims outer whitespace only in the agreed `sku` and `name` fields, then removes fully identical rows. It neither infers missing values nor merges different products just because their identifiers match.

## The useful failure case

Consider these synthetic rows:

```python
{"sku": "00123", "name": "  Blue mug  "}
{"sku": "00123", "name": "  Blue mug  "}
{"sku": "00123", "name": "Red mug"}
```

After trimming, the first two rows are identical. Keeping one removes a duplicate without choosing between conflicting descriptions. The third row remains, with a review flag: the identifier now has two names. Automatically keeping the last row would silently turn a data-quality question into a business decision.

That distinction gives the cleanup a testable contract. The synthetic five-row example produces four rows and two review flags: one conflicting identifier and one formula-like string. Its eight checks cover leading zeros, Chinese text, duplicate removal, unchanged source data, stable repeated cleanup, and rejection of numeric identifiers, among other assertions.

## What the check does not prove

The output is still text data. A spreadsheet application can interpret an identifier as a number on import, and formula-like text needs a separate handling policy before spreadsheet use. Flagging a string is not formula neutralization. This demonstration also does not resolve conflicting records, detect near-duplicates or implement a complete CSV import/export pipeline.

The practical deliverable is the cleaned data **plus** a change report and unresolved-item list. Those records let the client approve the choices that require business knowledge, while the mechanical changes remain reproducible.

*Original demonstration using synthetic data; no prior client project or production deployment is claimed. Run `python catalog_demo.py` from the repository root to inspect the checks.*
