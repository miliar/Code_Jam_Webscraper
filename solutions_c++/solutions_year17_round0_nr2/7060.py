#include<bits/stdc++.h>
using namespace std;

int main(){
	int n, tc=1;
	long long data;
	scanf("%d",&n);
	
	while(n--){
		int len, idx=0;
		char arr[100]={};
		scanf("%lld",&data);
		
		while(data){
			arr[idx++]=((data%10)+48);
			data/=10;
		}
		strrev(arr);
		
		len = strlen(arr);
		for(int i=1;i<len;i++){
			if(arr[i] < arr[i-1]){
				arr[i-1]-=1;
				for(int j=i;j<len;j++) arr[j]=57;
				i=0;
			}
		}
		
		int start=0;
		for(int i=0;i<len;i++){
			if(arr[i]!=48){
				start=i;
				break;
			}
		}
		
		printf("Case #%d: ",tc++);
		for(int i=start;i<len;i++) printf("%c",arr[i]);
		printf("\n");
	}
		
	return 0;
}
