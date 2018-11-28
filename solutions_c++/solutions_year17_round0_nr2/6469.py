#include <bits/stdc++.h>
using namespace std;
#define FOR(i,n) for(int i=0;i<(n);i++)

char s[20];
char res[20];
int len;

int BP(){
	int head = 0;
	int i;
	for(i=0;i<len-1;i++){
		if(s[i]>s[i+1]){
			break;
		}
		if(s[i]<s[i+1]) head = i+1;
	}
	if(i == len-1) return len-1;
	return head;
}

int main(){
	int T, t=0;
	scanf("%d",&T);
	while(t<T){
		t++;
		printf("Case #%d: ", t);
		scanf("%s", s);
		len = strlen(s);
		int bp = BP();
		if(bp == (len-1)) puts(s);
		else if(s[bp] == '1') {
			for(int i=0;i<len-1;i++)printf("9");
			puts("");
		}
		else{
			for(int i=0;i<len;i++){
				if(i<bp) printf("%c",s[i]);
				else if(i==bp) printf("%c",s[i]-1);
				else printf("9");
			}
			puts("");
		}
	}
}

