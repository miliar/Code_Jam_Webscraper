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
#define per(i,b,a) for (int i=(b)-1;i>=(a);i--)
#define REP(i,a,b) for (int i=(a);i<=(b);i++)
#define PER(i,b,a) for (int i=(b);i>=(a);i--)
using namespace std;
typedef long long LL;

const int INF = 0x3f3f3f3f;

const int MAXN = 1000005; // 1e6;
int T,r,c;
char f[500][500];
int main()
{
        freopen("A-large.in","r",stdin);
        freopen("outA_large.txt","w",stdout);
        scanf("%d",&T);
        rep(cas,1,T+1)
        {
                scanf("%d%d",&r,&c);
                rep(i,0,r) scanf(" %s",f[i]);
                rep(i,0,r)
                {
                        char now = '?';
                        rep(j,0,c)
                        {
                                if (f[i][j]=='?') f[i][j]=now;
                                else now = f[i][j];
                        }
                        now = '?';
                        per(j,c,0)
                        {
                                if (f[i][j]=='?') f[i][j]=now;
                                else now = f[i][j];
                        }
                }
                stack<int> s;
                rep(i,0,r)
                {
                        if (f[i][0]=='?') s.push(i);
                        else
                        {
                                while(!s.empty())
                                {
                                        int k = s.top();s.pop();
                                        rep(j,0,c)
                                        {
                                                f[k][j] = f[i][j];
                                        }
                                }
                        }
                }

                while(!s.empty()) s.pop();
                per(i,r,0)
                {
                        if (f[i][0]=='?') s.push(i);
                        else
                        {
                                while(!s.empty())
                                {
                                        int k = s.top();s.pop();
                                        rep(j,0,c)
                                        {
                                                f[k][j] = f[i][j];
                                        }
                                }
                        }
                }
                printf("Case #%d:\n",cas);
                rep(i,0,r) printf("%s\n",f[i]);
        }
}

