#include <bits/stdc++.h>
using namespace std;
int main() {
	 ios::sync_with_stdio(0);
	 cout << fixed << setprecision(10);
	
	 int t =0;
	 cin >> t;
	 for(int i=0;i<t;++i) {
		  double d=0;
		  int n=0;
		  cin >> d >> n;
		  vector<pair<int,int>>v(n);
		  for(auto&p:v) cin >> p.first >> p.second;
		  sort(v.rbegin(),v.rend());
		  double k,s,max_t = 0;
		  for (int j=0;j<n;++j) {
				tie(k,s)=v[j];
				double len=d-k;
				if (len/s > max_t) {
					 max_t = len/s;
				}
		  }
		  cout << "Case #" << i + 1 << ": " << d/max_t << endl;
	 }
	return 0;
}