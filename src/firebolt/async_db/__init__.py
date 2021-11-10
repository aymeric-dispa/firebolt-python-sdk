from firebolt.async_db._types import (
    ARRAY,
    BINARY,
    DATETIME,
    NUMBER,
    ROWID,
    STRING,
    Binary,
    Date,
    DateFromTicks,
    Time,
    TimeFromTicks,
    Timestamp,
    TimestampFromTicks,
)
from firebolt.async_db.cursor import Cursor

apilevel = "2.0"
# threads may only share the module, connections and cursors should noy be shared
threadsafety = 1
paramstyle = "qmark"