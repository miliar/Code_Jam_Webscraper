#include <stdio.h>
#include <string.h>
 int main(){
 	int T,E,R,flag;
 	scanf("%d",&T);
 	char S[1000];char c;int lS;
 	for(int c1=0;c1<T;c1++){
 		R=0;lS=0;flag=0;
 		getchar();
 		while(1){
			 c=getchar();
			 if(c!=32)
			 	S[lS++]=c;
			else break;
		}
		scanf("%d",&E);
		for(int c2=0;c2<=lS-E;++c2){
			if(S[c2]=='-'){
				for(int c3=0;c3<E;c3++){
					if(S[c2+c3]=='-')S[c2+c3]='+';
					else	S[c2+c3]='-';
				}
				R++;
			}
		}
		for(int c2=lS-E;c2<lS;c2++){
			if(S[c2]=='-'){
				flag=1;
				break;
			}
		}
		if(flag==0)printf("Case #%d: %d\n",c1+1,R);
		else	printf("Case #%d: IMPOSSIBLE\n",c1+1);
 	}
}
