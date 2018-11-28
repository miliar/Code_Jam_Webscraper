#include<bits/stdc++.h>
using namespace std;
long long a[102],b[102],c[102];
int p[102];
int main(void)
{
	int i=0,n,j,k,l,len,temp;
    FILE *fp1=fopen("C-small-2-attempt0.txt","r");
    while(!feof(fp1))
    {
    	if(i==0)
    	{
    		fscanf(fp1,"%d",&n);
    		i++;
    		continue;
    	}
    	fscanf(fp1,"%d %d",&a[i-1],&b[i-1]);
    	i++;
    }
    for(j=0;j<n;j++)
    {
    	len=0;
    	long long sum=0,rest,rest1;
    	for(k=0;;k++)
    	{
    		if(pow(2,k)-1>=b[j])
    		{
    			len=k;
    			break;
    		}
    	}
    	long long aa=pow(2,len-1);
    	sum=aa-1;
    	b[j]-=sum;
    	a[j]-=sum;
    	rest=a[j]/aa;
    	if((a[j]%aa)!=0)
    	{
    		rest+=1;	
		}
		rest1=a[j]-(rest-1)*aa;
    	if(b[j]<=rest1)
    	{
    		rest-=1;
    		c[j]=rest/2;
    		p[j]=rest-rest/2;
    		if(c[j]<p[j])
    		{
    			temp=c[j];
    			c[j]=p[j];
    			p[j]=temp;
    		}
    	}
    	else
    	{
    		rest-=1;
    		c[j]=(rest-1)/2;
    		p[j]=rest-1-c[j];
    		if(c[j]<p[j])
    		{
    			temp=c[j];
    			c[j]=p[j];
    			p[j]=temp;
    		}
    	}
    }
    fclose(fp1);   
    FILE *fp2=fopen("result.txt","wt+");
    for(j=0;j<n;j++)
	{
    	fprintf(fp2,"Case #%d: %d ",j+1,c[j]);
    	fprintf(fp2,"%d\n",p[j]);
	}
    fclose(fp2);
	return 0;
}
