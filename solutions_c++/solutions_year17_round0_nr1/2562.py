#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <climits>
#include <cstdio>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
#include <functional>
using namespace std;
#define db(a) (cout << (#a) << " = " << (a) << endl)
typedef long long ll;

unordered_set<string> visited;
ll K;

ll bfs(string s)
{  
  queue<string> q;
  q.push(s);
	ll erg = 0;
  while(!q.empty())
  {		
    size_t si = q.size();		
    for(size_t jj=0;jj<si;jj++)
    {
      string c = q.front(); q.pop();
			if(c.find_first_of('-') == string::npos) return erg;
      if(visited.count(c) > 0) continue;
      visited.insert(c);
      for(ll i=0;i<=ll(c.size())-K;i++)
			{
				string ns = c;
				bool good = false;
				for(ll j=0;j<K;j++)
				{
					if(ns[i+j] == '+') ns[i+j] = '-';
					else { ns[i+j] = '+'; good = true; }
				}
				if(good && visited.count(ns) <= 0)
				{
					//db(ns);
					q.push(ns);
				}
			}
    }
		erg++;
  }  
  return -1;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		string S;		
		cin>>S>>K;
		visited.clear();
//		ll erg = bfs(S);
		ll erg = 0;
		for(ll i=0;i<=ll(S.size())-K;++i)
		{
			if(S[i] == '+') continue;
			erg++;
			for(ll j=0;j<K;j++)
			{
				if(S[i+j] == '+') S[i+j] = '-';
				else S[i+j] = '+';
			}
		}
		if(S.find_first_of('-') != string::npos) erg = -1;
		if(erg >= 0) cout << "Case #" << t+1 << ": " << erg << "\n";
		else cout << "Case #" << t+1 << ": IMPOSSIBLE\n";
	}
  return 0;
}
