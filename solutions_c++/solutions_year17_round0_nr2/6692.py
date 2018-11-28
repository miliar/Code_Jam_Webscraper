#include <bits/stdc++.h>
using namespace std;



void test() {
	
	string N;
	cin >> N;
	
	bool chg = true;
	while (chg) {
		chg = false;
		
		for (int i = 1; i < N.size(); ++i) {
			if (N[i] < N[i-1]) {
				chg = true;
				
				for (int k = i; k<N.size(); ++k)
					N[k] = '9';
				N[i-1]--;
				if (N[0] == '0')
					N.erase(N.begin());
				
				break;
			}
		}
	}
	
	cout << N;
}

int main()
{
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		test();
		cout << endl;
	}
	return 0;
}
