#include<bits/stdc++.h>
using namespace std;
long long t,tt,n,m,i,j;
bool b;
char c[101][101];
void kiri(long long ki, long long kj)
{
	char cc=c[ki][kj];
	kj--;
	while(kj>=1&&c[ki][kj]=='?')
	{
		c[ki][kj]=cc;
		kj--;
	}
}
void kanan(long long ki, long long kj)
{
	char cc=c[ki][kj];
	kj++;
	while(kj<=m&&c[ki][kj]=='?')
	{
		c[ki][kj]=cc;
		kj++;
	}
}
void atas(long long ki, long long kj)
{
	char cc=c[ki][kj];
	ki--;
	while(ki>=1&&c[ki][kj]=='?')
	{
		c[ki][kj]=cc;
		ki--;
	}
}
void bawah(long long ki, long long kj)
{
	char cc=c[ki][kj];
	ki++;
	while(ki<=n&&c[ki][kj]=='?')
	{
		c[ki][kj]=cc;
		ki++;
	}
}
int main()
{
	freopen("r1a17in.txt","r",stdin);
	freopen("r1a17out.txt","w",stdout);
	cin>>t;
	while(t--)
	{
		tt++;
		cin>>n>>m;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				cin>>c[i][j];
			}
		}
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				b=0;
				if(c[i][j]!='?'&&b==0)
				{
					b=1;
					kiri(i,j);
					kanan(i,j);
				}
				else
				if(c[i][j]!='?')
				{
					kanan(i,j);
				}
			}
		}
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				b=0;
				if(c[i][j]!='?'&&b==0)
				{
					b=1;
					atas(i,j);
					bawah(i,j);
				}
				else
				if(c[i][j]!='?')
				{
					atas(i,j);
				}
			}
		}
		printf("Case #%lld:\n",tt);
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				cout<<c[i][j];
			}
			cout<<endl;
		}
	}
}
