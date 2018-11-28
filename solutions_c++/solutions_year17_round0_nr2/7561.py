#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin >> t;
	string n;
	for(int x = 1; x <= t; x++){
		cin >> n;
		int z = n.length()-1;
		for(int j = z-1; j >= 0; j--){
			if(n[j] > n[j+1]){
				n[j]--;
				while(z > j){
					n[z] = '9';
					z--;
				}
			}
		}
		if(n[0] == '0'){
			n = n.substr(1);
		}
		cout << "Case #" << x << ": " << n << endl; 
	}
	return 0;
}