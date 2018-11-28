#include <bits/stdc++.h>

using namespace std;

int Test, len;
char s[110];

bool work(){
	len = strlen(s);
	bool flag = 0;
	for (int i = 0; i + 1 < len; i++)
		if (s[i] > s[i + 1]){
			flag = 1;
			s[i] = s[i] - 1;
			for (int j = i; j > 0 && s[j] < '0'; j--){
				s[j] = '9';
				s[j - 1]--;
			}
			for (int j = i + 1; j < len; j++)
				s[j] = '9';
			break;
		}
	if (s[0] == '0'){
		flag = 1;
		for (int i = 0; i < len; i++)
			s[i] = s[i + 1];
	}
	return flag;
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &Test);
	for (int tt = 1; tt <= Test; tt++){
		scanf("%s", s);
		while (work());
		printf("Case #%d: ", tt);
		printf("%s\n", s);
	}
}