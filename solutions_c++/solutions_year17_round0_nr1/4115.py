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
int T,k;
int main()
{
        freopen("A-large.in","r",stdin);
        freopen("a_large.txt","w",stdout);
        cin>>T;
        rep(cas,1,T+1)
        {
                cin>>str>>k;
                int len = strlen(str);
                int cnt = 0;
                rep(i,0,len+1-k)
                {
                        if (str[i]=='-')
                        {
                                cnt ++;
                                rep(j,i,i+k)
                                {
                                        if (str[j]=='-') str[j]='+';
                                        else if (str[j]=='+') str[j]='-';
                                }
                        }
                }
                bool flag = true;
                rep(i,0,len) if (str[i]=='-') flag = false;

                if (flag)
                {
                        printf("Case #%d: %d\n",cas,cnt);
                }
                else printf("Case #%d: IMPOSSIBLE\n",cas);
        }
        fclose(stdin);
        fclose(stdout);
}
