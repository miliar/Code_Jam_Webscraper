#include <iostream>

using namespace std;

string ans(string n){
	bool cambio = true;
	while(cambio){
		cambio = false;
		for(size_t i = 0; i < n.size() - 1; i++){
			if(n[i] > n[i + 1]){
				n[i]--;
				for(size_t j = i + 1; j < n.size(); j++){
					n[j] = '9';
				}
				while(n[0] == '0'){
					n = n.substr(1, string::npos);
				}
				cambio = true;
				break;
			}
		}
	}
	return n;
}

int main(){
	int t;
	string n;
	cin >> t;
	for(int i = 1; i <= t; i++){
		cin >> n;
		cout << "Case #" << i << ": " << ans(n) << "\n";
	}
	return 0;
}