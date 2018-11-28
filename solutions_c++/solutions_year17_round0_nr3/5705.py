#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<fstream>

using namespace std;
void mxm(long long arngm[],long long nstl);
long long starta,enda;

int main()
{
	ifstream input;
    input.open("C-small-1-attempt1.in",ios::in);
    ofstream result;
    result.open("kmb.txt",ios::out);
    
	int tcs;
	input>>tcs;
	
	for(int t=0;t<tcs;t++)
	{
	
	long long nstl,noPeople,y;
	input>>nstl>>noPeople;
    long long len=nstl+2;
	long long arngm[len];
	
	
	   arngm[0]=1;
	   arngm[nstl+1]=1;	
		
		for(int i=1;i<nstl+1;i++)
		{
			arngm[i]=0;
		}
	
	
	
	for(int k=0;k<noPeople;k++)
	{
	    mxm(arngm,nstl);
		y=floor(((starta+1)+(enda-1))/2);
		arngm[y]=1;	
	}
	long long l,r,count=0;
	
	for(long long j=y-1;j>0 && j<nstl+1 ;j--)
		{
			if(arngm[j]==0)
			{
			count++;
			}
			else
			{
				break;
			}
		}
		l=count;
		
		count=0;
		
		for(long long j=y+1;j>0 && j<nstl+1;j++)
		{
			if(arngm[j]==0)
			{
			count++;
			}
			else
			{
				break;
			}
		}
		r=count;
		
		
	result<<"Case #"<<t+1<<": "<<max(l,r)<<" ";
	result<<min(l,r)<<"\n";
	
}
input.close();
result.close();
	return 0;
}

void mxm(long long arngm[],long long nstl)
{
	long long len=nstl+2;
	long long count=0,max_zeros=-1;
	
	for(long long p=0;p<len;p=p+count+1)
	{    count=0;
		for(long long s=p+1;s<len;s++)
		{
			if(arngm[s]==0)
			{
			count++;
			}
			else
			{
				if(max_zeros<count)
				{
				max_zeros=count;
				starta=p;
				enda=p+count+1;
			    }
				break;
			}
			
		}
		
	}
		
}
