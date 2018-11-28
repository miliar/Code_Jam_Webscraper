#include <bits/stdc++.h>
//#define DEBUG
#define si(n) scanf("%d",&n)
#define sl(n) cin>>n
#define sf(n) scanf("%f",&n)
#define pn(n) printf("%d\n",n)
#define ps(n) printf("%d ",n)
#define pln(n) cout<<n<<endl
#define pnl() printf("\n")
#define pls(n) cout<<n<<" "
#define pl(n) cout<<n
#define FOR(i,j,n) for(i=j;i<=n;i++)
#define FORR(i,j,n) for(i=j;i>=n;i--)
#define SORT(n) std::sort(n.begin(),n.end())
#define FILL(n,a) std::fill(n.begin(),n.end(),a)
#define ALL(n) n.begin(),n.end()
#define rsz resize
#define pb push_back
#define MAXINT std::numeric_limits<int>::max()
#define MININT std::numeric_limits<int>::min()
#define gc getchar_unlocked
#define pc putchar_unlocked
#define iOS std::ios_base::sync_with_stdio(false)
#define endl "\n"
#define INF 1000000000000000005LL
#define INFI 1009990000
#ifdef DEBUG
    #define debugHello() cout << "Hello" << endl
#else
    #define debugHello()
#endif
#ifdef DEBUG
    #define debug(x) cout << #x << " = " << x << endl
#else
    #define debug(x)
#endif
using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<bool> vb;
typedef vector<vector<int> > vvi;
typedef vector<vector<ll> > vvl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
const ld eps = 0.0000001L;
/**************** TEMPLATE ENDS HERE *************************/
const int MAXN = 153;
string ar[MAXN], ans[MAXN];
bool lst[MAXN][MAXN];
void fillCells(int rl, int cl,int i,int j,char c) {
    int ri,ci;
    FOR(ri,rl, i) {
        FOR(ci, cl, j) {
            ans[ri][ci] = c;
        }
    }
}
int main() {
    int t,tt,i,j,r,c;
    cin>>t;
    FOR(tt,1,t) {
        sl(r);sl(c);
        FOR(i,0,r-1) cin>>ar[i];
        FOR(i,0,r-1) ans[i].resize(c);
        memset(lst, false,sizeof(lst));
        FOR(i,0,r-1) {
            FORR(j,c-1,0) {
                if (ar[i][j] != '?') {
                    lst[i][j]=true;
                    break;
                }
            }
        }
        int lastRow = -1;
        bool done = false;
        FORR(i,r-1,0) {
            FOR(j,0,c-1) {
                if (ar[i][j] != '?') {
                    lastRow = i;
                    done = true;
                    break;
                }
            }
            if (done) break;
        }
        int rl,cl;
        rl=cl=0;
        done = false;
        FOR(i,0,r-1) {
            FOR(j,0,c-1) {
                if (ar[i][j] != '?') {
                    if (lst[i][j]) {
                        if (i != lastRow) {
                            fillCells(rl,cl,i,c-1, ar[i][j]);
                            rl = i+1;
                            cl = 0;
                            break;
                        } else {
                            fillCells(rl,cl,r-1,c-1, ar[i][j]);
                            rl = i+1;
                            cl = 0;
                            done = true;
                            break;
                        }
                    } else {
                        if (i != lastRow) {
                            fillCells(rl,cl,i,j, ar[i][j]);
                            cl = j+1;
                        } else {
                            fillCells(rl,cl,r-1,j, ar[i][j]);
                            cl = j+1;
                        }
                    }
                }        
            }
            if (done) break;
        }
        cout<<"Case #"<<tt<<":"<<endl;
        FOR(i,0,r-1) {
            cout<<ans[i]<<endl;
        }
    }
    return 0;
}
