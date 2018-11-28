#include <cstdio>

void run() {
	char str[20] = {};
	scanf("%s",str);
	int len;
	for(len=0;str[len]!='\0';++len);
	for(int i=len-1;i>0;--i) {
		if(str[i] < str[i-1]) {
			str[i-1]--;
			for(int j=i;j<len;j++)
				str[j] = '9';
		}
	}
	int i;
	for(i=0;i<len;i++)
		if(str[i]!='0')break;
	for(;i<len;i++)
		printf("%c",str[i]);
	printf("\n");
}

int main() {
	int N;
	scanf("%d",&N);
	for(int i=1;i<=N;i++) {
		printf("Case #%d: ",i);
		run();
	}
}