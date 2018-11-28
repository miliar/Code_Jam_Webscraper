#include<bits/stdc++.h>
using namespace std;

char a[20];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,_,i,j;
	for(scanf("%d",&T),_=1;_<=T;_++)
	{
		scanf("%s",a);
		do{
			for(i=1;a[i];i++){
				if(a[i]<a[i-1]){
					a[i-1]--;
					for(j=i;a[j];j++) a[j]='9';
					break;
				}
			}
		}while(a[i]);
		printf("Case #%d: %s\n",_,a+(a[0]=='0')),fprintf(stderr,"Case #%d: %s\n",_,a+(a[0]=='0'));
	}
	return 0;
}
