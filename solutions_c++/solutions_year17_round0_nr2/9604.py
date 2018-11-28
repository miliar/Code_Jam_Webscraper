#include<iostream>
#include<stdlib.h>
using namespace std;
main()
{	int t,j,z,i,var=0,n[100];
	FILE *fp1;
	fp1=fopen("B-small-attempt0 (1).txt","r");
	//int t,q,fl=1,i,k,j,z;
	fscanf(fp1,"%d",&t);
	for(i=0;i<t;i++){
		int a,b,s[20];
		fscanf(fp1,"%d",&a);
		while(a>0){
		b=a;z=0;var=0;
		while(a != 0){
			s[z]=a%10;z++;
        	a/= 10;
        }
        while(--z){
        	if(s[z]>s[z-1]){break;}
		}
		if(z==0){var=1;break;}  ///number found
		else{b--;a=b;}
		}
	if(var==1){ n[i]=b;}
	}
	FILE *fp;
	fp=fopen("google2.txt","w");
	for(i=0;i<t;i++){
		fprintf(fp,"%s%d%s%d\n","Case #",i+1,": ",n[i]);
	}
	
}
