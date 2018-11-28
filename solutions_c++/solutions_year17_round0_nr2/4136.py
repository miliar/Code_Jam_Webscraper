#include <bits/stdc++.h>
#define M 18
using namespace std;
char a[M+1];
int n;

void input(void){
	scanf("%s",a);
	n=strlen(a);
}

void process(void){
	int i,j=0;
	for(i=1;i<n;i++){
		if(a[i]<a[j]){
			for(i=0;i<j;i++) printf("%c",a[i]);
			if(!(j==0 && a[j]=='1')){
				printf("%c",a[i]-1);
			}
			for(j++;j<n;j++)printf("9");
			break;
		}if(a[i]>a[j]){
			j=i;
		}
	}
	if(i==n) printf("%s",a);
	printf("\n");
}

int main(){
	freopen("input.txt","r",stdin);

	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		printf("Case #%d: ",i);
		input();
		process();
	}
	return 0;
}
