#include <cstdio>
#include <algorithm>
using namespace std;


int main() {
	int i,j,k,T,C,S,f,sz;
	char str[1000];
	scanf("%i",&C);
	for(T=1;T<=C;++T) {
		scanf(" %s%i",str,&f);
		printf("Case #%i: ",T);
		S=sz=0;
		while(str[sz]!='\0')++sz;
		for(i=0;(i+f)<=sz;++i) {
			if(str[i]=='-') {
				for(j=0;j<f;++j)
					str[i+j] = (((str[i+j])=='-')?'+':'-');
				++S;
			}
		}
		bool good = true;
		for(i=0;i<sz;++i) 
			if(str[i]=='-') 
				good=false;
		if(good) printf("%i",S);
		else printf("IMPOSSIBLE");
		if(T!=C) printf("\n");
	}
	
}