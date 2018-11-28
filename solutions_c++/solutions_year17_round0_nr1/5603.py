#include <iostream>
#include <vector>

using namespace std;

void solve(int test){
	string set; cin >> set;
	int k; cin >> k;
	
	vector<bool> pan(set.length());
	for(int i = 0; i < set.length(); i++){
		if(set[i] == '-')pan[i] = false;
		else pan[i] = true;
	}
	
	int ans = 0;
	for(int i = 0; i < pan.size(); i++){
		if(pan[i]) continue;
		
		ans++;
		for(int j = i; j < i+k; j++){
			if(j >= pan.size()){
				cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
				return;
			}
			pan[j] = !pan[j];
		}
	}
	
	cout << "Case #" << test << ": " << ans << endl;
	
	return;
}

int main(){
	int t; cin >> t;
	for(int i = 1; i <= t; i++) solve(i);
	return 0;
}
