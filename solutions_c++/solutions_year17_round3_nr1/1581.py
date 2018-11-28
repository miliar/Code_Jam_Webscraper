#include<bits/stdc++.h>
using namespace std;

const int N=1010;
const double P=3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706;
int n, t, k;
double r[N], h[N];
pair<double, int> sv[N];
bool vis[N];

int main()
{
   freopen("r.txt","r", stdin);
   freopen("output.txt","w", stdout);
   scanf("%d", &t);
   for(int u=1;u<=t;u++){
    double sum=0;
    memset(vis, 0, sizeof vis);
    double ans=0;
    cin>>n>>k;
    for(int i=0;i<n;i++){
        cin>>r[i]>>h[i];
        sv[i]={r[i]*h[i], i};
    }
    sort(sv, sv+n);
    reverse(sv, sv+n);
    for(int i=0;i<k;i++){
        sum+=sv[i].first, vis[sv[i].second]=1;
    }
    for(int i=0;i<n;i++){
        double tmp=0;
        if(vis[i])
            tmp=(double)(P*r[i]*r[i])+(double)(2*P*sum);
        else{
            double sum2=sum+(r[i]*h[i])-sv[k-1].first;
            tmp=(double)(P*r[i]*r[i])+(double)(2*P*sum2);
        }
        //printf("%f  ", tmp);
        ans=max(ans, tmp);
    }
    printf("Case #%d: %.9f\n", u, ans);
   }

    return 0;
}
