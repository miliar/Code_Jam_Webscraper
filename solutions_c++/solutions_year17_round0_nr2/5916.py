#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
using namespace std;



int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		unsigned long long int n;
		scanf("%lld",&n);
		int num=((int)log10(n)) +1 ;
		unsigned long long int exp=1;
		for(int j=0;j<num-1;j++)
			exp*=10;
		bool dec=false;
		int org_num[num];
		int ans[num];
		for(int j=0;j<num;j++)
		{
			org_num[j]=n/exp;
			n=n%exp;
			exp/=10;
		}

		for(int j=0;j<num;j++)
		{
			if(dec)
				ans[j]=9;
			else if(org_num[j]<=org_num[j+1] || j == num-1)
			{
				ans[j]=org_num[j];
			}
			else
			{
				ans[j]=org_num[j];
				int k=j;
				while((k>=0) && (org_num[j]==org_num[k]))
					k--;
				k++;
				ans[k]--;
				k++;
				while(k<=j){
					ans[k]=9;
					k++;
				}	
				dec=true;
			}
		}
		printf("Case #%d: ",i+1);
		bool trail_zero=true;
		for(int j=0;j<num;j++)
		{
			if(trail_zero && ans[j]==0)
				continue;
			else if(ans[j]!=0)
			{
				trail_zero=false;
			}
			printf("%d",ans[j]);
		}
		printf("\n");
	}
}
