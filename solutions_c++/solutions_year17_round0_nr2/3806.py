#include <bits/stdc++.h>
using namespace std;

char s[100];

int main(){
	int T;
	
	scanf(" %d", &T);
	
	for (int k = 0; k < T; k++){
		scanf(" %s", s);
		
		int l = strlen(s);
		bool t = true;
		for (int i = 1; i < l; i++){
			if (s[i] < s[i - 1]){
				t = false;
				break;
			}
		}

		if (t){
			printf("Case #%d: %s\n", k + 1, s);
			continue;
		}
		
		int same = 0, first = 0, change = 0;
		for (int i = 1; i < l; i++){
			if (s[i] < s[i - 1]){
				if (first == 0){
					change = i - 1;
					same = -1;
				}
				else{
					change = i - 1;
				}
				break;
			}
			if (s[i] == s[i - 1] && first == 0){
				same = i - 1;
				first = 1;
				change = i;
			}
			if (s[i] > s[i - 1]){
				change = i;
				first = 0;
			}
		}

		if (same == -1){
			for (int i = change; i < l; i++){
				if (i == change)
					s[i] = s[i] - 1;
				else
					s[i] = '9';
			}
		}
		else{
			for (int i = same; i < l; i++){
				if (i == same)
					s[i] = s[i] - 1;
				else
					s[i] = '9';
			}
		}

		int st = 0;
		for (int i = 0; i < l; i++){
			if (s[i] != '0'){
				st = i;
				break;
			}
		}

		printf("Case #%d: ", k + 1);
		for (int i = st; i < l; i++)
			printf("%c", s[i]);
		printf("\n");

	}

	return 0;
}
