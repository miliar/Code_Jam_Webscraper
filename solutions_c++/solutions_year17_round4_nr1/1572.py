#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>

using namespace std;

int main()
{
	int t=0,T=0;
	
	FILE * fin=fopen("input.in","r");
	FILE * fin2=fopen("output.out","w");

	fscanf(fin,"%d",&T);

	while(t++<T)
	{
		int n=0, p=0, k=0, a=0, l=0;
		fscanf(fin,"%d%d",&n, &p);

		vector<int>v(5,0);

		for(int i=0;i<n;i++)
		{
			fscanf(fin,"%d",&a);
			a=a%p;
			if(a==0)
			{
				k++;
			}
			else
			{
				v[a]++;
				l++;
			}
		}

		int ost=0;
		while(l>0)
		{
			if(ost==0)
			{
				k++;
			}
			bool f=true;
			for(int i=4;i>0;i--)
			{
				if(v[i]>0 && ((ost+i)%p == 0 || ((ost+i)<p)))
				{
					l--;
					f=false;
					v[i]--;
					ost = (ost+i)%p;

					if(ost==0)
					{
						break;
					}
					i++;
				}
			}

			if(f)
			{
				for(int i=4;i>0;i--)
				{
					if(v[i]>0)
					{
						l--;
						v[i]--;
						ost = (ost+i)%p;
						break;
					}
				}
			}
		}

		fprintf(fin2, "Case #%d: %d\n", t, k);
	}

	return 0;
}