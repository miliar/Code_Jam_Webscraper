#include <bits/stdc++.h>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>

#define ook order_of_key
#define fbk find_by_order
#define pb push_back
#define mp make_pair
#define intl long long
#define maxn 100005
#define ff first
#define ss second
#define bug printf ("bug\n")
#define sz(a) ((int)a.size())
#define set0(a) memset ((a), 0 , sizeof(a))
#define set1(a) memset((a),-1,sizeof (a))
#define si(a) scanf("%d" , &a)
#define sl(a) scanf("%lld" , &a)
#define sii(a,b) scanf("%d %d" , &a , &b)
#define sll(a,b) scanf("%lld %lld" , &a , &b)
#define FOR(i,a,b) for(intl i = (a) ; i <= (b) ; i++)
#define IN freopen("in.txt" , "r" , stdin)
#define OUT freopen("output2.txt" , "w" , stdout)
#define whats(x) printf ("x : %d\n" , x)



using namespace std ;
//using namespace __gnu_pbds;

typedef pair <int,int> pii ;
typedef pair <intl,intl> pll ;
//typedef tree < int, null_mapped_type ,less<int>,rb_tree_tag,tree_order_statistics_node_update > ordered_set;

/***************************************************************************************************/




int main () {

    IN ;

    OUT ;


    int tc , caseno = 1 ;
    cin >> tc ;

    while (tc--) {

        string s ;
        cin >> s ;

        printf ("Case #%d: " , caseno++) ;

        int len = s.size() ;

        int ok = 1 , idx ;

        FOR(i,0,len-2) {
            if (s[i] > s[i + 1]) {
                ok = 0 ;
                idx = i ;
                break ;
            }
        }

        if (ok) {
            cout << s << endl ;
            continue ;
        }

        int j ;

        for (int i = idx ; i >= 0 ; i--) {
            if (s[i] == s[idx]) {
                j = i ;
            }
            else {
                break ;
            }
        }

        s[j]-- ;

        for (int i = j+1 ; i < len ; i++) s[i] = '9' ;

        if (s[j] == '0') s.erase(s.begin()) ;

        cout << s << endl ;

    }

    return 0 ;
}
