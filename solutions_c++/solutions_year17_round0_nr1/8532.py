#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;

int main(void){
	freopen("A-small-attempt5.in","r",stdin);
	freopen("out.txt","w",stdout);
	bool solve=false;
	int ca,flipsize;
	scanf("%d",&ca);

	for(int i=0;i<ca;i++){
		solve==false;
		char s[1000]={0};		
		scanf("%s",&s);
		int len = strlen(s);
		scanf("%d",&flipsize);
		int index=0,dotime=0;
		while(index<=len){//watch out impossible case,Ä²©³
			if(s[index]=='-'){
				if(index+flipsize>len){//impossible case
					printf("Case #%d: IMPOSSIBLE\n",i+1);
					solve=true;
					break;
				}

				for(int k=index;k<index+flipsize;k++){
					if(s[k]=='+'){
						s[k]='-';
						//index=k;
					}
					else{
						s[k]='+';
					}
				}
				dotime++;
			}
			else{
				index++;
				//fprintf(stderr,"%d ",index);
			}

			if(index>len){
				printf("Case #%d: %d\n",i+1,dotime);
				solve=true;
			}
		}

		if(index<len&&solve==false){//collision with impossible case
			fprintf(stderr,"test case %d failed\n",i+1);
			fflush(stderr);
		}
	}
}