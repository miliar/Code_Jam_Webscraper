#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cmath>
using namespace std;

typedef long long LL;

bool mycomp(pair<LL,LL> a, pair<LL,LL> b) {
	return a.first * a.second < b.first*b.second;
}

int main() {
	
	int test;
	cin>>test;
	
	for (int testc = 1; testc<=test; testc++) {
		double mxs = 0;
		int n,k;
		cin>>n>>k;
		vector<pair<LL,LL> > t; 
		t.resize(n);
		for (int i = 0; i < n; i++) {
			LL xx, xy;
			scanf("%lld %lld", &xx, &xy);
			t[i] = make_pair(xx, xy); 
		}
		sort(t.begin(), t.end());
		reverse(t.begin(), t.end());
		
		
		vector< pair<LL,LL> > up;
		for (int i = 0; i < n; i++) {
			double s = (double)t[i].first * (double)t[i].first * acos(-1);
			s += 2.0 * acos(-1) * (double)t[i].first * (double)t[i].second;
			// start with i
			up = vector< pair<LL,LL> >(t.begin()+i+1, t.end());
			sort(up.begin(), up.end(), mycomp);
			reverse(up.begin(), up.end());
			//cout<<i<<endl;
			/*for (unsigned j = 0; j < up.size(); j++) {
				cout << up[j].first << " " << up[j].second << endl;
			}*/
			
			if (up.size() < k-1)
				break;
			for (int j = 0; j < k-1; j++) {
				s += 2.0*acos(-1)*(double)up[j].first*(double)up[j].second;
			}
			//cout<<i<<" "<<s<<endl;
			if (s > mxs)
				mxs = s;
		}
		
		
		printf("Case #%d: %.9f\n", testc, mxs);
	}
	return 0;
}


