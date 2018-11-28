#include<iostream>
#include<cstdlib>
#include<string>

using namespace std;

bool checkTidy(long long value) {
	string str = to_string(value);
	for(int i=0; i<str.length()-1; ++i) 
		if(str[i] > str[i+1])
			return false;
	return true;
}

int main() {
	int test;
	cin >> test;
	for(int t=1; t<=test; ++t) {
		long long upbound;
		cin >> upbound;
		long long ans = upbound;
		while(checkTidy(ans) == false) {
			ans -= 1;
		}
		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}
