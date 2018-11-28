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

void solve() {
    int R, C;
    cin >> R >> C;
    char mat[27][27];
    FOI(r, 1, R)
        FOI(c, 1, C)
            cin >> mat[r][c];
    FOI(r, 1, R)
        FOI(c, 1, C) {
            if(mat[r][c] != '?') {
                int tr = r - 1;
                while(tr > 0 && mat[tr][c] == '?') {
                    mat[tr][c] = mat[r][c]; tr --;
                }
                tr = r + 1;
                while(tr < R + 1 && mat[tr][c] == '?'){
                    mat[tr][c] = mat[r][c]; tr ++;
                }
            }
        }

    cout << '\n';
    FOI(r, 1, R)
        FOI(c, 1, C) {
            if(mat[r][c] != '?') {
                int tc = c - 1;
                while(tc > 0 && mat[r][tc] == '?'){
                    mat[r][tc] = mat[r][c]; tc --;
                }
                tc = c + 1;
                while(tc < C + 1 && mat[r][tc] == '?'){
                    mat[r][tc] = mat[r][c]; tc ++;
                }
            }
        }
    FOI(r, 1, R){
        FOI(c, 1, C) {
            cout << mat[r][c];
        }
        cout << '\n';
    }
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    cin >> T;

    FOI(test, 1, T) {
        cout << "Case #" << test << ": "; solve(); //cout << '\n';
    }   
    
    return 0;
}

