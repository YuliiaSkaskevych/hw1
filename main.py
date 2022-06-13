
def parse(url: str)->dict:
    dic = {}
    a = url.split('?')
    try:
        if len(a) > 1:
            b=a[1].split('&')
            for i in b:
                c = i.split('=')
                dic[c[0]]=c[1]
    except IndexError:
        print('Error! Try again!')
    return dic

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('')
    assert parse('https://gidonline.io/?film=mentalist&year=2008&season=1') == {'film': 'mentalist', 'year': '2008', 'season': '1'}
    assert parse('http://auto.com/path/to/page?car=BMW&color=blue&country=Germany&year=1999&') == {'car':'BMW','color':'blue','country':'Germany','year':'1999'}
    assert parse('http://coffeshop.com/?coffee=latte&price=150&')=={'coffee':'latte','price':'150'}
    assert parse('https://www.youtube.com/?video=python&time=13:30&author=Mike')=={'video':'python','time':'13:30','author':'Mike'}
    assert parse('https://translate.google.com/?language=Ukrainian&symbols=5000&')=={'language':'Ukrainian','symbols':'5000'}
    assert parse('https://booking.com/?hotel=Hilton&guests=3&city=Kiev')=={'hotel':'Hilton','guests':'3','city':'Kiev'}
    assert parse('https://books.com.ua/?author=Orwell&book:1984&price=200&')=={'author':'Orwell','book':"1984",'price':'200'}
    assert parse('https://classroom.google.com/?group=412b&lessons=15')=={'group':'412b', 'lessons':'15'}
    assert parse('https://cinemacity.com/?cinema=Scream&year=2020&')=={'cinema':'Scream','year':'2020'}
    assert parse('https://pizzaeria.com/?pizza=Hawaii&price=300&place=DreamTown')=={'pizza':'Hawaii','price':'300','place':'DreamTown'}


def parse_cookie(query: str) -> dict:
    dic={}
    find=query.rfind(';')
    query_new=query[:find] +query[find+1:]
    print(query_new)
    a = query_new.split(';')
    if len(a) > 1:
        for i in a:
            c = i.split('=',1)
            dic[c[0]]=c[1]
    return dic

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('film=mentalist;year=2008;season=1')=={'film': 'mentalist', 'year': '2008', 'season': '1'}
    assert parse_cookie('car=BMW;color=blue;country=Germany;')=={'car':'BMW','color':'blue','country':'Germany','year':'1999'}
    assert parse_cookie('coffe=latte;price=150')=={'coffee':'latte','price':'150'}
    assert parse_cookie('video=python;time=13:30;author=Mike')=={'video':'python','time':'13:30','author':'Mike'}
    assert parse_cookie('language=Ukrainian;symbols=5000;')=={'language':'Ukrainian','symbols':'5000'}
    assert parse_cookie('hotel=Hilton;guests=3;city=Kiev')=={'hotel':'Hilton','guests':'3','city':'Kiev'}
    assert parse_cookie('author=Orwell;book=1984;price=200')=={'author':'Orwell','book':"1984",'price':'200'}
    assert parse_cookie('group=412b;lessons=15;')=={'group':'412b', 'lessons':'15'}
    assert parse_cookie('cinema=Scream;year=2020')=={'cinema':'Scream','year':'2020'}
    assert parse_cookie('pizza=Hawaii;price=300;place=DreamTown')=={'pizza':'Hawaii','price':'300','place':'DreamTown'}