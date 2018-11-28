#include<stdio.h>
#include<string.h>
int main(){
	int tc;
	scanf("%d",&tc);
	getchar();
	char arr[22];
	for(int ntc=0;ntc<tc;ntc++){
		gets(arr);
		bool valid=false;
		int count=strlen(arr)-1;
		while(valid==false){
			valid=true;
			for(int i=1;i<strlen(arr);i++){
				if(arr[i]<arr[i-1]){
					valid=false;
					break;
				}
			}
			if(valid==false){
				arr[count]='9';
				arr[count-1]-=1;
				count--;
			}
			else{
				break;
			}	
		}
		printf("Case #%d: ",ntc+1);
		for(int i=0;i<strlen(arr);i++){
			if(i==0&&arr[i]=='0'){
			}
			else{
				printf("%c",arr[i]);
			}
		}
		printf("\n");
	}
	return 0;
}
