#include <iostream>
#include <vector>
#include <fstream>
#include <string.h>
using namespace std;
#define f(i,n) for(int i=0;i<n;i++)
//ofstream coutp("smallop.txt");
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	f(jtt,t)
	{
		int r,c;
		cin>>r>>c;
		char a[r+1][c+1];
		f(i,r)	f(j,c)	cin>>a[i][j];

		int bl[r];
		f(i,r)	bl[i]=1;
		int i=0;
		while(i<r)
		{
			int j=0;
			int blc=0;

//			blc=0;
//			j=0;
			while(j<c)
			{
				int jc=0,blct=0;
				while(jc<c)
				{
					if(a[i][jc++]=='?')	blct++;
				}
				if(blct==0){
					bl[i]=0;
					break;
				}
				if(blct==c){
					bl[i]=1;
					break;
				}
				while(j<c)
				{
					if(a[i][j]=='?')	j++,blc++;
					else	break;
				}
				if(j==c && blc==0){
					bl[i]=0;
					break;
				}
				if(j==c)
				{
					if(blc==c)	bl[i]=1;
					else	bl[i]=0;
					i++;
					break;
				}
				else
				{
					char t=a[i][j];
					int tj=j--;
					while(j>=0)
					{
						if(a[i][j]=='?')	a[i][j--]=t;
						else	break;
					}
					j=tj+1;
					while(j<c)
					{
						if(a[i][j]=='?')	a[i][j++]=t;
						else	break;
					}
					bl[i]=0;
				}
			}
			i++;
		}
//		f(i,r)	cerr<<bl[i];
		f(i,r)
		{
			if(bl[i]==1)
			{
				int in=i;
				if(i==0)
				{
					while(bl[in]==1)	in++;
					f(k,c)
						a[i][k]=a[in][k];
				}
				else
				{
					while(bl[in]==1)	in--;
					f(k,c)	a[i][k]=a[in][k];
				}
				bl[i]=0;
			}
		}
		coutp<<"Case #"<<jtt+1<<":\n";
		f(i,r){
			f(j,c){
				coutp<<a[i][j];
				if(a[i][j]<'A' || a[i][j]>'Z')	cerr<<jtt+1<<" ";
			}
			coutp<<"\n";
		}





	}
	return 0;
}
