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

ll n,pos,id,t,temp,ans;
vll dig;
bool f;

void convert()
{
  
  while( n > 0){

    dig.pb(n % 10);
    n /= 10;

  }

  reverse(all(dig));

}

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(0);cout.tie(0);
  
  cin >> t;

  while(t--){

    dig.clear();
    ++id;
    cin >> n;
    temp = n;

    convert();

    pos = -1;

    for(ll i = 1;i < sz(dig); ++i){

      if(dig[i] < dig[i-1]){

	pos = i-1;
	break;
	
      }
    }

    f = false;

    while(pos > 0 && dig[pos-1] == dig[pos])
      --pos;
    
    for(ll i = pos;i + 1;--i){

      if(dig[i] > 1){

	f = false;
	--dig[i];
	break;

      }

      else{

	f = true;
	dig[i] = 9;

      }

    }

    ans = 0;
    
    for(ll i = ((f)?1:0);i <= pos;++i)
      ans = (ans * 10) + dig[i];

    for(ll i = pos+1;i < sz(dig);++i)
      ans = (ans * 10) + ((pos == -1) ? dig[i]:9);

    cout << "Case #" << id << ": " << ans << endl;

    
  }
  return 0;
}
