#include<set>
#include <unordered_set>
#include <unordered_map>
#include<map>
#include<list>
#include<iomanip>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<sstream>
#include<iostream>
#include<fstream>
#include<algorithm>
#include<numeric>
#include<utility>
#include<functional>
#include<stdio.h>
#include<assert.h>
#include<memory.h>
#include<bitset>
#include<math.h>
#include <string.h>

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define lp(i,a,n) for(int i=(a);i<=(int)(n);++i)
#define lpd(i,a,n) for(int i=(a);i>=(int)(n);--i)
#define clr(a,b) memset(a,b,sizeof a)
#define all(v) v.begin(),v.end()
#define println(a) cout <<(a) <<endl
#define sz(x) ((int)(x).size())
#define readi(x) scanf("%d",&x)
#define read2i(x,y) scanf("%d%d",&x,&y)
#define read3i(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define readll(x) scanf("%I64d",&x)
#define mod 1000000007ll
#define eps 1e-10
#define infi 1000000000ll
#define infll 1000000000000000000ll


using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef set<int> si;
typedef map<int,int> mii;
typedef map<ll,ll> mll;

const int N = 1004;

int n,k;
double dp[N][N];
bool vis[N][N];
pll p[N];

double solve(int i,int j) {
    
    if(j < 0) return -infll;
    if(i == n+1) return !j ?0:-infll;
    
    if(vis[i][j]) return dp[i][j];
    vis[i][j] = true;
    if(j == k) dp[i][j] = 2.0*M_PI*p[i].f*p[i].s+ M_PI*p[i].f*p[i].f + solve(i+1, j-1);
    else dp[i][j] = 2.0*M_PI*p[i].f*p[i].s + solve(i+1, j-1);
        
    return dp[i][j] = max(dp[i][j], solve(i+1, j));
}

int main(){
    
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    scanf("%d" ,&t);
    lp(cnt, 1, t) {
        scanf("%d%d" ,&n,&k);
        lp(i, 1, n)
            scanf("%lld%lld\n",&p[i].f,&p[i].s);
        
        sort(p+1, p+n+1,[](pll a, pll b){return a>b;});
        clr(vis,false);
        printf("Case #%d: %lf\n",cnt,solve(1, k));
    }
    return 0;
}


/*
 4
 2 1
 100 20
 200 10
 2 2
 100 20
 200 10
 3 2
 100 10
 100 10
 100 10
 4 2
 9 3
 7 1
 10 1
 8 4

 */