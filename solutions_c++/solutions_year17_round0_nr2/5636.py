#include<stdio.h>
#include<string>
using namespace std;

char arr[20];
int t,cont;
string num;
bool ind;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("salida.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		cont++;
		ind=false;
		scanf("%s",arr);
		num=arr;
		for(int i=num.length()-1;i>0;i--){
			if(num[i]=='*') continue;
			if(num[i]<num[i-1]){
				num[i-1]=num[i-1]-1;
				for(int j=i;j<num.length();j++) num[j]='9';
			}
		}
		printf("Case #%d: ",cont);
		for(int i=0;i<num.length();i++){
			if(num[i]!='0'){
				ind=true;
				printf("%c",num[i]);
			}else if(ind) printf("0");
		}
		printf("\n");
	}
	fclose(stdout);
}