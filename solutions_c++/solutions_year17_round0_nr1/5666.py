#include<stdio.h>
using namespace std;

int t,cont;
int k;
char arr[10000+10];
bool ind;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("salida.out","w",stdout);
	scanf("%d",&t);
	for(int h=1;h<=t;h++){
		scanf("%s%d",arr,&k);
		cont=0;
		ind=false;
		for(int i=0;arr[i+k-1]!=0;i++){
			if(arr[i]=='-'){
				for(int j=i;j<=i+k-1;j++) arr[j]=(arr[j]=='-'? '+':'-');
				cont++;
			}
		}
		for(int i=0;arr[i]!=0;i++){
			if(arr[i]=='-'){
				ind=true;
				break;
			}
		}
		printf("Case #%d: ",h);
		if(ind) printf("IMPOSSIBLE\n");
		else printf("%d\n",cont);
	}
	fclose(stdout);
}