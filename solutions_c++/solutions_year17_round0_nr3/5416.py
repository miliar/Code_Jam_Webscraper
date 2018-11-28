#include <stdio.h>
#include <string.h>
#include <algorithm>
 
using namespace std;

int main(void)
{
	FILE *in=fopen("1.inp","r");
	FILE *out=fopen("1.out","w");
	int t,tt,n,k,i,j,s,left_close,right_close,t_index,t_Ls,t_Rs;
	int arr[1002];
	fscanf(in,"%d",&t);	
	for(tt=1;tt<=t;tt++)
	{
		memset(arr,0,sizeof(arr));
		fscanf(in,"%d%d",&n,&k);
		arr[0]=arr[n+1]=1;
		for(i=0;i<k;i++)
		{
			t_index=-1;
			for(j=0;j<n+2;j++)
			{
				if(arr[j]==1)
				{
					left_close=j;
					continue;
				}
				for(s=j+1;s<n+2;s++)
					if(arr[s]==1)	
					{
						right_close=s;
						break;	
					}
				if(t_index==-1)
				{
					t_index=j;
					t_Ls=j-left_close-1;
					t_Rs=right_close-j-1;	
				}
				else
				{
					if(min(j-left_close-1,right_close-j-1)>min(t_Ls,t_Rs))
					{
						t_index=j;
						t_Ls=j-left_close-1;
						t_Rs=right_close-j-1;
					}
					else if(min(j-left_close-1,right_close-j-1)==min(t_Ls,t_Rs) && max(j-left_close-1,right_close-j-1)>max(t_Ls,t_Rs))
					{
						t_index=j;
						t_Ls=j-left_close-1;
						t_Rs=right_close-j-1;
					}
				}
			}
			arr[t_index]=1;
		}
		fprintf(out,"Case #%d: %d %d\n",tt,max(t_Ls,t_Rs),min(t_Ls,t_Rs));
	}
	return 0;
}
