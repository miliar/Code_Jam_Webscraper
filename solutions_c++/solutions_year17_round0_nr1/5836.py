#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;


int main(){
	int t, k,steps;
	char s[2000];
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%s %d",s,&k);
		steps=0;
		int nimp=1;
		for(int j=0;j<strlen(s);j++){
			if(s[j]=='-'){
				if(strlen(s)-j<k){nimp=0;break;}
				steps++;
				for(int l=0;l<k;l++){
					if(s[j+l]=='-')s[j+l]='+';
					else s[j+l]='-';
				}
			}
		}
		if(nimp)
			printf("Case #%d: %d\n",i+1,steps);
		else
			printf("Case #%d: IMPOSSIBLE\n",i+1);
	}
	return 0;
}