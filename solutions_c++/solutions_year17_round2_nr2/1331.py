#include<iostream>
#include<cstdio>
using namespace std;
int tt;
int main(){
	int T,I;
	cin>>T;
	for(I=0;I<T;I++){
		int n;
		int a[6],i,j,b[1005]={};
		char c[8]="ROYGBV";
		tt=0;
		scanf("%d",&n);
		for(i=0;i<6;i++)scanf("%d",&a[i]);
		printf("Case #%d: ",I+1);
		if(a[0]>=a[2]&&a[0]>=a[4]){
			if(a[0]>a[2]+a[4])printf("IMPOSSIBLE");
			else{
				while(a[0]<a[2]+a[4]){
					printf("RYB");
					a[0]--;
					a[2]--;
					a[4]--;
				}
				for(i=0;i<a[2];i++)printf("RY");
				for(i=0;i<a[4];i++)printf("RB");
			}
		}
		else if(a[2]>=a[0]&&a[2]>=a[4]){
			if(a[2]>a[0]+a[4])printf("IMPOSSIBLE");
			else{
				while(a[2]<a[0]+a[4]){
					printf("YRB");
					a[0]--;
					a[2]--;
					a[4]--;
				}
				for(i=0;i<a[0];i++)printf("YR");
				for(i=0;i<a[4];i++)printf("YB");
			}
		}
		else{
			if(a[4]>a[2]+a[0])printf("IMPOSSIBLE");
			else{
				while(a[4]<a[2]+a[0]){
					printf("BRY");
					a[0]--;
					a[2]--;
					a[4]--;
				}
				for(i=0;i<a[2];i++)printf("BY");
				for(i=0;i<a[0];i++)printf("BR");
			}
		}
		cout<<endl;
	}
	return 0;
}