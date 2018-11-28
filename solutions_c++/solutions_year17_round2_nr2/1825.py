#include <bits/stdc++.h>
using namespace std;

#define pb         push_back

typedef long long ll;
const ll INF = 1000000000000000000ll;
const ll MOD = 1000000007ll;
const double EPS = 1e-8;


int main(void) {
	//ios_base::sync_with_stdio(false);
	//cin.tie(0);
	string label = "ROYGBV";
	
	int test;
	cin >> test;

	for(int l=1; l<=test; l++){
		int n;
		cin >> n;

		vector<int> c;
		for(int i=0; i<6; i++){
			int t;
			cin >> t;
			c.pb(t);
		}

		string ans = "";
		int bef = -1;
		bool f = true;
		for(int i=0; i<n; i++){
			int select = -1;
			int num = 1;
			for(int j=0; j<6; j++){
				if(num <= c[j] && j != bef){
					num = c[j];
					select = j;
					if(i == n-2 && label[j] == ans[0]){
						break;
					}
				}

			}
			if(select == 1 || select == 3 || select == 5) puts("aaaaaaaaa");

			if(select == -1){
				f = false;
				break;
			}

			//cout << select << endl;
			bef = select;

			ans = ans + label[select];
			c[select]--;
		}

		if(f == false){
			printf("Case #%d: IMPOSSIBLE\n", l);
			continue;
		}
		//cout << ans.size() << endl;
		//cout << n << endl;

		for(int i=0; i<n-1; i++){
			//cout << ans[i] << ' ' << ans[i+1] << endl;
			if(ans[i] == ans[i+1]){
				f = false;
				break;
			}
		}
		if(ans[n-1] == ans[0]) f = false;

		if(f){
			printf("Case #%d: ", l);
			cout << ans << endl;
		}else{
			printf("Case #%d: IMPOSSIBLE\n", l);
		}
	}
	
	return 0;
}
