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
struct node
{
    int cnt;
    int p;
}tmp[6],res[3];
char ch[6]={'R','O','Y','G','B','V'};
bool cmp(node a,node b){
    return a.cnt > b.cnt;
}
int main()
{
#ifdef LOCAL
    freopen("B-small-attempt3.in","r",stdin);
    freopen("out1.txt","w",stdout);
#endif
    int t;cin >> t;
    int ks = 1;
    while(t--){
        int n;cin >> n;
        for(int i=0;i<6;i++)cin >> tmp[i].cnt;
        int tot = tmp[0].cnt+tmp[2].cnt + tmp[4].cnt;
        //if(tot > 10)continue;
        for(int i=0;i<6;i++)tmp[i].p = i;
        res[0] = tmp[0],res[1] = tmp[2],res[2] = tmp[4];
        sort(res,res+3,cmp);
        std::vector<char> v;
        int ok = 1;
       // cout << res[0].cnt << ch[res[0].p] << endl;
       // cout << res[1].cnt << ch[res[1].p] << endl;
        //cout << res[2].cnt << ch[res[2].p] << endl;
        while(res[1].cnt){
            v.push_back(ch[res[0].p]);
            v.push_back(ch[res[1].p]);
            res[0].cnt--;
            res[1].cnt--;
            
        }
        while(res[0].cnt && res[2].cnt){
            v.push_back(ch[res[0].p]);
            v.push_back(ch[res[2].p]);
            res[0].cnt--;
            res[2].cnt--;  
        }
        while(res[2].cnt){
            int tmp = v.size();
            for(int i=1;i<v.size();i++){
                if(v[i-1] != ch[res[2].p] && v[i]!=ch[res[2].p]){
                    v.insert(v.begin()+i,ch[res[2].p]);
                    break;
                }
            }
            if(tmp==v.size()){
                ok = 0;
            }
            res[2].cnt--;
        }
        printf("Case #%d: ",ks++);
        if(ok && v.size()==tot){
            for(int i=0;i<v.size();i++)printf("%c",v[i]);
            cout << '\n';
        }else{
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}