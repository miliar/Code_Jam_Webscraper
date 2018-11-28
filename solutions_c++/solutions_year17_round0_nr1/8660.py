#include <bits/stdc++.h>
using namespace std;

typedef pair<string, int> si;

int n, k, res, sz;
string s, target, aux;
set<string> visited;
string first, cnode;
si curr;

int main() {
  ios_base::sync_with_stdio(0); cin.tie(0);
  cin >> n;
  
  for (int cn=1; cn<=n; ++cn) {
    cin >> s >> k;
    res = -1;
    target = s;
    replace(target.begin(), target.end(), '-', '+');
    sz = s.length();
      
    queue<si> q;
    visited.clear();
    q.push(si(s,0));
      
    while (!q.empty()) {
      curr = q.front(); q.pop();
      cnode = curr.first;
      //cout << "current: " << cnode << endl;
      if (visited.count(cnode)) continue;
	
      visited.insert(cnode);

      if (cnode == target) {
	res = curr.second;
	break;
      }

      for (int i=0, j=k; j<=sz; ++i, ++j) {
	aux = cnode;
	for (int ii=i; ii<j; ++ii)
	  aux[ii] = ((aux[ii] == '+') ? '-' : '+');

	//cout << "next: " << aux << endl;
	  
	if (!visited.count(aux))
	  q.push(si(aux, curr.second+1));
      }
    }

    cout << "Case #" << cn << ": ";
    if (res == -1) cout << "IMPOSSIBLE";
    else cout << res;
    cout << "\n";      
  }
  return 0;
}
