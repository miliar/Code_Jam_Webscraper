#include<stdio.h>
#include<set>
#include<map>
using namespace std;
typedef long long LL;

set<LL> s;
set<LL>::iterator it;
map<LL,LL> m;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T,t,lt;
    LL n,k,x,v;
    scanf("%d", &T);
    for(lt=1;lt<=T;lt++)
    {
        scanf("%lld %lld", &n, &k);
        t=0;
        s.clear();
        m.clear();
        s.insert(n);
        m[n]=1;
        while(1){
            it=s.end();
            it--;
            x=*it;
            v=m[x];
            s.erase(it);
            if(k<=v){
                printf("Case #%d: %lld %lld\n", lt, x/2, (x-1)/2);
                break;
            }
            if(m.find(x/2)!=m.end())m[x/2]+=v;
            else m[x/2]=v;
            if(m.find((x-1)/2)!=m.end())m[(x-1)/2]+=v;
            else m[(x-1)/2]=v;
            s.insert(x/2);
            s.insert((x-1)/2);
            k-=v;
        }
    }
    return 0;
}
