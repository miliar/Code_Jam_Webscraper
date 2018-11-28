//g++ -std=c++11 -g -O2 -o ./a ./A.cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define ff first
#define ss second
#define nl '\n'
//////////////////////////////////////////////////////////////////////

const int N = 100;
int n,k;
double p[N],u;
const double eps = 1e-6;

int main(){
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);  
  int tc;cin>>tc;
  for(int tt=1;tt<=tc;tt++){
    cout<<"Case #"<<tt<<": ";

    cin>>n>>k>>u;
    for(int i=1;i<=n;i++)cin>>p[i];
    sort(p+1,p+1+n);

    p[n+1]=100;
    while(u>0.0){
      int i;
      for(i=1;i<=n and p[i]==p[1];i++);
      
      if( (p[i]-p[1])*(i-1) > u){
	for(int j=1;j<i;j++)p[j] += u/(i-1);
	u=0.0;
      }else{
	u -= (p[i]-p[1])*(i-1);
	for(int j=1;j<i;j++)p[j] = p[i];
      }
      //for(int i=1;i<=n;i++)cerr<<p[i]<<" \n"[i==n];
    }

    double ans = 1;

    for(int i=1;i<=n;i++)ans*=p[i];

    cout<<ans<<endl;
    cerr<<tt<<":"<<ans<<endl;
  }
  return 0;
}
