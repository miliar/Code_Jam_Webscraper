//g++ -std=c++11 -g -O2 -o ./a ./A.cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define ff first
#define ss second
#define nl '\n'
//////////////////////////////////////////////////////////////////////

const int N = 1010;
int n,k;
pair<double,double> c[N];
const double ppi = 3.14159265358979323846;
priority_queue<double,vector<double>,greater<double> > pq;

int main(){
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);  
  int tc;cin>>tc;
  for(int tt=1;tt<=tc;tt++){
    cout<<"Case #"<<tt<<": ";
    
    cin>>n>>k;
    for(int i=1;i<=n;i++)cin>>c[i].ff>>c[i].ss;

    sort(c+1,c+1+n,greater<pair<double,double> >());

    //for(int i=1;i<=n;i++)cerr<<c[i].ff<<','<<c[i].ss<<endl;
    
    double sum = 0;

    double ans = 0.0;
    for(int i=n;i>n-k;i--){
      double t = 2 * ppi * c[i].ff * c[i].ss;
      sum += t;
      pq.emplace(t);
    }
    
    ans = ppi * c[n-k+1].ff * c[n-k+1].ff + sum;

    for(int i=n-k;i>=1;i--){
      double lv = 2 * ppi * c[i].ff * c[i].ss;
      sum += lv;sum -= pq.top();
      pq.pop();
      pq.push(lv);
      double temp = ppi * c[i].ff * c[i].ff + sum;
      ans = max(ans,temp);
    }
    cout<<fixed<<setprecision(10)<<ans;

    while(!pq.empty())pq.pop();

    cout<<endl;
  }
  return 0;
}
