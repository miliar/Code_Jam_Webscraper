#include<stdio.h>
#include<string.h>
#include <stdlib.h>

int main(){
	char str[1001]={0,};
	int i,j, k;
	int n, pan, m;
	int count = 0;
	int check = 0;
	
	FILE *fp = fopen("A-large.in","r");
	
	fscanf(fp,"%d",&n);
	
	
	for(i=0;i<n;i++){
		fscanf(fp,"%s %d",str, &pan);
		
		m=0;
		for(j=0;j<1000;j++){
			if(str[j]!=NULL)
				m++;
			else if(str[j]==NULL)
				break;
		}
		
		//printf("%s %d\n",str,pan);
		
		count = 0;
		check = 0;
		
		for(j=0;j<m-pan+1;j++){
			
			if(str[j]=='-'){
				count++;
				for(k=j;k<j+pan;k++){
					
					
					
					if(str[k]=='-')
						str[k]='+';
					else if(str[k]=='+')
						str[k]='-';
						
				}
			}
		//	printf("%s\n",str);
		}
		

		
		for(j=0;j<m;j++){
			
			if(str[j]=='-')
				check = 1;
			
			str[j]=NULL;
		}
		
		printf("Case #%d: ",i+1);
		if(check == 0)
			printf("%d\n",count);
		else
			printf("IMPOSSIBLE\n");
		
	}
	

}
