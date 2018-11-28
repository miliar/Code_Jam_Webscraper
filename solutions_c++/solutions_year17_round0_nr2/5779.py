#include<bits/stdc++.h>

using namespace std;

typedef long long int ll;

void solve() {
	string num;
	cin >> num;
	int n = num.size();

	for(int i=0;i<n;i++){
		bool hasless = false;
		for(int j=i;j<n;j++){
			if(num[j] < num[i]){
				hasless = true;
				break;
			}else if(num[j] > num[i]) {
				break;
			}
		}

		if(hasless){
			num[i]--;
			for(int j=i+1;j<n;j++){
				num[j] = '9';
			}
			break;
		}
	}

	stringstream ss;
	ll res;
	ss << num;
	ss >> res;
	cout << res;
}

int main() {
	int n;
	cin >> n;

	for(int i=0;i<n;i++){
		cout << "Case #" << i+1 << ": ";
		solve();
		cout << endl;
	}

	return 0;
}
