#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	long long i,x,T,pos;
	string N;
	cin>>T;
	for(x=1;x<=T;x++)
	{
		cin>>N;
		pos=-1;
		for(i=1;i<N.length();i++)
		{
			if(N[i]<N[i-1])
			{
				pos=i-1;
				break;
			}
		}
		if(pos!=-1)
		{
			for(i=0;i<N.length();i++)
			{
				if(N[i]==N[pos])
				{
					pos=i;
					break;
				}
			}
			N[pos]-=1;
			for(i=pos+1;i<N.length();i++)
			{
				N[i]='9';
			}
			for(i=0;i<N.length();i++)
			{
				if(N[i]!='0')
				{
					pos=i;
					break;
				}
			}
			cout<<"Case #"<<x<<": ";
			for(i=pos;i<N.length();i++)
			{
				cout<<N[i];
			}
			cout<<"\n";
		}
		else
		{
			cout<<"Case #"<<x<<": "<<N<<"\n";
		}
	}
	return 0;
}

