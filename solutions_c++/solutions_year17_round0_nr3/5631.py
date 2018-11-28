#include <stdio.h>
#include<bits/stdc++.h>using namespace std;
struct set
{
    int low;
    int high;
    int number;
}s[1000];
int calculate(int arr[],int n)
{
	int t=0,i;
for(i=0;i<=999;i++)
	{
	    s[i].number=0;

	}
	t=0;
	for(i=0;i<=n;i++)
	{
	    if(arr[i]==1&&arr[i+1]==0)
	    {
	        s[t].low=i+1;
	   }
	    if(arr[i]==0)
	    {
	        s[t].number=s[t].number+1;
	    }

	    if(arr[i]==0&&arr[i+1]==1)
	     {
	         s[t].high=i;
	         t++;

	     }

	}
	return t;
}

void placemiddle(int a,int b,int arr[],int n)
{
    arr[(a+b)/2]=1;
}

int main(void) {
    freopen("input3.txt","r",stdin);
	 freopen("output3.txt","w",stdout);
    int arr[1002],i,j,k,n,t,d,maxnumber,temp,temp1,temp2,a,b,u,test,y;
	scanf("%d",&test);
	for(u=0;u<=test-1;u++)
	{
	scanf("%d",&n);
	scanf("%d",&k);

	for(i=0;i<=999;i++)
	{
	    s[i].number=0;
	}
	for(i=1;i<=n;i++)
	{
	    arr[i]=0;
	}
	arr[0]=1;
	arr[n+1]=1;


	t=calculate(arr,n);


	d=k;
	while(d>0)
	{
	    t=calculate(arr,n);


	    maxnumber=s[0].number;
	    temp=0;
	    for(j=0;j<=t-1;j++)
	    {
	        if(s[j].number>maxnumber)
	        {
	            maxnumber=s[j].number;
	            temp=j;

	        }


	    }
	    placemiddle(s[temp].low,s[temp].high,arr,n);
	  a=s[temp].low;
	  b=s[temp].high;
	  if(d==1)
	  {
	      for(i=((a+b)/2)-1;i>=0;i--)
	      {
	          if(arr[i]==1)
	          {
	              temp1=(a+b)/2-1-i;
	              break;
	          }
	      }
	      for(i=((a+b)/2)+1;i<=n+1;i++)
	      {
	          if(arr[i]==1)
	          {
	              temp2=i-(a+b)/2-1;

	              break;
	          }
	      }
	  }


	    d--;

	}

	printf("Case #%d: ",u+1);
	if(temp1>temp2)
    printf("%d %d\n",temp1,temp2);
	else
	printf("%d %d\n",temp2,temp1);
	}
	return 0;
}

