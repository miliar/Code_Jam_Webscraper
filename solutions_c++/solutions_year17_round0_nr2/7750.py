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



int64 f(int64 N) {
    string s = "";
    while (N) {

        s += ('0' + N%10);
        N/=10;

    }

    reverse(all(s));
    bool f = 0;
    FORN(i,1,s.sz) {
        if ( s[i] < s[i-1] or f ) {
            s[i] = s[i-1];
            f = 1;
        }
    }

    N = 0;
    FOR(i,s.sz) {
        N*=10;
        N+=(s[i] - '0');
    }
    return N;
}

int main(){

    freopen("in.txt","r", stdin);
    freopen("out.txt","w", stdout);

    int T, caso = 1;
    cin >> T;
    while(T--){

        int64 N;
        cin>>N;
        int64 lo = 1, hi = N, mi;
        while ( hi - lo > 1 ) {

            mi = (hi + lo)/2;

            if (f(mi) <= N ) lo = mi;
            else             hi = mi;
            //trace2(mi, f(mi));
        }
        int64 ans;
        if (f (hi) <= N) ans = f(hi);
        else             ans = f(lo);

        printf("Case #%d: %lld\n", caso++, ans);

    }
    return 0;
}
