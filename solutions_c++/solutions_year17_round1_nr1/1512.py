#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int cas=1;cas<=t;cas++)
	{
		int r,c;
		cin>>r>>c;
		string a[r];
		for(int i=0;i<r;i++) cin>>a[i];
		int last_completed=-1;
		bool waiting=0;
		for(int i=0;i<r;i++)
		{
			int last=0;
			for(int j=0;j<c;j++)
			{
				if(a[i][j]!='?')
				{
					for(int jp=last;jp<j;jp++) a[i][jp]=a[i][j];
					last=j+1;
				}
			}
			if(a[i][c-1]=='?')
			{
				if(last==0)
				{
					if(last_completed!=-1)
					{
						a[i]=a[last_completed];
						last_completed=i;
					}
					else
					{
						waiting=1;
					}
				}
				else 
				{
					for(int jp=last;jp<c;jp++) a[i][jp]=a[i][last-1];
					last_completed=i;
				}
			}
			else last_completed=i;

			if(last_completed!=-1 && waiting)
			{
				waiting=0;
				for(int ip=0;ip<i;ip++) a[ip]=a[last_completed];
			}
		}
		 
		cout<<"Case #"<<cas<<":\n";
		for(int i=0;i<r;i++) 
		{
			cout<<a[i]<<'\n';
		}
		
	}
	return 0;
}
