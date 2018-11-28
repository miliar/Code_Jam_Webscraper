#include<bits/stdc++.h>
using namespace std;
int main(void)
{
	char a[102][20],b[102][20];
	int i=0,n,j,k,l,len,num=0;
    FILE *fp1=fopen("B-large.txt","r");
    while(!feof(fp1))
    {
    	if(i==0)
    	{
    		fscanf(fp1,"%d",&n);
    		i++;
    		continue;
    	}
    	fscanf(fp1,"%s",&a[i-1]);
    	i++;
    }
    fclose(fp1);
    for(j=0;j<n;j++)
    {
    	len=strlen(a[j]);
    	//a[j][len]='9';
    	int flag=0,p=0,q=0;
    	for(k=0;k<len;k++)
    	{
			if(a[j][k]=='0')
    		{
    			p=k;
    			break;
    		}
    		if(a[j][k]!='1')
    		break;   		
    	}
    	for(k=0;k<len;k++)
    	{
    		if(a[j][k]=='0')
    		{
    			q=k;
    			break;
    		}
    	}
    	if(p)
    	{
    		for(k=0;k<len-1;k++)
    		b[j][k]='9';
    		b[j][len-1]='\0';
    		continue;
    	}
    	else
    	{
    		for(k=0;k<len-1;k++)
    		{
    			if(a[j][k]<=a[j][k+1])
    			b[j][k]=a[j][k];
    			else
    			{
    				flag=1;int flag1=0;
    				for(l=k;l>0;l--)
    				{
    					if(a[j][l-1]<a[j][l])
    					{
    						flag1=1;
    						k=l;
    						break;
    					}
    				}
    				if(flag1==0)
    				k=0;
    				printf("%d %d %d\n",flag1,k,k);
    				b[j][k]=a[j][k]-1;
    				for(l=k+1;l<len;l++)
    				b[j][l]='9';
    				break;
    			}
    		}
    		if(flag==0)
    		b[j][len-1]=a[j][len-1];
    	}
    	b[j][len]='\0';
    	printf("%s%s%s",b[j],b[j],b[j]);
    }
    FILE *fp2=fopen("result.txt","wt+");
    for(j=0;j<n;j++)
    fprintf(fp2,"Case #%d: %s\n",++num,b[j]);
    fclose(fp2);
	return 0;
}
