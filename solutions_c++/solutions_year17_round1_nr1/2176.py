//https://code.google.com/codejam/contest/5304486/dashboard
#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	 freopen("A-largeoutput-.txt","w",stdout);
	int tp;
	cin>>tp;
	for(int t=1;t<=tp;t++)
	{
		int l,r,c;
		cin>>r>>c;
	//	string a[r][c];
		string a[r];
		int b[r][c];
		for(int i=0;i<r;i++)
		//for(int j=0;j<c;j++)
		{
		//	b[i][j]=0;
			cin>>a[i];
			for(int k=0;k<c;k++)
			{
					b[i][k]=0;
				if(a[i][k]!='?')
			{
				b[i][k]=1;
			}
			}
		}
		for(int i=0;i<r;i++)
		for(int j=0;j<c;j++)
		{
			if(b[i][j]==1)
			{
			//	cout<<"vijay\n";
				int k=j+1,right,left;
				while(a[i][k]=='?'&&k<c)
				{
				//	cout<<"pratap\n";
					a[i][k]=a[i][j];
					//if(i==0)
					//cout<<a[i][k]<<"  ";
					k++;
				}
				//cout<<"\n";
				right=k-1;
			    k=j-1;
				while(a[i][k]=='?'&&k>=0)
				{
					a[i][k]=a[i][j];
					k--;
				}
				left=k+1;
				for(int h=i-1;h>=0;h--)
				{
					bool fill=true;
					for(int f=left;f<=right;f++)
					{
						if(a[h][f]!='?')
						{
							fill=false;
							break;
						}
					}
					if (fill==false)
					break;
					else {
						for(int f=left;f<=right;f++)
						a[h][f]=a[i][j];
					}
				}
				
				for(int h=i+1;h<r;h++)	
					{
							bool fill=true;
						for(int f=left;f<=right;f++)
					{
						if(a[h][f]!='?')
						{
							fill=false;
							break;
						}
					}
					  if (fill==false)
					break;
					else {
						for(int f=left;f<=right;f++)
						a[h][f]=a[i][j];
					}
					}
			}
		}
		
		cout<<"Case #"<<t<<":\n";
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				cout<<a[i][j];
			}
			cout<<"\n";
		}
		
		
		
		
		
	}
}
