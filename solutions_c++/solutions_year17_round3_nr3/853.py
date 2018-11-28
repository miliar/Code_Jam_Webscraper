#include <bits/stdc++.h>
#define N 100009
#define mod 1000000007
#define inf 1000000000
using namespace std;
typedef long long ll;
typedef double db;

double a[N];

void solve(int tc){
    printf("Case #%d: ",tc);
    int n,k; scanf("%d %d",&n,&k);
    double u; scanf("%lf",&u);
    for(int i=0;i<n;i++){
        scanf("%lf",a+i);
    }
    sort(a,a+n); a[n]=1.0;
    double p=0.,q=1.;
    for(int t=0;t<200;t++){
        double mid = .5*(p+q), sum = 0.;
        for(int i=0;i<n;i++){
            if(a[i]<mid) sum+=mid-a[i];
        }
        if(sum > u) q=mid;
        else p=mid;
    }
    double ans=1.;
    for(int i=0;i<n;i++){
        ans*=max(p,a[i]);
    }
    printf("%.10f\n",ans);
}

int main(){
    freopen("C-small-1-attempt1.in","r",stdin); freopen("out.txt","w",stdout);
    int t; scanf("%d",&t);
    for(int i=1;i<=t;i++) solve(i);
    return 0;
}
