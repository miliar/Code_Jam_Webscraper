#include<iostream>
#include<map>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n,k;
		cin>>n>>k;
		map<int,int,greater<int> > stall;
		stall[n]=1;
		int high=0,low=0;
		for(int j=0;j<k;j++)
		{
			map<int,int>:: iterator it;
			it=stall.begin();
			int x=it->first;
			if(x%2!=0)
			{
				if(stall.find(x/2)!=stall.end())	
				stall[x/2]=stall[x/2]+2;
				else
				stall[x/2]=2;
				high=low=x/2;
			}	
			else
			{
				if(stall.find(x/2)!=stall.end())	
				stall[x/2]=stall[x/2]+1;
				else
				stall[x/2]=1;
				if(stall.find(x/2-1)!=stall.end())	
				stall[x/2-1]=stall[x/2-1]+1;
				else
				stall[x/2-1]=1;
				high=x/2;
				low=(x/2)-1;
			}
			it=stall.begin();
			(it->second)--;
			if(it->second==0)
			stall.erase(it);
		}
		cout<<"Case #"<<i+1<<": "<<high<<" "<<low<<endl;
	}	
}












