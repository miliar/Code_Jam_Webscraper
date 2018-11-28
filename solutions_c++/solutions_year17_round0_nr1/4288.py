#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		string s;
		int x,j,k,count=0;
		cin>>s;
		cin>>k;
		x=k;
		int l=s.length();
		for(j=l-1;j>=0;j--)
		{
			if(s[j]=='-')
			{
				if(j-k+1>=0)
				{
					int y=j;
					while(x!=0)
					{
						if(s[y]=='-')
						s[y]='+';
						else s[y]='-';
						y--;
						x--;
					}
					count++;
					x=k;
				}
				else
				break;
			}
		}
		if(j==-1)
		cout<<"Case #"<<i+1<<": "<<count<<endl;
		else
		cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
	}
}
