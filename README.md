# Security audit: frappe/frappe

Date: 2026-11-19 | Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Found 4 issue(s): 2 critical, 2 high.

## Findings

### 1. [HIGH] Hardcoded credentials

**CWE-798** | `frappe/integrations/doctype/google_settings/test_google_settings.py` line 15

Credentials hardcoded in source. Anyone with repo access can extract them.

```
settings.api_key = "test_api_key"
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 2. [HIGH] Hardcoded credentials

**CWE-798** | `frappe/utils/test_print_format_generator.py` line 291

Credentials hardcoded in source. Anyone with repo access can extract them.

```
generator.render_pdf(password="s3cret")
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 3. [CRITICAL] SQL injection via string formatting

**CWE-89** | `frappe/core/doctype/duckdb_sync/duckdb_sync.py` line 113

SQL query built by string formatting. Attacker can inject arbitrary SQL.

```
conn.execute(f'delete from "{duck_tb.table_name}";').fetchall()
```

**Fix:** Use parameterized queries: cursor.execute('SELECT * FROM t WHERE id=%s', (val,))
---

### 4. [CRITICAL] SQL injection via string formatting

**CWE-89** | `frappe/core/doctype/duckdb_sync/duckdb_sync.py` line 209

SQL query built by string formatting. Attacker can inject arbitrary SQL.

```
conn.execute(f'delete from "{duck_tb.table_name}";').fetchall()
```

**Fix:** Use parameterized queries: cursor.execute('SELECT * FROM t WHERE id=%s', (val,))
---
