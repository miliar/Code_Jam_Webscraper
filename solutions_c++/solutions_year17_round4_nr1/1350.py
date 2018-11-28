#include <bits/stdc++.h>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int testCase = 1; testCase <= T; testCase++){
		cout << "Case #" << testCase << ": ";
		int N, P;
		cin >> N; cin >> P;
		vector <int> C(4, 0);
		for(int i = 0; i < N; i++){
			int g;
			cin >> g;
			C[g % P]++;
		}
		if(P == 2) cout << C[0] + (C[1] + 1) / 2;
		else if(P == 3){
			int m = min(C[1], C[2]);
			int r = max(C[1], C[2]) - m;
			cout << C[0] + m + (r + 2) / 3;
		}
		else{
			int m = min(C[1], C[3]);
			int r = max(C[1], C[3]) - m;
			int a = C[0] + m + C[2] / 2;
			if(C[2] % 2 && r >= 2){
				a++;
				r -= 2;
				C[2]--;
			}
			a += r / 4;
			if(C[2] % 2 || r % 4) a++; 
			cout << a;
		}
		cout << endl;
	}
  return 0;
}
