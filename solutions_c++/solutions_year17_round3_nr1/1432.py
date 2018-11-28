#include <bits/stdc++.h>

using namespace std;
const double pi = 3.14159265359;

void solve() {
	int n,k;
	cin >> n >> k;
	vector<pair<double,double> > v(n);
	for(int i = 0;i < n; i++){
		cin >> v[i].first >> v[i].second;
	}
	sort(v.rbegin(), v.rend());

	double ans = 0;
	for(int i = 0;i + k - 1 < n; i++){
		vector<double> temp;
		double t1 = 0;
		t1 = v[i].first*v[i].first;
		t1 += 2 * v[i].first * v[i].second;
		for(int j = i+1;j < n; j++){
			temp.push_back(v[j].first*v[j].second);
		}
		sort(temp.rbegin(), temp.rend());
		for(int j = 0;j < k-1; j++){
			t1 += 2*temp[j];
		}
		ans = max(ans,t1);
	}
	printf("%0.12lf\n",ans*pi );
}

int main() {
	assert(freopen("input.txt","r",stdin));
	assert(freopen("output.txt","w",stdout));
	int t; cin>>t;
	for(int i = 1;i <= t;i++) {
		cerr<<"Executing Case #"<<i<<endl;
		cout<<"Case #"<<i<<": ";
		solve();
	}

}
