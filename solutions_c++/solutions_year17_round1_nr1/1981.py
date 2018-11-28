#include<iostream>
#include<algorithm>
#include<limits>
#include<vector>
#include<cmath>
#include<bitset>
#include<map>
#include<stdio.h>
#include <iomanip>


using namespace std;

typedef long long ll;
typedef long double ld;

int main()
{

	int t;
	cin>>t;
	int t2=t;
	while(t)
	{
		int r,c;
		cin>>r>>c;
		char c3[r][c],c2[r][c];
		int i,cnt=0;
		int v[r][c];
		for(i=0;i<r;i++)
		{
			fill_n(v[i],c,0);
		}
		for(i=0;i<r;i++)
		{
			int j;
			for(j=0;j<c;j++)
			{
				cin>>c3[i][j];
				c2[i][j]=c3[i][j];
				if(c3[i][j]=='?')
				{
					cnt++;
				}
			}
		}
		int cnt2=0;
		for(i=0;i<r;i++)
		{
			int j;
			for(j=0;j<c;j++)
			{
				if(c2[i][j]!='?')
				{
					int k;
					int l=j,h=j;
					for(k=j+1;k<c;k++)
					{
						if(c2[i][k]!='?' || v[i][k]!=0 )
						{
							break;
						}
						v[i][k]=1;
						c3[i][k]=c2[i][j];
						h++;
					}
					for(k=j-1;k>=0;k--)
					{
						if(c2[i][k]!='?' || v[i][k]!=0)
						{
							break;
						}
						v[i][k]=1;
						c3[i][k]=c2[i][j];
						l--;
					}
					//cout<<"l: "<<l<<" h: "<<h<<endl;
					for(k=i-1;k>=0;k--)
					{
						int k2;
						int flag=0;
						for(k2=l;k2<=h;k2++)
						{
							if(c2[k][k2]!='?' || v[k][k2]!=0)
							{
								flag=1;
								break;
							}
						}
						if(flag==1)
						{
							break;
						}
						else
						{
							for(k2=l;k2<=h;k2++)
							{
								v[k][k2]=1;
								c3[k][k2]=c2[i][j];
							}
						}
					}
					for(k=i+1;k<r;k++)
					{
						int k2;
						int flag=0;
						for(k2=l;k2<=h;k2++)
						{
							if(c2[k][k2]!='?' || v[k][k2]!=0)
							{
								flag=1;
								break;
							}
						}
						if(flag==1)
						{
							break;
						}
						else
						{
							for(k2=l;k2<=h;k2++)
							{
								v[k][k2]=1;
								c3[k][k2]=c2[i][j];
							}
						}
					}
					
					
				}
			}
		}
		cout<<"Case #"<<t2-t+1<<":"<<endl;
		for(i=0;i<r;i++)
		{
			int j;
			for(j=0;j<c;j++)
			{
				cout<<c3[i][j];
			}
			cout<<endl;
		}
		
		t--;
	}

	return 0;
}

