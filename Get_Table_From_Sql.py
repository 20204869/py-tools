import ply.lex as lex, re


#提取SQL字符串中的表名
def extract_table_name_from_sql(sql_str):

    # remove the /* */ comments
    q = re.sub(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/", "", sql_str)

    # remove whole line -- and # comments
    lines = [line for line in q.splitlines() if not re.match("^\s*(--|#)", line)]

    # remove trailing -- and # comments
    q = " ".join([re.split("--|#", line)[0] for line in lines])

    # split on blanks, parens and semicolons
    tokens = re.split(r"[\s)(;]+", q)

    # scan the tokens. if we see a FROM or JOIN, we set the get_next
    # flag, and grab the next one (unless it's SELECT).

    result = []
    get_next = False
    for token in tokens:
        if get_next:
            if token.lower() not in ["", "select"]:
                result.append(token)
            get_next = False
        get_next = token.lower() in ["from", "join"]
    return result

if __name__ == '__main__':
    table_list = []
    code = "."
    sql2="""
select * from table1 a left join table2 b on a.id = b.id
"""
    tables = extract_table_name_from_sql(sql2)
    print(extract_table_name_from_sql(sql2))
    for table in tables:
        for k in code:
            if k in table:
                print(table)
