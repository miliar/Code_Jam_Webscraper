#include<bits/stdc++.h>
#define double long double
using namespace std;
typedef pair<double,int> P;
int main(){
  int T;
  cin>>T;
  for(int i=1;i<=T;i++){
    int n,k;
    cin>>n>>k;
    P p[1000];
    double r[1000],h[1000];
    for(int j=0;j<n;j++)
      cin>>r[j]>>h[j],p[j].first=r[j]*h[j]*2*M_PI,p[j].second=j;
    sort(p,p+n);
    double ans=0;
    for(int a=n-1;a>=0;a--){
      double cl=p[a].first+M_PI*r[p[a].second]*r[p[a].second];
      int cnt=1;
      for(int j=n-1;j>=0&&cnt<k;j--){
	if(j==a||r[p[a].second]<r[p[j].second])continue;
	cnt++;
	cl+=p[j].first;
      }
      ans=max(ans,cl);
    }
    cout<<"Case #"<<i<<": ";
    printf("%.9Lf",ans);
    cout<<endl;
  }
  return 0;
}
