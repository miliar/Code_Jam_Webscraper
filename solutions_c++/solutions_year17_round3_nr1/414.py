#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#define pb push_back
#define mp make_pair
#define eps 1e-9
#define zero(x) (fabs(x)<eps)
#define pi acos(-1.0)
#define f1 first
#define f2 second
#define CLR(x,y) memset(x,y,sizeof(x))
using namespace std;
#define fr(i,x,y) for(int i=x;i<=y;i++)
typedef long long ll;
typedef pair <int, int> PII;
template<typename X> inline bool minimize(X&p,X q){if(p<=q)return 0;p=q;return 1;}
template<typename X> inline bool maximize(X&p,X q){if(p>=q)return 0;p=q;return 1;}
int  n,k;
struct node{
    int r,h;
    ll t;
    bool operator<(const node&oth )const{
        return t>oth.t;
    }
}a[1005];
void doit(){
    scanf("%d%d",&n,&k);
    fr(i,1,n)
    {
        scanf("%d%d",&a[i].r,&a[i].h);
        a[i].t=1LL*a[i].r*a[i].h*2;
    }
    sort(a+1,a+1+n);

    int xx;
    ll tmp,an=0;
    fr(i,1,n){
        tmp=1LL*a[i].r*a[i].r+a[i].t;
        xx=1;
        fr(j,1,n){
            if (xx==k)break;
            if (a[j].r>a[i].r||i==j) continue;
            tmp+=a[j].t;
            xx++;
        }
        if (tmp>an) an=tmp;
    }
    printf("%.6lf\n",pi*an);

}
int main() {
    freopen("A-large (2).in","r",stdin);
    freopen("A-large (2).out","w",stdout);

    int cas,i=0;
    scanf("%d",&cas);
    while (cas--)
    {
        printf("Case #%d: ",++i);
        doit();

    }
}