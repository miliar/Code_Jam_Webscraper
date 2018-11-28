#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("B-small-attempt0.in","r",stdin);
    freopen("B-output.out","w",stdout);
	int t,n,r,o,y,g,b,v,i,j,k,cnt,flag;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
	    int b[3],c[3],d[3];
	    char ch[4];
	    scanf("%d %d %d %d %d %d %d",&n,&b[0],&o,&b[1],&g,&b[2],&v);
	    flag=1;
	    int a[n+1];
	    for(j=1;j<=n;j++)
	    a[j]=0;
	    c[0]=b[0];
	    c[1]=b[1];
	    c[2]=b[2];
	    sort(b,b+3);
	    d[0]=b[0];
	    d[1]=b[1];
	    d[2]=b[2];
	    flag=1;
	    k=1;
	    for(j=2;j>=0;j--)
	    {
	        cnt=0;
	        while(k<=n)
	        {
	            if(b[j]==0)
	            break;
	            if(a[k]==0)
	            {
	                a[k]=j+1;
	                b[j]--;
	                k++;
	                cnt++;
	            }
	            if(b[j]!=0)
	            k++;
	            cnt++;
	            if(k>n)
	            k=k%n;
	            if(cnt>n)
	            break;
	        }
	        if(b[j]!=0)
	        {
	            flag=0;
	            break;
	        }
	    }
	    if(flag==0 || (a[1]==a[n] && n!=1))
	    printf("Case #%d: IMPOSSIBLE\n",i);
	    else
	    {
	        if(d[0]==c[0])
	        {
	            ch[0]='R';
	            d[0]=-1;
	            c[0]=-2;
	        }
	        else if(d[0]==c[1])
	        {
	            ch[0]='Y';
	            d[0]=-1;
	            c[1]=-2;
	        }
	        else
	        {
	            ch[0]='B';
	            d[0]=-1;
	            c[2]=-2;
	        }
	        if(d[1]==c[0])
	        {
	            ch[1]='R';
	            d[1]=-1;
	            c[0]=-2;
	        }
	        else if(d[1]==c[1])
	        {
	            ch[1]='Y';
	            d[1]=-1;
	            c[1]=-2;
	        }
	        else
	        {
	            ch[1]='B';
	            d[1]=-1;
	            c[2]=-2;
	        }
	        if(d[2]==c[0])
	        {
	            ch[2]='R';
	            d[2]=-1;
	            c[0]=-2;
	        }
	        else if(d[2]==c[1])
	        {
	            ch[2]='Y';
	            d[2]=-1;
	            c[1]=-2;
	        }
	        else
	        {
	            ch[2]='B';
	            d[2]=-1;
	            c[2]=-2;
	        }
	        printf("Case #%d: ",i);
	        for(j=1;j<=n;j++)
	        {
	            if(a[j]==1)
	            printf("%c",ch[0]);
	            else if(a[j]==2)
	            printf("%c",ch[1]);
	            else
	            printf("%c",ch[2]);
	        }
	        printf("\n");
	    }
	}
	return 0;
}
