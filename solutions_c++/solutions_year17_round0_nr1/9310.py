#include <bits/stdc++.h>

using namespace std;

string s;
int k, t;

int main () {
	ios_base::sync_with_stdio(0);
	cin >> t;
	
	for(int j = 1; j <= t; j++){
		cin >> s >> k;
		int ans = 0;
		int op = 0;

		for(int i = 0; i <= int(s.size())-k; i++){
			if(s[i] == '-'){
				for(int ii = i; ii < i+k; ii++){
					if(s[ii] == '-')
						s[ii] = '+';
					else
						s[ii] = '-';
				}
				ans++;
				//cout << s << endl;
			}
		}	
		for(int i = 0; i < s.size(); i++){
			if(s[i] == '-') ans = -1;
		}
		printf("Case #%d: ",j);
		if(ans == -1){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("%d\n",ans);
		}
	}

	return 0;
}