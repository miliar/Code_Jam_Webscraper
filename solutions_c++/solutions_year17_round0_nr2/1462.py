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
int main(){
    freopen("C:\\Users\\meixinyu\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\meixinyu\\Desktop\\out.txt","w",stdout);
    int t;cin >> t;
    int kase = 1;
    while(t--){
        printf("Case #%d: ",kase++);
        ll n;cin >> n;
        //cout << n << endl;
        int tmp[25];
        MEM(tmp,0);
        int l = -1;
        ll m = n;
        while(n){
            tmp[++l] = n%10;
            n/=10;
        }
        l = max(0,l);
        int i;
        for(i=l;i>=1;i--){
            if(tmp[i]>tmp[i-1])break;
        }
        if(i==0 || l==0){
            cout << m;
        }
        else{
            if(tmp[i]>1){
                //for(int j=l;j>i;j--)printf("%d",tmp[j]);
                int t = tmp[i];
                int tt = i;
                //cout << tmp[i] << endl;
                while(tt<=l && tmp[tt]==t)tt++;
                tmp[--tt]--;
                for(int j=l;j>=tt;j--)printf("%d",tmp[j]);
                for(int j=0;j<tt;j++)printf("%d",9);
            }
            else{
                for(int i=0;i<l;i++)printf("%d",9);
            }
        }
        cout << '\n';
    }  
}