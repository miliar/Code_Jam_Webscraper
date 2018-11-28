#include <bits/stdc++.h>

#define pb push_back
#define all(a) a.begin(),a.end()
#define allr(a) a.rbegin(),a.rend()
#define fr first
#define se second
#define mp make_pair
#define sz(a) ll((a).size())
#define memo(a,b) memset(a,b,sizeof(a))
#define MAX 100001
#define INF 1e18+1

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;
typedef vector<ll> vll;
typedef vector<pll> vpll;

ll t,n,k,l,r,ans1,ans2,id,height,val,cnt;
string s;
map<ll,ll> ma,temp;
int main()
{
  ios::sync_with_stdio(false);
  cin.tie(0);cout.tie(0);
  
  cin >> t;

  while(t --){

    ++id;

    cin >> n >> k;

    height = 63 - __builtin_clzll(k);

    k = k - (1ll << height) + 1;

    ma[n] = 1;

    for(ll i = 1;i <= height; ++i){

      for(auto it : ma){

	temp[it.fr / 2] += it.se;
	temp[it.fr - (it.fr/2) - 1] += it.se;

      }

      ma.clear();

      for(auto it : temp)
	ma[it.fr] = it.se;

      temp.clear();

    }

    for(auto it : ma){
      val = it.fr;
      cnt = it.se;
    }

    if(cnt < k){
      val = ma.begin()->fr;
    }

    //cout << val << " " << cnt << endl;

    ans1 = val/2;
    ans2 = val - ans1 - 1;
    
    cout<< "Case #" << id << ": " << ans1 << " " << ans2 <<endl;

    ma.clear();

  }

    
  return 0;
}
