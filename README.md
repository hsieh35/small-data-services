# Small data & localization fixes

Get a small data, localization or webpage problem fixed with a defined scope, a fixed pilot quote and a reviewable result.

## Pilot offers

| Service | Pilot quote | Included scope |
| --- | ---: | --- |
| Product CSV cleanup | US$25 | One UTF-8 CSV, up to 2,000 rows, 10 columns and 5 MB. Agreed whitespace cleanup, exact duplicate removal, identifier preservation and a change report. |
| Simplified Chinese UI text QA | US$35 | Up to 100 short UI strings in JSON/CSV/Markdown. Terminology, placeholder and punctuation checks; a proposed patch and issue list. |
| Static webpage repair | US$49 | One reproducible HTML/CSS/JavaScript defect in a public, runnable project; a focused patch and relevant verification. |

These are starting quotes for the scopes above, not accepted orders. One correction round within the agreed scope is included. Timing, payment compatibility and final scope must be confirmed before a paid project starts. No subscription or upfront platform purchase is required by these offers.

## A small, reproducible example

This catalog is **synthetic demonstration data**, not client work:

| Input SKU | Input name | Result |
| --- | --- | --- |
| `00123` | `  Blue mug  ` | `00123`, `Blue mug` |
| `00123` | `  Blue mug  ` | Exact duplicate removed after agreed trimming |
| `00007` | ` 茶杯 ` | `00007`, `茶杯` |
| `00888` | `=1+1` | Kept as text, flagged for spreadsheet formula review |

Rules: trim only agreed text fields; never infer missing values; never turn identifiers into numbers; remove only fully identical rows after those changes. Distinct products sharing a SKU are retained and flagged, not silently merged. Formula-like text is flagged; opening CSV in a spreadsheet can still execute formulas or strip leading zeros, so import identifier columns as text. Spreadsheet-safe delivery settings must be agreed separately.

The runnable example in `catalog_demo.py` checks duplicate handling, leading zeros, Chinese text, conflicting identifiers and formula flags. It uses only Python's standard library and makes no network requests.

## Request a scoped quote

[Open a request](https://github.com/hsieh35/small-data-services/issues/new?template=service-request.md) with:

1. The desired result and a tiny **synthetic or fully redacted** example.
2. File size / number of strings, or a public bug reproduction.
3. Your budget, deadline and acceptance check.
4. Any workflow restrictions or confidentiality requirements.

**Issues and this repository are public. Do not post real customer records, personal information, credentials, proprietary source files, account numbers or bank information.** A suitable private exchange and delivery route must be agreed separately before exchanging non-public material.

I will respond with a concrete scope, checks and quote where the work fits. Please wait for confirmation before sending any payment. Opening an issue does not create an order or reserve a delivery time.

## Delivery checks

Each project includes the agreed checks and a clear account of changes, unresolved items and limitations. Code and data changes use explicit rules and reproducible tests where appropriate. Any required qualifications, workflow restrictions and confidential-data handling must be agreed before work begins.

---

中文：承接小范围商品表格整理、简体中文界面文字检查、静态网页问题修复。公开试单报价分别为 25 / 35 / 49 美元，范围见上表，实际项目需先确认需求、验收与结算。交付包含修改说明和约定的检查结果。请只在公开 issue 提供虚构或充分脱敏的样例，勿上传真实客户资料、账号或收款信息。
