#include <bits/stdc++.h>

#define ll long long

using namespace std;

pair<ll,ll> arr[1010];
bool yes[1005];

int main() {
	ios::sync_with_stdio(false);
	int test;
	cin >> test;
	cout.setf(ios::fixed,ios::floatfield);
	cout.precision(9);
	for(int ctr=1;ctr<=test;ctr++) {
		int n,k;
		cin >> n >> k;
		for(int i=0;i<n;i++) cin >> arr[i].first >> arr[i].second;
		sort(arr,arr+n,greater<pair<ll,ll> >());
		if(n==k) {
			double res = M_PI*arr[0].first*(2*arr[0].second+arr[0].first);;
			for(int i=1;i<n;i++) res += 2*M_PI*arr[i].first*arr[i].second;
			cout << "Case #" << ctr << ": " << res << "\n";
		}
		else {
			double maxVal = 0.00;
			for(int i=0;i<n;i++) {
				double base = M_PI*arr[i].first*(2*(arr[i].second)+arr[i].first);
				double otherVal = 0.00;
				for(int j=i+1;j<n;j++) { 
					otherVal += 2*M_PI*(arr[j].first*arr[j].second); 
					yes[j] = true;
				}
				for(int l=0;l<(n-i-k);l++) {
					double minVal = DBL_MAX;
					int index = i;
					for(int j=i+1;j<n;j++) {
						if(yes[j]) {
							minVal = min(minVal,2*M_PI*(arr[j].first*arr[j].second));
							if(minVal==2*M_PI*(arr[j].first*arr[j].second)) index = j;
						}
					}
					yes[index] = false;
					otherVal -= minVal;
				}
				maxVal = max(maxVal,base+otherVal);
			}		
			cout << "Case #" << ctr << ": " << maxVal << "\n";
		}
	}
	return 0;
}