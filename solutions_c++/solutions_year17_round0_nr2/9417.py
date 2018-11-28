#include<stdio.h>
#include<string.h>
int chartoint(char a){
	return a-'0';
}
int main(){
	int T;
	scanf("%d\n",&T);
	for(int i=1;i<=T;i++){
		char arr[20];
		gets(arr);
		//printf("%s\n",arr);
		int length = strlen(arr);
		for(int j=1;j<length;j++){
			if(chartoint(arr[j])<chartoint(arr[j-1])){
				int tempidx2 = j;
				int tempidx = -1;
				
				//printf("tempidx: %d\n",tempidx);
				for(int k=length-1;k>j-1;k--){
					//	printf("mau diganti %c %c\n",arr[k-1],arr[k]);
					arr[k] = '9';
					if(arr[k-1]==0&&k-1!=0){
						arr[k-1] = '9';
					}
					else{
						arr[k-1] = arr[k-1]-1;
					}	
					//	printf("setelah diganti %c %c\n",arr[k-1],arr[k]);
				}
				for(int k=j-1;k>0;k--){
					if(chartoint(arr[k])>=chartoint(arr[k-1])){
						break;
					}
					else{
						arr[k] = '9';
						if(arr[k-1]==0&&k-1!=0){
							arr[k-1] = '9';
						}
						else{
							arr[k-1] = arr[k-1]-1;
						}	
					}
				}
				
			}
		}
		printf("Case #%d: ",i);
		bool nol = true;
		for(int j=0;j<length;j++){
			if(nol==true&&arr[j]!='0'){
				printf("%c",arr[j]);
				nol = false;
			}
			else if(nol==false){
				printf("%c",arr[j]);
			}
		}
		printf("\n");
	}
	
}
