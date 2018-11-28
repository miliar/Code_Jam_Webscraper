//g++ -std=c++14 -g -O2 -o ./a ./A.cpp
#include <bits/stdc++.h>
using namespace std;
#define ff first
#define ss second
#define nl '\n'
typedef long long ll;
//////////////////////////////////////////////////////////////////////

const int L = 20;
ll N;
int dig[L],n;
bool done[L][10][2];
ll dp[L][10][2],pw[L];
const ll INF = (ll)9e18;

ll f(int idx=1,int last=0,bool up=1){
  if(idx>n)return 0;
  if(done[idx][last][up])return dp[idx][last][up];
  done[idx][last][up]=true;
  
  ll ret = -INF;//
  
  for(int i=last;i<10;i++){
    if(up and i > dig[idx])continue;
    ret = max(ret , i*pw[idx] + f(idx+1,i,up and i==dig[idx]) );
  }
  
  return dp[idx][last][up]=ret;
}

void solve(){
  memset(done,0,sizeof done);
  cin>>N;
  n=0;
  for(ll x=N;x>0;x/=10)dig[++n] = x%10;
  reverse(dig+1,dig+n+1);
  pw[n]=1;
  for(int i=n-1;i>=1;i--)pw[i]=pw[i+1]*10ll;
  
  cout << f() ;
}

int main(){
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  
  int tc;cin>>tc;
  for(int tt=1;tt<=tc;tt++){
    cout<<"Case #"<<tt<<": ";
    solve();
    cout<<nl;
  }
  
  return 0;
}
