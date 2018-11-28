#include<stdio.h>
#include<process.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<stdlib.h>
using namespace std;
int main() {
   FILE *fp1, *fp2;
   long long int i,j,n,m,t;
   double x,min,f,d,l,k; 
   fp1=fopen("C:\\Users\\subham7\\Downloads\\A-large (2).in", "r");
   fp2=fopen("E:\\file8.txt", "w");
   fscanf(fp1,"%lld",&t);
   for(i=1;i<=t;i++)
   {
   	fscanf(fp1,"%lf%lld",&d,&n);
   	for(j=0;j<n;j++)
   	{
   		fscanf(fp1,"%lf%lf",&k,&l);
   		f=(d-k)/l;
   	//	if((d-k)%l!=0)
   	//	f=f+1;
   		x=d/f;
   		//printf("%f\n",x);
   		if(j==0)
   		min=x;
   		if(x<min)
   		min=x;
	}
   	fprintf(fp2,"Case #%lld: %.6f\n",i,min);
   }
   fclose(fp1);
   fclose(fp2);
   return 0;
}
