#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	int t,z;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		int r,c,i,j,k;
		cin>>r>>c;
		string mat[r];
		for(i=0;i<r;i++)
			cin>>mat[i];
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(mat[i][j]!='?')
				{
					for(k=i-1;k>=0;k--)
					{
						if(mat[k][j]=='?')
							mat[k][j]=mat[k+1][j];
						else break;
					}
					for(k=i+1;k<r;k++)
					{
						if(mat[k][j]=='?')
							mat[k][j]=mat[k-1][j];
						else break;
					}
				}
			}
		}
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(mat[i][j]!='?')
				{
					for(k=j-1;k>=0;k--)
					{
						if(mat[i][k]=='?')
							mat[i][k]=mat[i][k+1];
						else break;
					}
					for(k=j+1;k<c;k++)
					{
						if(mat[i][k]=='?')
							mat[i][k]=mat[i][k-1];
						else break;
					}
				}
			}
		}
		cout<<"Case #"<<z<<":\n";
		for(i=0;i<r;i++)
			cout<<mat[i]<<endl;
		
	}
}