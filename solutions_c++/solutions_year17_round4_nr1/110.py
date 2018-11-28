#include <bits/stdc++.h>
using namespace std;

void doCase(int t) {
	int N, P;
	cin >> N >> P;
	
	vector<int> G(N);
	for (int i=0; i<N; i++) {
		cin >> G[i];
	}
	
	cout << "Case #" << t << ": ";
	switch(P) {
	case 2: {
		int e = 0, o = 0;
		for (int i=0; i<N; i++) {
			if (G[i] % 2 == 0)
				e++;
			else
				o++;
		}
		cout << e + ((o+1)/2) << endl;
		break;
		}
	case 3: {
		int e = 0, a = 0, b = 0;
		for (int i=0; i<N; i++) {
			if (G[i] % 3 == 0)
				e++;
			else if (G[i] % 3 == 1)
				a++;
			else
				b++;
		}
		
		cout << e + min(a,b)+(max(a,b)-min(a,b)+2)/3 << endl;
		break;
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
		doCase(i+1);
	return 0;
}
