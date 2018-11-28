#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
typedef unsigned long long ll;
int main(){
	ll t;
	cin >> t;
	for(ll c = 1; c <= t; c++){
		string s;
		int k = 0,ans = 0;
		cin >> s >> k;
		vector<bool> flips(s.length());
		for(int i = 0; i < s.length(); i++){
			if(s[i] == '-')flips[i] = 0;
			else flips[i] = 1;
		}
		for(int i = 0; i < flips.size()-k+1; i++){
			if(flips[i] == 0){
				ans++;
				for(int j = i; j < i+k; j++){
					flips[j]  = (!flips[j]);
				}
			}
		}
		bool contains_unflipped = false;
		for(int i = 0; i < flips.size(); i++){
			if(flips[i] == 0)contains_unflipped = true;
		}
		if(contains_unflipped)cout << "Case #" << c << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << c << ": " << ans << endl;
	}
}