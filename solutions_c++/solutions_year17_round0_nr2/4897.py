#include<bits/stdc++.h>
using namespace std;
int main() {
	int t;
	cin>>t;
	int casenum = 0, ans;
	while(t--) {
		casenum++;
		long long int num;
		cin>>num;
		vector<int> v;
		while(num > 0) {
			v.push_back(num % 10);
			num /= 10;
		}
		reverse(v.begin(), v.end());
		for(int i = v.size() - 1; i >= 1; i--) {
			if(v[i] < v[i-1]) {
				v[i-1]--;
				for(int j = i; j < v.size(); j++) {
					v[j] = 9;
				}
			}
		}
		long long int ans = 0;
		for(int i = 0; i < v.size(); i++) {
			ans = 10*ans + v[i];
		}
		cout<<"Case #"<<casenum<<": "<<ans<<endl;
	}
}
