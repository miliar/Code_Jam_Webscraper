#include<bits/stdc++.h>

using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",&mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define ps(mark) printf("%s\n",mark);
#define pd(mark) printf("%d\n",mark);
#define pl(mark) printf("%lld\n",mark);
#define clr(mark) memset(mark,0,sizeof(mark))
#define rec(x,y) for(x=0;x<y;x++)
#define rec_1(x,y) for(x=1;x<=y;x++)
#define F first
#define S second
#define MP make_pair
#define pb push_back
#define ll long long


int main()
{

	freopen("B-large.in","r",stdin);
	freopen("B-large-attempt.out","w",stdout);
	int t;
	sd(t);
	for(int z=1;z<=t;z++)
	{
		ll num,n;
		sl(num);
		int a[19],k=0,flag=0;
		n=num;
		while(n>0)
		{
			a[k]=n%10;
			k++;
			n=n/10;
		}
		int i=k-1,j;
		if(i==0)
		{
			printf("CASE #%d: %lld\n",z,num);
		}
		else
		{
			while(a[i]<=a[i-1])
			{
				i--;
				if(i==0)
				{
					printf("CASE #%d: %lld\n",z,num);
					flag=1;
					break;
				}
			}
			if(flag==0)
			{
				for(j=i-1;j>=0;j--)
				{
					a[j]=9;
				}
				a[i]=a[i]-1;
				for(j=i;j<k-1;j++)
				{
					if(a[j]<a[j+1])
					{
						a[j]=9;
						a[j+1]=a[j+1]-1;
					}
				}
				n=0;
				for(i=k-1;i>=0;i--)
				{
					n=(n*10)+a[i];
				}
				printf("CASE #%d: %lld\n",z,n);
			}
		}

	}	
	return 0;
} 