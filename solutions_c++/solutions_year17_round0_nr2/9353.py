#include <stdio.h>
#include <string.h>

char s[100];
int len;

bool Judge(){
	len = strlen(s);
	for(int i = 0; i < len - 1; ++i){
		if(s[i] > s[i + 1]) return false;
	}
	return true;
}

void Change(){
	char ss[100];
	memset(ss,0,sizeof(ss));
	int p = 0;
	for(int i = 0; i < len - 1; ++i){
		if(s[i] > s[i + 1]){
			s[i]--;
			if(s[i] > '0') ss[p++] = s[i];
			if(s[i] == '0' && i > 0) ss[p++] = s[i];
			for(int j = i + 1; j < len; ++j) ss[p++] = '9';
			break;
		}
		ss[p++] = s[i];
	}
	memcpy(s,ss,sizeof(ss));
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int tt = 1; tt <= T; ++tt){
		scanf("%s",s);
		printf("Case #%d: ",tt);
		while(!Judge()){
			Change();
		}
		printf("%s\n",s);
	}
	return 0;
}