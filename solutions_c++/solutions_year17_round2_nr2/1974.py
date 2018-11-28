#include<stdio.h>
#include<process.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<stdlib.h>
using namespace std;
char a[1005];
long long int c1[1005];
int main() {
   FILE *fp1, *fp2;
   long long int i,j,n,m,t,a1,a2,a3,a4,a5,a6,c[5],b[5];
   long long int x,min,f,d,l,k,p,s; 
   fp1=fopen("C:\\Users\\subham7\\Downloads\\B-small-attempt2.in", "r");
   fp2=fopen("E:\\file8.txt", "w");
   fscanf(fp1,"%lld",&t);
   for(i=1;i<=t;i++)
   {
   	fscanf(fp1,"%lld%lld%lld%lld%lld%lld%lld",&n,&a1,&a2,&a3,&a4,&a5,&a6);
    b[0]=a1;
    c[0]=1;
    b[1]=a3;
    c[1]=2;
    b[2]=a5;
    c[2]=3;
    for(j=0;j<2;j++)
    {
    	for(p=0;p<2;p++)
    	{
    		if(b[p+1]<b[p])
    		{
    			d=b[p+1];
    			b[p+1]=b[p];
    			b[p]=d;
    			d=c[p+1];
    			c[p+1]=c[p];
    			c[p]=d;
			}
		}
	}
	x=b[0]-b[2]+b[1];
	c1[0]=2;
	c1[1]=1;
	if(x>0)
	{
		c1[2]=0;
	}
	p=0;
	s=1;
	if(x>=0)
   	{
	for(j=0;j<n;j++)
   	{
	   if(c1[j]==2)
	   {
	   	    if(c[2]==1)
	   	    a[j]='R';
	   	    else if(c[2]==2)
	   	    a[j]='Y';
	   	    else
	   	    a[j]='B';
	   	    if(x>0)
	   	    c1[j+3]=2;
	   	    else
	   	    c1[j+2]=2;
	   }
	   else if(c1[j]==1)
	   {
	   	    if(s>b[1])
	   	    p=1;
	   	    if(c[1-p]==1)
	   	    a[j]='R';
	   	    else if(c[1-p]==2)
	   	    a[j]='Y';
	   	    else
	   	    a[j]='B';
	   	    if(x>0)
	   	    c1[j+3]=1;
	   	    else
	   	    c1[j+2]=1;
	   	    s=s+1;
	   }
	   else
	   {
	   	    if(c[0]==1)
	   	    a[j]='R';
	   	    else if(c[0]==2)
	   	    a[j]='Y';
	   	    else
	   	    a[j]='B';
	   	    x=x-1;
	   	    if(x>0)
	   	    c1[j+3]=0;
	   }   
	}
	fprintf(fp2,"Case #%lld: ",i);
	for(j=0;j<n;j++)
	fprintf(fp2,"%c",a[j]);
	fprintf(fp2,"\n");
    }
	else
	fprintf(fp2,"Case #%lld: IMPOSSIBLE\n",i,min);
   }
   fclose(fp1);
   fclose(fp2);
   return 0;
}
