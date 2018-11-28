#include <bits/stdc++.h>
#define maxn 100
#define REP(i,x,y) for(int i=x;i<(y);i++)
#define RREP(i,x,y) for(int i=x;i>(y);i--)
using namespace std;
typedef long long ll;
ll n,k;
int a[maxn];
map<ll,int>ma;
int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("data.out","w",stdout);
    int T;scanf("%d",&T);int cas=1;
    while(T--){
        scanf("%I64d %I64d",&n,&k);
        ma.clear();
        REP(i,1,k+1){
            ll tmp;
            if(!ma.empty()){
                map<ll,int>::reverse_iterator it=ma.rbegin();
                tmp=(*it).first;
                ma[tmp]--;
                if(ma[tmp]==0) ma.erase(tmp);
            }
            else tmp=n;
            if(tmp/2LL) ma[tmp/2LL]++;
            if(tmp-tmp/2LL-1LL) ma[tmp-tmp/2LL-1LL]++;
            if(i==k) printf("Case #%d: %I64d %I64d\n",cas++,tmp/2LL,tmp-tmp/2LL-1LL);
        }
    }
}
