#include<stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	int num, i, j, count, s_check;
	FILE *fp;
	int k;
	char str[20]={0,};
	char check[20]={0,};
	
	fp=fopen("B-large.in","r");
	
	fscanf(fp,"%d",&num);
	//scanf("%d",&num);
	
	for(i=0;i<num;i++){
		fscanf(fp,"%s",str);
	
	//	scanf("%s",str);
		
		count=0;
		s_check=-1;
		
		for(j=0;j<20;j++){
			if(str[j]>='0' && str[j]<='9')
			{
				count++; // ÀÚ¸® ¼ö  
				str[j] = str[j] - '0';
			}else{
				break;
			}
		}
		
		for(j=0;j<count-1;j++){
			
			if(str[j]==str[j+1]){
				check[j]='1';
			}
			else if(str[j]>str[j+1]){
				check[j]='2';
				s_check=j;
				break;
			}else{
				check[j]='0';
			}
			
		}
		
	//	printf("%s %d ",check, s_check);
		
		for(j=s_check-1;j>=0;j--){
			if(check[j]!='1')
				break;
		}
		
//		printf("%d ",j);
		if(s_check!=-1){
			for(k=j+2;k<count;k++){
				str[k]=0;
			}
			
			str[count-1]--;
		}
		
		
		
		for(j=count-1;j>=0;j--){
			if(str[j]<0){
				str[j]+=10;
				str[j-1]--;
			}
			
		}
		
		printf("Case #%d: ",i+1);
		for(j=0;j<count;j++){
			if(j==0 && str[j]== 0){
			}else{
				printf("%d",str[j]);
			}
		}
		printf("\n");
	}
	
	
}
