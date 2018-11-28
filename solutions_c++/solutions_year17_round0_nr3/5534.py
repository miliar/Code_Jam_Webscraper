#include <iostream>
#include <stdio.h>
#include <map>
#include <vector>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
using namespace std;

int main()
{
	FILE * fin=fopen("input.in","r");
	FILE * fin2=fopen("output.out","w+");

	int t=0;
	fscanf(fin,"%d",&t);
	int n=0, k=0;
	int RR=1;

	while(t-->0)
	{
		fscanf(fin,"%d%d",&n,&k);

		vector<bool>v(n,false);
		k--;

		while(k>0)
		{
			int l=0, r=0;
			int kk=0, kmax=0;

			for(int i=0;i<n;i++)
			{
				if(v[i]==true)
				{
					if(kmax<=kk)
					{
						kmax=kk;
						r=i;
					}
					kk=0;
				}
				else
				{
					kk++;
				}
			}
			
			if(kmax<=kk)
			{
				kmax=kk;
				r=n;
			}

			l=r-kmax;

			if(kmax%2==0)
			{
				v[l+(kmax>>1)-1]=true;
			}
			else
			{
				v[l+(kmax>>1)]=true;
			}
			k--;
		}

		if(true)
		{
			
			int l=0, r=0;
			int kk=0, kmax=0;

			for(int i=0;i<n;i++)
			{
				if(v[i]==true)
				{
					if(kmax<=kk)
					{
						kmax=kk;
					}
					kk=0;
				}
				else
				{
					kk++;
				}
			}
			
			
			if(kmax<=kk)
			{
				kmax=kk;
			}

			kmax--;
			int a=(kmax>>1);
			int b= kmax-a;
			
			fprintf(fin2, "Case #%d: %d %d\n",RR,a>b?a:b,a<b?a:b);

		}

		RR++;

	}

	return 0;
}