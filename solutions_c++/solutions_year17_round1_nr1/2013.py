#include <iostream>

using namespace std;

int t;
int r, c;
char f[27][27];
int k, j;
char akt;

int main()
{
	cin>>t;
	for(int i=1; i<=t; i++)
	{
		cin>>r>>c;
		for(int j=1; j<=r; j++)
		{
			for(int k=0; k<c; k++)
			{
				cin>>f[k][j];
			}
		}
		
		for(int j=1; j<=r; j++)
		{
			k=0;
			while(f[k][j] == '?')k++;
			
			if(k != c)
			{
				akt = f[k][j];	
				for(int k=0; k<c; k++)
				{
					if(f[k][j] != '?')
						akt = f[k][j];
					f[k][j] = akt;
				}
			}
			else
			{
				for(int k=0; k<c; k++)
				{
					if(f[k][j] != '?')
						akt = f[k][j];
					f[k][j] = f[k][j-1];
				}
			}
		}
		j=r;
		k=0;
		while(f[k][j] != (char)0 && j>0)j--;
		
		for(; j>0; j--)
			for(int k=0; k<c; k++)
				f[k][j] = f[k][j+1];
		
		
		cout<<"Case #"<<i<<": ";
		cout<<endl;
		
		for(int j=1; j<=r; j++)
		{
			for(int k=0; k<c; k++)
			{
				cout<<f[k][j];
			}
			cout<<endl;
		}
		for(int j=0; j<=r; j++)
		{
			for(int k=0; k<c; k++)
			{
				f[k][j] =(char)0 ;
			}
		}
		
	}
	return 0;
}
