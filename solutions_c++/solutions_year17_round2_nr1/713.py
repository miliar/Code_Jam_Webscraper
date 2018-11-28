#include<bits/stdc++.h>
using namespace std;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for(int I = 1; I <= T; ++I){
		cout << "Case #" << I  << ": ";
		int n;
		double d;
		double t = 0;
		cin >> d >> n;
		while(n--) {
			int x,y;
			cin >> x >> y;
			t = max(t, (d-x)/y);
		}
		cout.setf(ios::fixed);
		cout.precision(10);
		cout << d/t << endl;


	}

}
