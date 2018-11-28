#include <bits/stdc++.h>
#define fr(x) scanf("%d", &x)
using namespace std;

char s[128];

int main(){
	int t, flag, len;
	fr(t);

	for(int t1=1; t1<=t ;++t1){
		scanf(" %s", &s[1]);
		flag=-1;

		len=strlen(&s[1]);

		for(int i=1;i<len;++i){
			if(s[i+1]<s[i]){
				flag=s[i];
				break;
			}
		}

		if(flag==-1){
			printf("Case #%d: %s\n", t1, &s[1]);
		}
		else{
			int i;
			for(i=1;s[i]!=flag;++i){
			}
			--s[i];
			++i;
			for(;s[i]!='\0';++i){
				s[i]='9';
			}

			printf("Case #%d: %s\n", t1, ((s[1]=='0') ? (&s[2]) : (&s[1])));
		}
	}
	return 0;
}