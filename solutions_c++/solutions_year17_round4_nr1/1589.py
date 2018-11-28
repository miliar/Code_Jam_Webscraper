#include <bits/stdc++.h>
using namespace std;
int main(){
	int t; cin >> t;
	int cs = 0;
	int N, P;
	while(t--){
		++cs;
		cin >> N >> P;
		int ans = 0;
		if(P == 2){
			int x = 0;
			for(int i=1; i<=N; ++i){
				int y; cin >> y;
				if(y & 1) ++x;
				else ++ans;
			}
			ans += (x >> 1);
			ans += (x & 1);
		}
		else if(P == 3){
			int x = 0, y = 0;
			for(int i=1; i<=N; ++i){
				int z; cin >> z;
				if(z % 3 == 0) ++ans;
				else if(z % 3 == 1) ++x;
				else ++y;
			}
			int k = min(x, y);
			ans = ans + k;
			x -= k;
			y -= k;
			if(x){
				ans = ans + (x / 3);
				if(x % 3) ++ans;
			}	
			else{
				ans = ans + (y / 3);
				if(y % 3) ++ans;
			}
		}
		else{

		}
		cout << "Case #" << cs << ": " << ans << endl;
	}
}