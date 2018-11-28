#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <string>
#include <cstring>

using namespace std;
string get(int r,int o,int y,int g,int b,int v){
	string ans = "";
	if(o > 0){
		if(b < 2)
			return "IMPOSSIBLE";
		ans = "BOB";
		b-=2, o--;
	}

	while(o > 0){
		if(b > 0)
			ans += "OB", b--, o--;
		else{
			int len = ans.length();
			if(len > 0 && ans[len-1] == 'O')
				return "IMPOSSIBLE";
			ans += "O", o--;
		}
	}

	while(b+r+y>0){
		int len = ans.length();
		if(len > 0 && ans[len-1] == 'O')
			return "IMPOSSIBLE";

		if(len > 0 && ans[len-1] == 'B'){
			if(r >= y && r > 0){
				ans += "R", r--;
			}
			else if(y > r && y > 0){
				ans += "Y", y--;
			}
			else
				return "IMPOSSIBLE";
		}

		else if(len > 0 && ans[len-1] == 'Y'){
			if(b >= r && b > 0){
				ans += "B", b--;
			}
			else if(b < r && r > 0){
				ans += "R", r--;
			}
			else
				return "IMPOSSIBLE";
		}

		else if(len > 0 && ans[len-1] == 'R'){
			if(b >= y && b > 0){
				ans += "B", b--;
			}
			else if(b < y && y > 0){
				ans += "Y", y--;
			}
			else
				return "IMPOSSIBLE";
		}

		else if(len == 0){
			if(b >= y && b >= r)
				ans += "B", b--;
			else if(y <= r && r >= b){
				ans += "R", r--;
			}
			else if( y>= b && y >= r){
				ans += "Y", y--;
			}
		}
		// cout << ans << endl;
	}
	int len = ans.length();
	if(len > 0 && ans[len-1] == ans[0]){
		if(len >= 3){
			if(ans[len-1] == ans[len-3])
				return "IMPOSSIBLE ";
			swap(ans[len-1], ans[len-2]);
		}
		if(len > 0 && ans[len-1] == ans[0])
			return "IMPOSSIBLE ";
	}
	return ans;
}
int main(){
	int T;
	cin >> T;
	for(int _t = 1; _t <= T; _t++){
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y>> g >> b >> v;
		printf("Case #%d: %s\n", _t, get(r, o, y, g, b, v).c_str());
	}
	return 0;
}