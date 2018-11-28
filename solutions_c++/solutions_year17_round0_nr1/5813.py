#include<iostream>

using namespace std;

void solve() {
	string pattern;
	int l;
	cin >> pattern >> l;
	int n = pattern.size();

	int count = 0;
	for(int i=0;i<n-l+1;i++){
		bool ok = true;
		for(int j=i;j<n;j++){
			if(pattern[j] == '-'){
				ok = false;
			}
		}
		if(ok) break;

		if(pattern[i] == '-'){
			count++;
			for(int j=0;j<l;j++){
				pattern[i+j] = pattern[i+j] == '+' ? '-' : '+';
			}
		}
	}

	bool ok = true;
	for(int j=0;j<n;j++){
		if(pattern[j] == '-'){
			ok = false;
		}
	}
	if(ok) {
		cout << count;
	}else{
		cout << "IMPOSSIBLE";
	}


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
