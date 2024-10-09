import sqlite3
from datetime import datetime


def get_posts(cur: sqlite3.Cursor):
    result = cur.execute("""
        SELECT content,created_at
        FROM posts
        ORDER BY created_at DESC
        LIMIT 100"""
        ).fetchall()
    posts = [dict(content=item[0], created_at=item[1])for item in result]
    return posts

def set_post(cur:sqlite3.Cursor,content:str):
    if content!="":
        cur.execute("""
                    INSERT INTO posts(content,created_at)
                    VALUES(?,?)""",
                    (content, datetime.now()))
        cur.commit()