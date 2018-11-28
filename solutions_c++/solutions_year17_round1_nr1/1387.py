#include"bits/stdc++.h"
#define fast ios_base::sync_with_stdio(false);cin.tie(0);
#define pb push_back
#define mp make_pair
#define ll long long int
#define vi vector<int>
#define vii vector<pair< int,int> >
#define pii pair<int,int>
#define plli pair<ll,ll>
#define ff first
#define ss second
#define MOD 1000000007
using namespace std;
int main()
{
	fast;
	int t=1,cases=1;
	cin>>t;
	while(t--)
	{
		int n,m;
		cin>>n>>m;
		char ch;
		string s[30];
		int i,j,k;
		for(i=0;i<n;i++)
		{
			cin>>s[i];
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(s[i][j]=='?')
				{
					ch='x';
					for(k=j;k>=0;k--)
					{
						if(s[i][k]!='?')
						{
							ch=s[i][k];
							break;
						}
					}
					if(ch!='x')
					{
						s[i][j]=ch;
					}
					else
					{
						for(k=j;k<m;k++)
						{
							
						if(s[i][k]!='?')
						{
						
							ch=s[i][k];
							break;
						}
						}
						if(ch!='x')
						{
						s[i][j]=ch;
						}
						}
				}
			}
		}			
		
		for(i=0;i<m;i++)
		{
			for(j=0;j<n;j++)
			{
				if(s[j][i]=='?')
				{
					ch='x';
					for(k=j;k>=0;k--)
					{
						if(s[k][i]!='?')
						{
							ch=s[k][i];
							break;
						}
					}
					if(ch!='x')
					{
						s[j][i]=ch;
					}
					else
					{
						for(k=j;k<n;k++)
						{
							
						if(s[k][i]!='?')
						{
						
							ch=s[k][i];
							break;
						}
						}
						if(ch!='x')
						{
						s[j][i]=ch;
						}
						}
				}
			}
		}				
					 
		cout<<"Case #"<<cases<<":"<<endl;
		cases++;
		for(i=0;i<n;i++)
		cout<<s[i]<<endl;
	}
	}