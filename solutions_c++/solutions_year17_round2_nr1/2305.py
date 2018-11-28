//g++ -std=c++14 -g -O2 -o ./a ./A.cpp
#include <bits/stdc++.h>
using namespace std;
#define ff first
#define ss second
#define nl '\n'
typedef long long ll;
//////////////////////////////////////////////////////////////////////

const int N = 1010;
ll d,n,k[N],s[N];
double t[N];

int main(){
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  int __tc;cin>>__tc;
  for(int __tt=1;__tt<=__tc;__tt++){
    cout<<"Case #"<<__tt<<": ";

    cin>>d>>n;
    for(int i=1;i<=n;i++){
      cin>>k[i]>>s[i];
      t[i] = ((double)(d-k[i]))/((double)s[i]);
    }

    double T = *max_element(1+t,1+t+n);
    double S = ((double)d) / T;
    cout<<fixed<<setprecision(6)<<S;
    
    cout<<nl;
  }
  return 0;
}
