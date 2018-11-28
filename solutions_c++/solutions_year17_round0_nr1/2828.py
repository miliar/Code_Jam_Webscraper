#include <bits/stdc++.h>
using namespace std;

int t, k, n;
bool v[1005];

int main(){
	string s;
	cin >> t;
	for(int caso=1; caso<=t; caso++){
		
		cin >> s;
		int l = s.size();		
		for(int i=0; i<l; i++){
			if(s[i]=='-') v[i] = 1;
			else v[i] = 0;
		}
		
		cin >> k;	

		int R = 0;
		for(int i = 0; i+k <= l; i++)
			if(v[i]){
				for(int j = 0; j < k; j++)
					v[i+j] = 1-v[i+j];
				R++;
			}

		bool ok = true;
		for(int i = 0; i < l; i++){
			if(v[i]==1){
				ok = false;
				break;
			}
		}

		if(ok) printf("Case #%d: %d\n", caso, R);
		else printf("Case #%d: IMPOSSIBLE\n",caso);
	}

	return 0;
}
