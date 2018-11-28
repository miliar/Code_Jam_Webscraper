#include<stdio.h>
#include<algorithm>

struct data
{
    int s,e,v;
    data(){};
    data(int s, int e, int v):s(s),e(e),v(v){};
    bool operator<(const data &r)const{
        return s<r.s;
    }
};

struct Time
{
    int x,v;
    Time(){};
    Time(int x, int v):x(x),v(v){};
};

int k1,k2;
data a[505];
Time A[505],B[505];
int d[505][1500],d2[505][1500];
int MX=1e9;

int max(int a, int b)
{
    if(a<b)return b;
    return a;
}
int min(int a, int b)
{
    if(a>b)return b;
    return a;
}

void DP()
{
    int i,j,k;
    for(i=0;i<=k1;i++){
        for(j=0;j<=1440;j++)d[i][j]=MX;
    }
    d[0][0]=0;
    for(i=1;i<=k1;i++){
        for(j=0;j<=1440;j++){
            d[i][j]=d[i-1][j];
            for(k=0;k<=A[i].x&&j-k>=0;k++){
                d[i][j]=min(d[i][j],d[i-1][j-k]+A[i].v);
            }
        }
    }
    for(i=0;i<=k2;i++){
        for(j=0;j<=1440;j++)d2[i][j]=MX;
    }
    d2[0][0]=0;
    for(i=1;i<=k2;i++){
        for(j=0;j<=1440;j++){
            d2[i][j]=d2[i-1][j];
            for(k=0;k<=B[i].x&&j-k>=0;k++){
                d2[i][j]=min(d2[i][j],d2[i-1][j-k]+B[i].v);
            }
        }
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n,m,s,e,i,N,t,res,l,lt,ans,cnt;
    scanf("%d", &lt);
    for(l=1;l<=lt;l++){
        res=0;
        cnt=0;
        k1=k2=1;
        ans=MX;
        scanf("%d %d", &n, &m);
        for(i=1;i<=n;i++){
            scanf("%d %d", &s, &e);
            a[i]=data(s,e,0);
        }
        for(i=1;i<=m;i++){
            scanf("%d %d", &s, &e);
            a[i+n]=data(s,e,1);
        }
        N=n+m;
        std::sort(a+1,a+N+1);
        t=a[1].s+1440-a[N].e;
        if(a[1].v!=a[N].v)cnt++;
        if(a[1].v==0){
            if(a[1].v==a[N].v)A[k1++]=Time(t,2);
            else A[k1++]=Time(t,0);
        }
        else{
            if(a[1].v==a[N].v)B[k2++]=Time(t,2);
            else B[k2++]=Time(t,0);
        }
        t=a[1].e+1440-a[N].e;
        if(a[1].v==0)res+=t;
        else res-=t;
        for(i=2;i<=N;i++){
            if(a[i].v!=a[i-1].v){
                t=a[i].s-a[i-1].e;
                if(a[i].v==0)A[k1++]=Time(t,0);
                else B[k2++]=Time(t,0);
                cnt++;
            }
            else{
                t=a[i].s-a[i-1].e;
                if(a[i].v==0)A[k1++]=Time(t,2);
                else B[k2++]=Time(t,2);
            }
            if(a[i].v==0)res+=(a[i].e-a[i-1].e);
            else res-=(a[i].e-a[i-1].e);
        }
        res/=2;
        k1--,k2--;
        DP();
        for(i=max(res,0);i<=1440;i++){
            if(d[k1][i]!=MX&&d2[k2][i-res]!=MX)ans=min(ans,d[k1][i]+d2[k2][i-res]);
        }
        if(i>1440){
            printf("Case #%d: %d\n", l, cnt+ans);
            continue;
        }
    }
    return 0;
}
