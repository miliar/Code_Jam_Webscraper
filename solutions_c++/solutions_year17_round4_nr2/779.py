#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define fi first
#define se second
#define mp make_pair
#define SZ(x) ((int)(x.size()))
#define FOI(i,a,n) for(int (i)=int(a);(i)<=int(n);++(i))
#define FOD(i,a,n) for(int (i)=int(a);(i)>=int(n);--(i))
#define IN(x,y) ((y).find((x))!=(y).end())
#define ALL(t) t.begin(),t.end()
#define MSET(tabl,i) memset(tabl, i, sizeof(tabl))
#define PSET(x,y) fixed<<setprecision(y)<<lf(x)
#define DBG(c) cout << #c << " = " << c << endl;
#define RTIME ((double)clock()/(double)CLOCKS_PER_SEC)

template<typename T,typename S>inline bool REMIN(T&a,const S&b){return a>b?a=b,1:0;}
template<typename T,typename S>inline bool REMAX(T&a,const S&b){return a<b?a=b,1:0;}

typedef long long ll;
typedef long double lf;
typedef pair<int, int> pi;
typedef vector<pi> vpi;
typedef vector<int> vi;
typedef vector<vi> vvi;

ll toint(const string &s) { stringstream ss; ss << s; ll x; ss >> x; return x; }
string tostring ( int number ){  stringstream ss; ss<< number; return ss.str();}
int bit(ll x, int pos){ return (x >> pos) & 1; }
ll power(ll base, ll exp, ll c = 1e9 + 7) { if(!exp) return 1; ll r = power(base, exp/2, c); r=(r*r)%c; if(exp&1) r=(r*base)%c; return r; }

const ll INF = 1e9;
const int NMAX = 1e5+5;
const ll MOD = 1000000007;
const lf PI = 2*acos(0);

ll T,N,M;  
int a,b,c;
string s1, s2;

void solve() {
    int C;
    cin >> N >> C >> M;
    int b1[1003], b2[1003], n1 = 0, n2 = 0;
    MSET(b1, 0); MSET(b2, 0);
    FOI(i, 1, M) {
        cin >> a >> b;
        if(b == 1) b1[a] ++, n1 ++;
        else b2[a] ++, n2 ++;
    }
    int siz = max(n1, max(n2, b1[1] + b2[1]));
    int com = 0;
    FOI(i, 2, N) {
        REMAX(com, max(b2[i] - siz + b1[i], b1[i] - siz + b2[i]));
    }
    int promo = com;
    cout << siz << ' ' << promo << '\n';
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    cin >> T;

    FOI(test, 1, T) {
        cout << "Case #" << test << ": "; solve(); //cout << '\n';
    }   
    
    return 0;
}

