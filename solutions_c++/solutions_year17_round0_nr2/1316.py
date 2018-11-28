#include <bits/stdc++.h>
#define SZ(v) ((int)(v).size())

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

int main(){
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++){
		ll res = 0;
		char s[20];
		scanf("%s", s);
		bool nine = false;
		int n = (int) strlen(s);
		for (int i=0; i<n; i++){
			if (!nine){
				if (i == 0) res = s[i] & 15;
				else {
					if (s[i-1] > s[i]){
						res = 0;
						bool first = true;
						for (int ii=0; ii<i; ii++){
							if (s[ii] == s[i-1]){
								if (first){
									res = res * 10 + ((s[i-1]&15)-1);
									first = false;
								}
								else res = res * 10 + 9;
							}
							else
								res = res * 10 + (s[ii]&15);
						}
						res = 10 * res + 9;
						nine = true;
					}
					else res = 10 * res + (s[i] & 15);
				}
			}
			else res = res * 10 + 9;
		}
		printf("Case #%d: %lld\n", t, res);
	}
	return 0;
}