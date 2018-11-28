#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define mmax(a,b,c) max(max(a,b),c)
#define mmin(a,b,c) min(min(a,b),c)
#define sqr(n) ( ( n ) * ( n ) )
#define pb push_back
#define mp make_pair
#define size(x) ((int)(x).size())

const int N = 1 * 100500;
const int mod = 1e9 + 7;
const int inf = 1e9;

map < string, bool > m;
int res = -1;

void bfs( string s, int k ){
    queue < pair < string, int > > q;
    q.push( mp( s, 0 ) );
    while( !q.empty() ){
        pair < string, int > temp = q.front();
        q.pop();
        s = temp.first;
        m[ s ] = 1;
        int turn = temp.second;
        for (int i = 0; i < size( s ); i++){
            if ( s[i] != '+' ) break;
            if ( i == size( s ) - 1 ){
                res = turn;
                return;
            }
        }
        for (int i = 0; i <= size( s ) - k; i++){
            string tmp = s;
            for (int j = i; j < i + k; j++){
                if ( tmp[j] == '+' ) tmp[j] = '-';
                else tmp[j] = '+';
            }
            if ( !m[ tmp ] ){
                q.push( mp( tmp, turn + 1 ) );
            }
        }
    }
}

int main()
{
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdout);
    ofstream cout( "output.txt" );
    int t;
    cin >> t;
    int x = 1;
    while( t ){
        res = -1;
        m.clear();
        string s;
        int k;
        cin >> s >> k;;
        bfs( s, k );
        cout << "Case #" << x << ": ";
        if ( res == -1 ){
            cout << "IMPOSSIBLE\n";
        }
        else{
            cout << res << '\n';
        }
        --t;
        ++x;
    }
    return 0;
}
