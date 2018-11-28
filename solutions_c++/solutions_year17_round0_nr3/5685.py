#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<fstream>

using namespace std;
void maximum(long long arrangement[],long long noStalls);
long long starta,enda;

int main()
{
	ifstream input;
    input.open("input.txt",ios::in);
    ofstream result;
    result.open("result.txt",ios::out);
    
	int testCases;
	input>>testCases;
	
	for(int t=0;t<testCases;t++)
	{
	
	long long noStalls,noPeople,y;
	input>>noStalls>>noPeople;
    long long len=noStalls+2;
	long long arrangement[len];
	
	
	   arrangement[0]=1;
	   arrangement[noStalls+1]=1;	
		
		for(int i=1;i<noStalls+1;i++)
		{
			arrangement[i]=0;
		}
	
	
	
	for(int k=0;k<noPeople;k++)
	{
	    maximum(arrangement,noStalls);
		y=floor(((starta+1)+(enda-1))/2);
		arrangement[y]=1;	
	}
	long long l,r,count=0;
	
	for(long long j=y-1;j>0 && j<noStalls+1 ;j--)
		{
			if(arrangement[j]==0)
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
		
		for(long long j=y+1;j>0 && j<noStalls+1;j++)
		{
			if(arrangement[j]==0)
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

void maximum(long long arrangement[],long long noStalls)
{
	long long len=noStalls+2;
	long long count=0,max_zeros=-1;
	
	for(long long p=0;p<len;p=p+count+1)
	{    count=0;
		for(long long s=p+1;s<len;s++)
		{
			if(arrangement[s]==0)
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

