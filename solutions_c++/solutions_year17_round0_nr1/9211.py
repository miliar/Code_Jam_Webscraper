#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;
main()
{	FILE *fp1;
	fp1=fopen("A-large (1).txt","r");
	int t,q,fl=1,i,k,j,z;char s1[100];
	fscanf(fp1,"%d",&t);
	int count[t];
	for(i=0;i<t;i++){
		count[i]=0;
		fl=1;
		char s[1000];
		fscanf(fp1,"%s %d",s,&k);
		for(z=0;s[z]!='\0';z++);
		for(j=0;j<=z-1;j++){
			if(s[j]=='-'){
				if(j+k<=z){
					count[i]++;
					for(q=j;q<j+k;q++){
						if(s[q]=='-'){
						s[q]='+';
						}
						else{
						s[q]='-';
						}
					}
				}
				else{
					fl=0;
					count[i]=-1;
					break;
				}
			}
		}
	}
	
	FILE *fp;
	fp=fopen("google2.txt","w");
	for(i=0;i<t;i++){
		if(count[i]!=-1){
			fprintf(fp,"%s%d%s%d\n","Case #",i+1,": ",count[i]);
		}
		else{
			fprintf(fp,"%s%d%s%s\n","Case #",i+1,": ","IMPOSSIBLE");
		}
	}
}
