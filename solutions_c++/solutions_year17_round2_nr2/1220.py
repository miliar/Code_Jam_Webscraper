#include <bits/stdc++.h>

using namespace std;

typedef long long ll ;


int main()
{
    freopen("B-small-attempt2.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;
    int t;
    scanf("%d",&t) ;
    for ( int ctr = 1 ; ctr <= t; ctr++ )
    {
        char c[] = {'z','R', 'O', 'Y', 'G', 'B', 'V'};
        int n = 6 ;
        int a[99] = {} ;
        priority_queue < pair < int, char > > Q ;
        for ( int i = 0 ; i < 7; i++ )
        {
            scanf("%d",&a[i]);
            if ( i )
                if ( a[i] )
                    Q.push({a[i],c[i]}) ;
        }
        int bb = a[1] + a[3] + a[5] ;
        string s = "" ;
        char f = 'z' ;
        while ( Q.size() )
        {
            //cout << "LOL" ;
            pair < int, char > tmp = Q.top() ;
            Q.pop() ;
            if ( tmp.first > 0 ) ;
            else continue ;

            if ( s.size() )
            {
                if ( s.back() == tmp.second )
                {
                    if ( Q.size() ) ;
                    else
                    {
                        Q.push(tmp) ;
                        break;
                    }
                    pair < int, char > tmp2 = Q.top() ;
                    Q.pop() ;
                    if ( Q.size() )
                    {
                        pair < int, char > tmp3 = Q.top() ;
                        Q.pop() ;
                        if ( tmp3.first == tmp2.first )
                            if ( tmp3.second == f )
                            {
                                s += tmp3.second ;
                                tmp3.first-- ;
                                if ( tmp3.first) Q.push(tmp3) ;
                                Q.push(tmp2) ;
                            }
                            else
                            {
                                s += tmp2.second ;
                                tmp2.first-- ;
                                if ( tmp2.first) Q.push(tmp2) ;
                                Q.push(tmp3) ;
                            }
                        else
                        {
                            Q.push(tmp3) ;
                            tmp2.first-- ;
                            s += tmp2.second ;
                            if ( tmp2.first ) Q.push(tmp2) ;

                        }
                    }
                    else
                    {

                        tmp2.first-- ;
                        s += tmp2.second ;
                        if ( tmp2.first ) Q.push(tmp2) ;
                    }
                    Q.push(tmp) ;
                }
                else if ( s.back() == f )
                {
                    s += tmp.second ;
                    tmp.first-- ;
                    if ( tmp.first ) Q.push(tmp) ;
                }
                else
                {
                    if ( Q.size() )
                    {

                        pair < int, char > tmp2 = Q.top() ;
                        Q.pop() ;
                        if ( tmp.first > tmp2.first )
                        {
                            tmp.first-- ;
                            s += tmp.second;
                            if ( tmp.first ) Q.push(tmp) ;
                            Q.push(tmp2) ;
                        }
                        else
                        {

                            if ( Q.size() )
                            {
                                pair < int, char > tmp3 = Q.top() ;
                                Q.pop() ;
                                if ( tmp3.first == tmp2.first )
                                    if ( tmp3.second == f && s.back() != f )
                                    {
                                        s += tmp3.second ;
                                        tmp3.first-- ;
                                        if ( tmp3.first) Q.push(tmp3) ;
                                        Q.push(tmp2) ;
                                        Q.push(tmp) ;
                                    }
                                    else if ( tmp2.second == f && s.back() != f)
                                    {
                                        s += tmp2.second ;
                                        tmp2.first-- ;
                                        if ( tmp2.first) Q.push(tmp2) ;
                                        Q.push(tmp3) ;
                                        Q.push(tmp) ;
                                    }
                                    else //if ( tmp.second == f && s.back() != f)
                                    {
                                        Q.push(tmp3) ;
                                        Q.push(tmp2) ;
                                        tmp.first-- ;
                                        s += tmp.second ;
                                        if ( tmp.first ) Q.push(tmp) ;
                                    }
                                else
                                {
                                    Q.push(tmp3) ;
                                    if ( tmp2.second == f && s.back() )
                                    {
                                        s += tmp2.second ;
                                        tmp2.first-- ;
                                        if ( tmp2.first) Q.push(tmp2) ;
                                        Q.push(tmp) ;
                                    }
                                    else
                                    {
                                        s += tmp.second ;
                                        tmp.first-- ;
                                        if ( tmp.first) Q.push(tmp) ;
                                        Q.push(tmp2) ;
                                    };

                                }
                            }
                            else
                            {
                                if ( tmp2.second == f && s.back() )
                                {
                                    s += tmp2.second ;
                                    tmp2.first-- ;
                                    if ( tmp2.first) Q.push(tmp2) ;
                                    Q.push(tmp) ;
                                }
                                else
                                {
                                    s += tmp.second ;
                                    tmp.first-- ;
                                    if ( tmp.first) Q.push(tmp) ;
                                    Q.push(tmp2) ;
                                }
                            }
                        }
                    }
                    else
                    {

                        tmp.first-- ;
                        s += tmp.second;
                        if ( tmp.first ) Q.push(tmp) ;
                    }
                }
            }
            else
            {
                f = tmp.second ;
                s += tmp.second ;
                tmp.first-- ;
                if ( tmp.first )
                    Q.push(tmp) ;
            }
        }
        cout << "Case #" << ctr << ": " ;
        if ( s.back()== s[0] || Q.size() )
            cout << "IMPOSSIBLE" << endl;
        else
        {
            assert(bb == s.size()) ;
            cout << s << endl;
        }
    }
    return 0;
}
