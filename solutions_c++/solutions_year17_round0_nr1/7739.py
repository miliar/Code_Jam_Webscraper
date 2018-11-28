#include <bits/stdc++.h>

#define fst first
#define snd second
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define clr(a, v) memset( a , v , sizeof(a) )
#define pb push_back
#define mp make_pair
#define sz size()
#define FORN( i , s , n ) for( int i = (s) ; i < (n) ; i++ )
#define FOR( i , n ) FORN( i , 0 , n )
#define FORIT( i , x ) for( typeof x.begin() i = x.begin() ; i != x.end() ; i++ )
#define trace(x)    cout << #x << ": " << x << endl;
#define trace2(x, y) cout << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z) cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define read ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

using namespace std;

typedef long long int64;
typedef vector <int> vi;
typedef pair <int,int> ii;
typedef vector <string> vs;
typedef vector <ii> vii;

int main(){
    freopen("AA.txt","r", stdin);
    freopen("outB.txt","w", stdout);
    int T, caso = 1;
    cin >> T;
    while(T--){

        string s; int K;
        cin>>s>>K;
        vi v(s.sz);
        FOR(i,s.sz) v[i] = (s[i] == '+');

        int cont = 0;
        FOR(i, v.sz - K+1) {
            if (v[i] == 0){
                FOR(j, K) v[i+j] = 1 - v[i+j];
                cont++;
            }
        }
        int aux = 0;
        FOR(i,v.sz) aux+=v[i];
        if (aux == v.sz) printf("Case #%d: %d\n", caso++, cont);
        else             printf("Case #%d: IMPOSSIBLE\n", caso++);
    }
    return 0;
}
