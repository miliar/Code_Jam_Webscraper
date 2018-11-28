#include <bits/stdc++.h>

using namespace std;

int main(){

	int t;

	cin >> t;
	long long n;
	for(int i = 0; i < t; ++i){
		cin >> n;
		
		for(long long j = n; j >= 1; j--){
			string aux = to_string(j);
			int ok = 0;
			for(int k = 0; k < aux.length(); k++){
				
				if(aux[k] <= aux[k + 1]){
					ok++;
				}else{
					break;
				}
				
			}

			if(ok >= aux.size() - 1){
					cout << "Case #" << i + 1 << ": " << j << endl; 
					break;
			}

			ok = 0;
		}

	}

	return 0;
}