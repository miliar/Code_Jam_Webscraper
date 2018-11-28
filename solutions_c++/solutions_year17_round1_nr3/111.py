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
int bit(ll x, int pos){ return ((1ll<<pos)&x) ? 1 : 0; }

const int INF = 1e9;
const int NMAX = 1e5+5;
const ll MOD = 1000000007;
const lf PI = 2*acos(0);

ll power(ll base, ll exp, ll c = MOD) { if(!exp) return 1; ll r = power(base, exp/2, c); r=(r*r)%c; if(exp&1) r=(r*base)%c; return r; }

ll T,N,M;  
int a,b,c;
string s1, s2;
int dp[101][101][101][101];
ll H, A, DH, DA, B, D;
int first;

int dper(int curh, int cura, int dh, int da) {
    if(curh <= 0) return -1;
    if(dh <= 0) return 0;
    REMIN(cura, DH);
    REMAX(da, 0);
    if(dp[curh][cura][dh][da] != -2)
        return dp[curh][cura][dh][da];
    int &steps = dp[curh][cura][dh][da] = -1;
    int get = INF;
    if(dh <= cura) {
        get = 1;
    } else {
        int temp = dper(curh - da, cura, dh - cura, da);
        if(temp != -1)
            REMIN(get, 1 + temp);
        if(B && cura < dh) {
            temp = dper(curh - da, cura + B, dh, da);
            if(temp != -1)
                REMIN(get, 1 + temp);
        }
        if(D && da) {
            temp = dper(curh - max(int(da - D), 0), cura, dh, da - D);
            if(temp != -1)
                REMIN(get, 1 + temp);
        }
        if(curh != H) {
            temp = dper(H - da, cura, dh, da);
            if(temp != -1)
                REMIN(get, 1 + temp);   
        }
    }
    if(get == INF)
        return steps = -1;
    return steps = get;
} 

void solve() {
        cin >> H >> A >> DH >> DA >> B >> D;
        first = 1;
        FOI(h, 1, H)
            FOI(ac, 1, DH)
                FOI(dh, 1, DH)
                    FOI(dac, 0, DA)
                        dp[h][ac][dh][dac] = -2;
        int stor = dper(H, A, DH, DA);
        if(stor == -1)
            cout << "IMPOSSIBLE";
        else
            cout << stor;
        cout << '\n';
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    cin >> T;

    FOI(test, 1, T) {
        cout << "Case #" << test << ": "; solve(); //cout << '\n';
    }   
    
    return 0;
}

