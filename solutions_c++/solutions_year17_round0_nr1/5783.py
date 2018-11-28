
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
#define eps 1e-9
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

int k;
char str[1005];
int main(){
    int t;
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d" ,&t);
    lp(cnt, 1, t){
        scanf("%s%d" ,str,&k);
        int ans = 0 , n = (int) strlen(str);
        lp(i, 0, n-k) {
            if(str[i] == '-') {
                ++ans;
                lp(j, i, i+k-1) str[j] = str[j] == '-' ? '+':'-';
            }
        }
        printf("Case #%d: ",cnt);
        bool done = true;
        lp(i, 0, n-1) done &= str[i] == '+';
        if(!done) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
    return 0;
}
/*
 */









