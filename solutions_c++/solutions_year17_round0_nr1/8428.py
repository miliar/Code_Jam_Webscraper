#include<iostream>

using namespace std;

int main()
{
	int n;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		char st[2000]={'+'};	
		int k;
		int plus=0;
		bool chk=false;
		cin>>st;
		cin>>k;
		for(int j=0;j<strlen(st);j++)
		{
			if(st[j]=='-')
			{
				plus++;
				for(int a=j;a<j+k;a++)
				{
					if(j+k>strlen(st))
						break;
					if(st[a]=='-')
						st[a]='+';
					else
						st[a]='-';
				}
			}
		}
		for(int r=0;r<strlen(st);r++)
		{
			if(st[r]=='-')
				chk=true;
		}
		if(chk==false)
			cout<<"Case #"<<i+1<<": "<<plus<<endl;
		else		
		cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
	}
}