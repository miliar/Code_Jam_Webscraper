#include<bits/stdc++.h>
#define endl '\n'
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);cin.tie(0);
	int n;
	cin >> n;
	for (int k = 1; k < n + 1; k++){
		long long a, b;
		cin >> a;
		for (long long i = a; i > -1; i-- ){
			stringstream ss;
			string s;
			ss << i;
			s = ss.str();
			sort(s.begin(),s.end());
			b = stoll(s);
			if (i == b) break;
		}
		cout << "Case #" << k << ": " << b << endl;
	}
	return 0;	
}