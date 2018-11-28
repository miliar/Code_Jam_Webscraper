#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
    freopen("A-largeoutput.out","w",stdout);
	int t,r,c,i,j,k,l,m,index1,index2,index3,index4,flag;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
	    scanf("%d %d",&r,&c);
	    char ch[r][c+1];
	    int vis[r][c];
	    for(j=0;j<r;j++)
	    {
	        for(k=0;k<c;k++)
	        vis[j][k]=0;
	    }
	    for(j=0;j<r;j++)
	    scanf("%s",ch[j]);
	    for(j=0;j<r;j++)
	    {
	        for(k=0;k<c;k++)
	        {
	            if(ch[j][k]!='?' && vis[j][k]==0)
	            {
	                l=k-1;
	                index1=k;
	                while(l>=0)
	                {
	                    if(ch[j][l]=='?')
	                    index1--;
	                    else
	                    break;
	                    l--;
	                }
	                l=k+1;
	                index2=k;
	                while(l<c)
	                {
	                    if(ch[j][l]=='?')
	                    index2++;
	                    else
	                    break;
	                    l++;
	                }
	                l=j-1;
	                index3=j;
	                while(l>=0)
	                {
	                    flag=1;
	                    for(m=index1;m<=index2;m++)
	                    {
	                        if(ch[l][m]!='?')
	                        {
	                            flag=0;
	                            break;
	                        }
	                    }
	                    if(flag==1)
	                    {
	                        index3--;
	                        l--;
	                    }
	                    else
	                    break;
	                }
	                l=j+1;
	                index4=j;
	                while(l<r)
	                {
	                    flag=1;
	                    for(m=index1;m<=index2;m++)
	                    {
	                        if(ch[l][m]!='?')
	                        {
	                            flag=0;
	                            break;
	                        }
	                    }
	                    if(flag==1)
	                    {
	                        index4++;
	                        l++;
	                    }
	                    else
	                    break;
	                }
	                for(l=index3;l<=index4;l++)
	                {
	                    for(m=index1;m<=index2;m++)
	                    {
	                        ch[l][m]=ch[j][k];
	                        vis[l][m]=1;
	                    }
	                }
	            }
	        }
	    }
	    printf("Case #%d:\n",i);
	    for(j=0;j<r;j++)
	    printf("%s\n",ch[j]);
	}
	return 0;
}
