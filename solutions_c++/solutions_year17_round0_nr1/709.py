#include<bits/stdc++.h>
using namespace std;
int main(){
	int T;
	cin >> T;
	for(int l = 1; l <= T; l++){
		string s;
		int k;
		cin >> s >> k;
		int cont = 0;
		int t = s.size();
		for(int i = 0; i + k - 1 < t; i++){
			if(s[i] == '-'){
				cont++;
				for(int j = i; j < i+k; j++)
					s[j] = (s[j] == '+') ? '-' : '+';
			}
		}
		int flag = 1;
		for(int i = 0; i < t; i++)
			if(s[i] == '-')
				flag = 0;
		cout << "Case #" << l << ": ";
		if(flag)
			cout << cont << "\n";
		else cout << "IMPOSSIBLE" << endl;


	}

	return 0;
}