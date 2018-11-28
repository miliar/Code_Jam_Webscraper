#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <climits>
#include <utility>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#define REP(i,n) for(int (i)=0;i<(int)(n);++(i))
#define REPIT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define PB push_back
#define FT first
#define SD second
#define ZERO(x) memset(x,0,sizeof(x))
#define NEG(x) memset(x,-1,sizeof(x))
#define RI(x) scanf("%d",&(x))
#define RII(x,y) scanf("%d%d",&(x),&(y))
#define RIII(x,y,z) scanf("%d%d%d",&(x),&(y),&(z))
#define OIII(x,y,z) printf("%d %d %d\n",(x),(y),(z))
#define OII(x,y) printf("%d %d\n",(x),(y))
#define OI(x) printf("%d\n",(x))
#define OL(x) cout<<(x)<<endl
#define OLL(x,y) cout<<(x)<<" "<<(y)<<endl
#define OLLL(x,y,z) cout<<(x)<<" "<<(y)<<" "<<(z)<<endl
#define RS(s) scanf("%s",(s))
#define MP(x,y) make_pair((x),(y))
#define SZ(x) ((int)(x).size())
#define FIN(f) freopen(f,"r",stdin)
#define FOUT(f) freopen(f,"w",stdout)
typedef long long LL;
using namespace std;
typedef pair<int,int> PII;
const int MOD = 1e9+7;
const int maxn = 222222;
int t;
int n,p;
double q[55][55];
double r[55];
double  R[2][55];
int arr[10];
bool cnt1(double x) {
    bool f = 0;
    int N = x / R[1][0] - 1;
    while(1) {
        N++;
        if(N*R[0][0] > x)break;
        if(N*R[0][0] <= x && N*R[1][0] >= x) {
            f = 1;
            break;
        }
    }
    return f;
}
bool cnt(double x, double y) {
    bool f = 0;
    int N = max(x / R[1][0] - 1, y / R[1][1] - 1);
    while(1) {
        N++;
        if(N*R[0][0] > x || N*R[0][1] > y)break;
        if(N*R[0][0] <= x && N*R[0][1] <= y && N*R[1][0] >= x && N*R[1][1] >= y) {
            f = 1;
            break;
        }
    }
    return f;
}
int ok() {
    int ret = 0;
    for(int i=0; i<p;++i) {
        ret += cnt(q[0][i], q[1][arr[i]]);
    }
    return ret;
}
int main(int argc, char const *argv[])
{
    RI(t);
    REP(kase, t) {
        RII(n,p);
        REP(i,n){
            cin>>(r[i]);
            R[0][i] = r[i] * 0.9;
            R[1][i] = r[i] * 1.1;
        }
        REP(i,n)REP(j,p)cin>>q[i][j];
        int ans = 0;
        if(n==2) {
        for(int i=0;i<p;++i)arr[i] = i;
        do {
            ans = max(ans, ok());
        } while(next_permutation(arr,arr+p));
        } else {
            for(int i=0;i<p;++i) {
                ans += cnt1(q[0][i]);
            }
        }

        printf("Case #%d: %d\n", kase+1, ans);
    }
    return 0;
}