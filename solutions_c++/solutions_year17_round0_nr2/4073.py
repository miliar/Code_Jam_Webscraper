#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <stack>
#include <queue>
#include <utility>
#include <bitset>
#define fi first
#define se second
#define mkp make_pair
#define pb push_back
#define rep(i,a,b) for (int i=(a);i<(b);i++)
#define per(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,a,b) for (int i=(a);i<=(b);i++)
#define PER(i,a,b) for (int i=(b);b>=(a);i--)
using namespace std;
typedef long long LL;

const int INF = 0x3f3f3f3f;

const int MAXN = 1000005; // 1e6;
char str[MAXN];
char ans[MAXN];
int T;
int main()
{
        freopen("B-large.in","r",stdin);
        freopen("B_large.txt","w",stdout);
        cin>>T;
        rep(cas,1,T+1)
        {
                cin>>str;
                int len = strlen(str);
                int now = 0;
                ans[len]='\0';
                rep(i,0,len)
                {
                        ans[i]=str[i];
                        if (ans[i]<ans[i-1]) {
                                rep(j,i,len) ans[j]='9';
                                now = i;
                                break;
                        }
                }
                per(i,0,now)
                {
                        ans[i]--;
                        if (i != 0 && ans[i]<ans[i-1]) ans[i]='9';
                        else break;
                }
                cout<<"Case #"<<cas<<": ";
                if (ans[0] == '0') cout<<ans+1<<endl;
                else cout<<ans<<endl;

        }
}
