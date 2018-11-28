#include <iostream>
#include <fstream>
#include <stdio.h>

#include <string>
#include <map>


using namespace std;

int main() {
	int t; 
	cin >> t;
	for (int i0=1;i0<=t;++i0) {
		cout << "Case #" << i0 << ": ";
		string s;
		int k;
		cin >> s >> k;

		int n = s.size();
		int ans = 0;
		//cout << s << endl;

		for (int i = 0; i <= n-k; ++i) {
			if (s[i] == '-') {
				ans++;
				for (int j=i;j<i+k;++j) {
					if (s[j] == '+') 
						s[j] = '-';
					else s[j] = '+';	
				};			
			};
			//cout << i << " " << k << " " << s << endl;
		};

		//cout << s << endl;
		bool flag = true;
		for (int i=0;i<n;++i)
			if (s[i] == '-') {
				flag = false;
				break;
			};



		if (flag)
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE" << endl;

	}	
}