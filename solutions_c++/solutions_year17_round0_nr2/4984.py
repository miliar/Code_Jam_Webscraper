#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll gen(string num){
	ll ans = 0;
	for (int i = 0;i < (int)num.size();i++){
		ans *= 10LL;
		ans += (num[i] - '0');
	}
	return ans;
}

int main(){
	freopen("input.in","r",stdin);
	freopen("output-p474.out","w+",stdout);
	int T; cin >> T;
	for (int cs = 1;cs <= T;cs++){
		string num; cin >> num;
		int n = num.size();
		int last = -1;
		ll sol = -1;
		//cout << "num = " << num << '\n';

		for (int d = 0;d < n;d++){
			//printf("%d \n",d);

			int act = num[d] - '0';
			//cout << "act = " << act << '\n';
			if (act < last){ 
				break; // not legal 
			}
			if (act-1 >= last){
				/// solucion con act-1 y 99999
				string test = num;
				test[d] --;
				for (int j = d+1;j < n;j++){
					test[j] = '9';
				}
				//cout << " candidate: "<<gen(test) << '\n';
				sol = max(sol , gen(test));
			}
			if (d == n-1 && act >= last){
				sol = max(sol , gen(num));
			}

			last = act;
		}

		printf("Case #%d: %lld\n",cs,sol);


	}
}