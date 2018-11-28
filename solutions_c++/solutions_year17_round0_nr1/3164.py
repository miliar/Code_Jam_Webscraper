#include <bits/stdc++.h>
using namespace std;
int main (){
	ios_base::sync_with_stdio(0);
	int z;
	cin >> z;
	for (int cassse = 1; cassse <= z; ++cassse){
		string a;
		cin >> a;
		int b;
		cin >> b;
		int n = a.length();
		vector <int> v(n, 0);
		bool q = 1;
		int odp = 0;
		int akt = 0;
		for (int i = 0; i < n; ++i){
			int c = 0;
			if (a[i] == '+') c = 1;
			c += akt;
			akt += v[i];
			c %= 2;			
			if (!c){
				++odp;
				if(i + b - 1>= n){
					q = 0;
					break;
				}
				else {
					v[i+b-1] += 1;
					++akt;
				}
			}
		}
		cout << "Case #" << cassse <<": ";
		if(q){
			cout << odp << '\n';
		}
		else {
			cout <<"IMPOSSIBLE\n";	
		}
	}
}
