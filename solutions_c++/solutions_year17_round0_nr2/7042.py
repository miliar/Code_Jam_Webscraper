#include <cstdio>
#include <algorithm>
using namespace std;

bool vis[20]={0};
bool foo(char *str, int i, int sz, bool respect) {
	if(i==sz) return false;
	if(!respect) {
		str[i]='9';
		vis[i] = true;
		if(!vis[i+1])
			foo(str,i+1,sz,respect);
		return false;
	}
	if(i+1==sz) return false;
	
	
	if(str[i]>str[i+1]) {
		--str[i];
		foo(str,i+1,sz,false);
		return true;
	}
	
	if(foo(str,i+1,sz,respect)) return foo(str,i,sz,respect);
	return false;
}

int main() {
	int i,j,k,T,C,S,f,sz;
	char str[20];
	scanf("%i",&C);
	for(T=1;T<=C;++T) {
		scanf(" %s",str);
		printf("Case #%i: ",T);
		S=sz=0;
		while(vis[sz]=0, str[sz]!='\0')++sz;
		
		foo(str,0,sz,true);
		i=0;
		while(str[i]=='0')++i;
		printf("%s",str+i);
		
		if(T!=C) printf("\n");
	}
}