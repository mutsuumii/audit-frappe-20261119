# SQL injection via string formatting
# CWE-89 | Severity: CRITICAL
# File: frappe/core/doctype/duckdb_sync/duckdb_sync.py line 209

**Risk:** SQL query built by string formatting. Attacker can inject arbitrary SQL.

**Fix:** Use parameterized queries: cursor.execute('SELECT * FROM t WHERE id=%s', (val,))
