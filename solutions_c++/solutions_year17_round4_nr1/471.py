/*  ^^ ====== ^^ 
ID: meixiuxiu
PROG: test
LANG: C++11
*/
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cctype>
#include <bitset>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int ,int> pii;
#define MEM(a,b) memset(a,b,sizeof a)
#define CLR(a) memset(a,0,sizeof a);
#define pi acos(-1.0)
#define maxn 40000
#define maxv 100005
const int inf = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
std::map<int,int> mp;
int main()
{
#ifdef LOCAL
    freopen("A-large.in", "r", stdin);
    freopen("out.txt","w",stdout);
#endif
    int kase = 1;
    int t;cin >> t;
    int n,p;
    while(t--){
        cin >> n >> p;
        std::vector<int> v;
        mp.clear();
        for(int i=1;i<=n;i++){
            int a;cin >> a;
            int tt = a%p;
            if(tt && mp[p-tt]==0)mp[tt]++;
            else if(mp[p-tt])mp[p-tt]--;
            else mp[tt]++;
        }
        for(int i=0;i<p;i++){
            for(int j=0;j<mp[i];j++){
                v.push_back(i);
            }
        }
        int cnt = (n-v.size())/2;
        int pos = 0;
        int last = 0;
        while(pos < v.size()){
            if(v[pos]==0){
                pos++;
                continue;
            }
            if(last){
                if(last >= v[pos]){
                    last -= v[pos];
                    cnt++;
                }
                else{
                    last = p - (v[pos]-last);
                    cnt++;
                }
            }
            else{
                last = p-v[pos];
            }
            pos++;
        }
        printf("Case #%d: %d\n",kase++,n-cnt);
    }
    return 0;
}