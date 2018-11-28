#include <cstdio>
#include <cstring>

char str[1010]; 

void run() {
	int k, len, cou = 0;
	scanf("%s%d",str, &k);
	for(len=0;str[len]!='\0';++len);
	for(int i=0;i<len - k + 1;i++) {
		if(str[i]=='-') {
			for(int j=0;j<k;j++)
				if(str[i+j] == '+')
					str[i+j] = '-';
				else
					str[i+j] = '+';
			++cou;
		}
	}
	for(int i=0;i<k;i++)
		if(str[len-1-i]=='-') {
			printf("IMPOSSIBLE\n");
			return ;
		}
	printf("%d\n",cou);
}

int main() {
	int N;
	scanf("%d",&N);
	for(int i=1;i<=N;i++) {
		printf("Case #%d: ",i);
		run();
	}
}