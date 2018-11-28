#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
const double PI=  3.1415926535897932;
double ans;
int n, k, cases;
long long r[1010], h[1010];
long long tmpr[1010], tmph[1010];


bool cmp(int a, int b){
    if(r[a]*h[a]>r[b]*h[b])
        return 1;
    return 0;
}
void mergeSort(int L, int R)
{
    if(L>=R) return;
    int M=(R-L)/2+L;
    mergeSort(L,M);
    mergeSort(M+1,R);
    int i=L, j=M+1, t=L-1;
    while(i<=M && j<=R){
        if(cmp(i, j)){
            tmpr[++t]=r[i];tmph[t]=h[i];
            ++i;
        }
        else{
            tmpr[++t]=r[j];tmph[t]=h[j];
            ++j;
        }
    }
    while(i<=M){
        tmpr[++t]=r[i];tmph[t]=h[i];
        ++i;
    }
    while(j<=R){
        tmpr[++t]=r[j];tmph[t]=h[j];
        ++j;
    }
    for(int p=L;p<=R;++p){
        r[p]=tmpr[p];h[p]=tmph[p];
    }
}
void init()
{
    scanf("%d%d",&n,&k);
    long long R=-10, H=-10;
    for(int i=1;i<=n;++i){
        scanf("%lld%lld",&r[i],&h[i]);
        if(R<r[i] || (R==r[i] && H<h[i])){
            R=r[i]; H=h[i];
        }
    }
    mergeSort(1,n);
//for(int i=1;i<=n;++i)
    //cout<<r[i]<<' '<<h[i]<<endl;

    long long R2=-10, H2=-10;
    for(int i=1;i<=k;++i){
        if(R2<r[i] || (R2==r[i] && H2<h[i])){
            R2=r[i];H2=h[i];
        }
    }

    for(int i=k+1;i<=n;++i){
        if(r[i]>R2 && r[i]*r[i]+2*r[i]*h[i]>R2*R2+2*r[k]*h[k]){
            R2=r[k]=R; H2=h[k]=H;
        }
    }
    //cout<<ok<<endl;
    ans=R2*R2;
    for(int i=1;i<=k;++i)
        ans+=2*r[i]*h[i];
    ans*=PI;
}

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("a-l.out","w",stdout);
    scanf("%d",&cases);
    for(int kase=1;kase<=cases;++kase){
        init();
        cout<<"Case #"<<kase<<": ";
        cout.precision(9);
        cout.setf(ios::fixed);
        cout<<ans<<endl;
        //printf("Case #%d: %f\n",kase, ans);
    }

    return 0;
}
