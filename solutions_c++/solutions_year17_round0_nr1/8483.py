#include<iostream>
#include<queue>
#include<vector>
#include<cmath>
#include<string>
using namespace std;

int main(){
	int t, k;
	string s;
	cin >> t;
	for(int z = 1; z <=t; ++ z){
		cin >> s >> k;
		int ret = 0;
		for (int i = 0; i < s.size(); ++ i){
			if (s[i] == '-'){	
				if (i + k >	 s.size()){
					ret = -1; break;
				}
				ret ++;
				for (int j = 1; j < k; ++ j) s[i+j] = (s[i+j] == '+')? '-' : '+';
			}
		}
		cout << "Case #" << z << ": ";
		if (ret == -1) cout << "IMPOSSIBLE" << endl;
		else cout << ret << endl;
	}
	return 0;
}