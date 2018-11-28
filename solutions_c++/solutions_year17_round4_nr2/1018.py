#include<stdio.h>
#include<algorithm>
#include<vector>
#define pb push_back
using namespace std;

int n,C,m;
int c[1005],a[1005],c1[1005];

int f(int v)
{
    int i,j,t,x=n,res=0;
    for(i=1;i<=n;i++){
        c[i]=a[i];
    }
    for(i=n;i>=1;i--){
        x=min(x,i);
        if(c[i]>v){
            t=c[i]-v;
            while(1){
                if(x==0)return -1;
                if(c[x]>v){
                    x--;
                    continue;
                }
                else if(c[x]+t<=v){
                    c[x]+=t;
                    break;
                }
                else{
                    t-=(v-c[x]);
                    c[x]=v;
                    x--;
                }
            }
            c[i]=v;
            res+=t;
        }
    }
    return res;
}

int main()
{
    freopen("1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T,lt,p,b,s,e,mid,i,mem;
    scanf("%d", &T);
    for(lt=1;lt<=T;lt++)
    {
        scanf("%d %d %d", &n, &C, &m);
        for(i=1;i<=m;i++){
            scanf("%d %d", &p, &b);
            c[p]++;
            c1[b]++;
        }
        s=0;
        for(i=1;i<=C;i++){
            s=max(s,c1[i]);
        }
        for(i=1;i<=n;i++)a[i]=c[i];
        e=m;
        while(s<=e){
            mid=(s+e)/2;
            if(f(mid)!=-1)e=mid-1,mem=mid;
            else s=mid+1;
        }
        printf("Case #%d: %d %d\n", lt, mem, f(mem));
        for(i=1;i<=n;i++)c[i]=0;
        for(i=1;i<=C;i++)c1[i]=0;
    }
    return 0;
}
