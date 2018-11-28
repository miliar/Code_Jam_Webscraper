#include<stdio.h>
#include<iostream>
#include<map>
#include<string.h>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long LL;
const int N = 1005;
int n,m;
struct Node{
    int l,r;
    int id;
    bool operator < (const Node& o) const{
        return l<o.l;
    }
}a[N];

int sum[2];
const double pi = acos(-1.0);
int getInterval(int i,int j){
    if(i<j){
        return a[j].l-a[i].r;
    }else{
        return 1440-a[i].r+a[j].l;
    }
}
void merge(int u,int v){
    if(u<v){
        a[u].r = a[v].r;
        for(int i=v;i<n-1;i++){
            a[i] = a[i+1];
        }
        n--;
    }else{
        a[u].r = 1440;
        a[v].l=0;
    }
}
bool merge(int u){
    int v = (u+1)%(n);
    int id = a[v].id;
    int interval = getInterval(u,v);

    if(sum[id]+interval>720) return false;
    // printf("merge [%d,%d) and [%d,%d)\n",a[u].l,a[u].r,a[v].l,a[v].r);
    sum[id]+=interval;
    merge(u,v);

    return true;
}
int getAns(){
    int res = 0;
    if(n==1) return 2;
    for(int i=0;i<n;i++){
        int j = (i+1)%n;
        if(j>i){
            if(a[i].id!=a[j].id) res++;
            else res+=2;
        }else{
            if(a[i].r==1440 && a[j].l==0){
                if(a[i].id!=a[j].id) res++;
            }else{
                if(a[i].id!=a[j].id) res++;
                else res+=2;
            }

        }

    }
    return res;
}
int main(){
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T;scanf("%d",&T);
    int cas = 1;
    while(T--){
        scanf("%d%d",&n,&m);
        // printf("n=%d, m=%d\n",n,m);
        sum[0]=sum[1]=0;
        for(int i=0;i<n;i++){
            a[i].id = 0;
            scanf("%d%d",&a[i].l,&a[i].r);
            sum[0]+=a[i].r-a[i].l;
        } 
        for(int i=n;i<m+n;i++){
            a[i].id = 1;
            scanf("%d%d",&a[i].l,&a[i].r);
            sum[1]+=a[i].r-a[i].l;
        }
        
        n+=m;
        
        sort(a,a+n);

        // for(int i=0;i<n;i++){
        //     printf("[%d,%d) ",a[i].l,a[i].r);
        // }
        // puts("");
        int num = 300;
        while(num--){
            if(n==1) break;
            int pos = -1, interval = 100000;
            for(int i=0;i<n;i++){
                int j = (i+1)%(n);
                if(j<i && a[j].l==0 && a[i].r==1440) continue;
                if(a[i].id!=a[j].id) continue;
                int tmp = getInterval(i,j);
                if(tmp<interval) pos = i,interval = tmp;
            }
            // printf("pos:%d\n",pos);
            if(pos==-1) break;
            if(!merge(pos)) break;
            // for(int i=0;i<n;i++){
            //   printf("[%d,%d) ",a[i].l,a[i].r);
            // }
            // puts("");
        }
        printf("Case #%d: %d\n",cas++,getAns());
        // puts("");



    }

    return 0;
}
