#include<bits/stdc++.h>
using namespace std;
int main(void)
{
	char a[102][12],c[102];
	int i=0,n,j,k,l,len,b[102]={0};
    FILE *fp1=fopen("A-small-attempt1.txt","r");
    while(!feof(fp1))
    {
    	if(i==0)
    	{
    		fscanf(fp1,"%d",&n);
    		i++;
    		continue;
    	}
    	fscanf(fp1,"%s %d",&a[i-1],&c[i-1]);
    	i++;
    }
    for(j=0;j<n;j++)
    {
    	int flag=1;
    	len=strlen(a[j]);
    	for(k=0;k<len-c[j]+1;k++)
    	{
    		if(a[j][k]=='+')
    		continue;
    		else
    		{
    			for(l=k;l<k+c[j];l++)
    			{
    				if(a[j][l]=='+')
    				a[j][l]='-';
    				else
    				a[j][l]='+';
    			}
    			b[j]++;
    		}
    	}
    	for(k=len-c[j];k<len;k++)
    	{
    		if(a[j][k]=='-')
    		{
    			flag=0;
    			break;
    		}
    	}
    	if(flag==0)
    	b[j]=9999;
    	printf("%s\n",a[j]);
    }
    fclose(fp1);   
    FILE *fp2=fopen("result.txt","wt+");
    for(j=0;j<n;j++){
    if(b[j]!=9999)
    fprintf(fp2,"Case #%d: %d\n",j+1,b[j]);
	else
	fprintf(fp2,"Case #%d: IMPOSSIBLE\n",j+1);
	}
    fclose(fp2);
	return 0;
}
