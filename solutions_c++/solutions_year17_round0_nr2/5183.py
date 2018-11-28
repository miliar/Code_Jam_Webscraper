#include <bits/stdc++.h>
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define INF 0x3f3f3f3f
#define LINF 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int main(){
	int T;
	cin >> T;
	for(int caso = 1; caso <= T; caso++){
		string n, ans;
		cin >> n;
		ans = n;
		bool flag = true;
		while(flag){
			flag = false;
			for(int i = 0; i < ans.size() - 1; i++){
				if(ans[i] > ans[i+1]){
					flag = true;
					ans[i]--;
					ans[i+1] += 10;
				}
			}
			for(int i = ans.size() -1; i > 0; i--){
				if(ans[i] < ans[i-1]){
					flag = true;
					ans[i-1]--;
					ans[i] += 10;
				}
			}
		}
		for(int i = 0; i < ans.size(); i++){
			ans[i] = max('0',ans[i]);
			ans[i] = min('9',ans[i]);
		}
		if(ans[0] <= '0') ans.erase(0,1);
		printf("Case #%d: ",caso);
		cout << ans << endl;
	}
	return 0;
}
