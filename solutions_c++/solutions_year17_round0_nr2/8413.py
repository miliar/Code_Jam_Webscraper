#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool non_descending(long long int);

int main() {
	int t;
	long long int n;

	cin >> t;

	for (int i=0; i<t; i++) {
		cin >> n;

		long long int ans;

		for (long long int j=n; j>=1; j--) {
			if (non_descending(j)) {
				ans = j;
				break;
			}
		}

		cout << "Case #"<< i+1 << ": "<< ans << endl;
	}

	return 0;
}

bool non_descending(long long int num) {
	string n = to_string(num);
	bool asc = true;
	for(int i=0; i<n.length()-1; i++) {
		if(n[i] > n[i+1]){
			asc = false;
			break;
		}
	}
	return asc;
}