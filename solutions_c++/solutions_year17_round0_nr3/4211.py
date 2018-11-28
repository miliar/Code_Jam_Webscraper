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
typedef pair<int,int> P;
const int INF = 0x3f3f3f3f;

const int MAXN = 1000005; // 1e6;
int T,k,n;
int main()
{
        freopen("C-small-2-attempt0.in","r",stdin);
        freopen("C-small-2.txt","w",stdout);
        cin>>T;
        rep(cas,1,T+1)
        {
                cin>>n>>k;
                priority_queue<int> que;
                que.push(n);
                rep(i,0,k-1)
                {
                        int q = que.top();
//                        cout<<q<<endl;
                        que.pop();
                        int p = (q-1)/2;
                        que.push(p);
                        que.push(q-1-p);
                }
                int q = que.top();
                int p = (q-1)/2;
                printf("Case #%d: %d %d\n",cas,q-p-1,p);
        }
}
