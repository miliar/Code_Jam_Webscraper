#include<bits/stdc++.h>

using namespace std;

int main(){
	int n, t, flip;
	string s;
	scanf("%d", &t);
	for (int c = 1; c <= t; c++) {
		flip = 0;
		cin >> s >> n;
		int l = s.size();
		for (int i = 0; i < l - n + 1; i++) {
			if (s[i] == '-') {
				flip++;
				for (int j = 0; j < n; j++) {
					if (s[i + j] == '-') {
						s[i + j] = '+';
					} else {
						s[i + j] = '-';
					}
				}
				//cout << s << endl;
			}
		}
		int happy = 0; 
		for (int i = 0; i < l; i++) {
			if (s[i] == '+') {
				happy++;
			}
		} 		
		printf("Case #%d: ", c);
		if (happy == l) {
			printf("%d", flip);
		} else {
			printf("IMPOSSIBLE");
		}
		printf("\n");
	}	
	return 0;
}
