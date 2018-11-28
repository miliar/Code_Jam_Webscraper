#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <iomanip>

using namespace std;

int main(){
	int q;
	cin >> q;
	for (int z = 0; z < q; z++){
		string s;
		cin >> s;
		int k;
		cin >> k;
		int ans = 0;
		for (int i = 0; i < s.size(); i++){
			if (s[i] == '-'){
				if (i <= s.size() - k){
					ans++;
					for (int j = 0; j < k; j++){
						if (s[i+j] == '+'){
							s[i+j] = '-';
 						} else {
							s[i+j] = '+';
						}
					}
				} else {
					ans = -1;
					break;
				}
			}
		}
		if (ans == -1){
			cout << "Case #" << z+1 << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << z+1 << ": " << ans << endl;
		}
	}
}