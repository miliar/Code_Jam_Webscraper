#include <bits/stdc++.h>
using namespace std;
#define int long long
main (){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int z;
	cin >> z;
	for (int cassse = 1; cassse <= z; ++cassse){
		cout << "Case #" << cassse <<": ";
		string a;
		cin >> a;
		int n = a.length();
		int change = -1;
		for (int i = 0; i < n-1; ++i){
			if(a[i] > a[i+1]){
				change = i;
				break;
			}
		}
		if (change >= 0){
			int change2 = 0;
			for (int i = change; i >= 0; --i){
				if (a[i] != '0'){
					a[i] = a[i]-1;
				}
				change2 = i+1;
				if(i>0)if(a[i-1] <= a[i])break;
			}
			for (int i = change2; i < n; ++i){
				a[i] = '9';
			}
		}
		if(a[0] != '0')cout << a << '\n';
		else {
			for (int i = 1; i <n; ++i){
				cout << a[i];
			}
			cout << '\n';
		}
	}
}
