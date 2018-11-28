//g++ -std=c++14 -g -O2 -o ./a ./A.cpp
#include <bits/stdc++.h>
using namespace std;
#define ff first
#define ss second
#define nl '\n'
typedef long long ll;
//////////////////////////////////////////////////////////////////////



int main(){
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  int tc;cin>>tc;
  for(int tt=1;tt<=tc;tt++){
    ll n,k;cin>>n>>k;
    
    map<ll,ll> mp;
    mp[n]=1;

    ll ans;
    for(ll ops=k;ops>0;){
      ll len,cnt;
      tie(len,cnt) = *mp.rbegin();
      if(cnt >= ops){
	ans = len;break;	
      }else{
	mp.erase(--mp.end());
	ops -= cnt;
	ll lx = (len-1)/2;
	ll rx = len-1-lx;
	mp[lx]+=cnt;mp[rx]+=cnt;
      }
    }
    ll lS = (ans-1)/2;
    ll rS = ans-1 - lS;
    
    cout<<"Case #"<<tt<<": "<<rS<<' '<<lS<<nl;
  }

  return 0;
}
