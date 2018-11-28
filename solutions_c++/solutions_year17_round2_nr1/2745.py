
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
#define mod 1000000007
#define eps 1e-6
#define infi 1e9
#define infll 1e18
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



int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    scanf("%d",&t);
    lp(cnt, 1, t){
        int n;
        double d,ans = infll;
        scanf("%lf%d",&d,&n);
        
        lp(i, 1, n) {
            double k,s;
            scanf("%lf%lf",&k,&s);
            ans = min(ans,d*s/(d-k));
        }
        printf("Case #%d: %.8lf\n",cnt,ans);
    }
    return 0;
}


//ios::sync_with_stdio(0);cin.tie(0);
/*
 abcda
 
 */

