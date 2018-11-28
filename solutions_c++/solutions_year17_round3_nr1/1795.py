#include <bits/stdc++.h>

using namespace std;
vector< pair<double,double> > v;

int main() {
	int t,n,k;
	double r,h;
	cin >> t;
	int tt=1;
	while (t--) {
		v.clear();
		cin >> n >> k;
		for (int i = 0; i < n; i++) {
			cin >> r >> h;
			v.push_back(make_pair(r,h));
		}
		sort(v.rbegin(), v.rend());
		double answer = 0;
	  for (int kk = 0; kk < n; kk++) {
  		multiset<double> s;
  		double ans = acos(-1)*v[kk].first*v[kk].first+2*acos(-1)*v[kk].first*v[kk].second;
  		double tmp=ans;
  		int j = 2;
  		for (int i = 0; i < n; i++) {
  		  if (i<=kk) continue;
  			ans = 2 * acos(-1)*v[i].first*v[i].second;
  			if (j == k+1 && s.size() > 0) {
  				multiset<double>::iterator k = s.end();
  				k--;
  				if (*k < ans) {
  					s.erase(k);
  					s.insert(ans);
  				}
  				j--;
  			} else if (j!=k+1) {
  				s.insert(ans);
  			}
  			j++;
  		}
  		double tot = 0;
  		
  		for (multiset<double>::iterator i = s.begin(); i != s.end(); i++) {
  			tot += *i;
  		}
  		if (j==k)
      		answer = max(answer, tot+tmp);
	  }
		printf("Case #%d: %.6f\n", tt++, answer);
	}	
}