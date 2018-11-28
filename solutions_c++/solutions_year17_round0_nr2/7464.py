#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

char* find_ans(char str[]) {
	int len = strlen(str);
	for(int i=0;i<len-1;i++) {
		if(str[i] > str[i+1]) {
			str[i]--;
			str[i+1] = '9';
			for(int j=i+2; j<len;j++) {
				str[j] = '9';
			}
			return find_ans(str);
		}
	}
	return str;
}
int main() {
	int t;
	char str[20];
	char* ans;
	scanf("%d",&t);
	for(int i=1; i<=t;i++) {
		scanf("%s", str);
		printf("Case #%d: ",i);
		ans = find_ans(str);
		int len = strlen(str);
		int fin_len=len;
		for(int j=0; j<len;j++) {
			if(ans[j]!='0') {
				break;
			} else {
				fin_len--;
			}
		}
		if(fin_len == 0) {
			printf("0");
		} else {
			for(int j=0;j<fin_len;j++) {
				printf("%c", ans[len-fin_len + j]);
			}
		}
		printf("\n");
	}
}