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

ll k,ans,t,id;
bool f;
string s;
int main()
{
  ios::sync_with_stdio(false);
  cin.tie(0);cout.tie(0);
  
  cin >> t;

  while(t --){

    ++id;

    cin >> s >> k;

    for(int i = 0;i < s.length()-k+1; ++i){

      if(s[i] == '-'){

	++ans;
	s[i] = '+';

	for(int j = i+1;j < i + k;++j)

	  s[j] = (s[j] == '+') ? '-' : '+';

      }

    }

    f = false;
    
    for(int i = s.length()-k+1;i < s.length(); ++i){

      if(s[i] == '-'){

	f = true;
	break;

      }

    }

    cout << "Case #" << id << ": ";
    
    if(f)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << ans << endl;

    ans = 0;

  }
      
  return 0;
}
