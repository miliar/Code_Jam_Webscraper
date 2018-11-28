#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define Max(x,y,z) max(x,max(y,z))
#define Min(x,y,z) min(x,min(y,z))
#define fr(i,s,e) for(i=s;i<e;i++)
#define rf(i,s,e) for(i=s-1;i>=e;i--)
#define pb push_back
#define eb emblace_back
#define mp make_pair
#define ff first
#define ss second
#define ll long long
#define trace1(x)                cerr<<#x<<": "<<x<<endl
#define trace2(x, y)             cerr<<#x<<": "<<x<<" | "<<#y<<": "<<y<<endl
#define trace3(x, y, z)          cerr<<#x<<":" <<x<<" | "<<#y<<": "<<y<<" | "<<#z<<": "<<z<<endl
#define trace4(a, b, c, d)       cerr<<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<endl
#define trace5(a, b, c, d, e)    cerr<<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<" | "<<#e<< ": "<<e<<endl
#define trace6(a, b, c, d, e, f) cerr<<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<" | "<<#e<< ": "<<e<<" | "<<#f<<": "<<f<<endl
#define vl vector<long long>

#define vi vector<int> 
#define vii vector< vector<int> >
#define vll vector< vector<long long> >
#define vpi vector< pair<ll,ll> >  
vi lps;
void calclps(string s,int m)
{
	lps[0]=0;
	int len=0;
	for(int i=1;i<m;i++)
	{
		if(s[len]==s[i])
		{
			lps[i]=lps[i-1]+1;
			len++;
			
		}
		else
		{
			while(len>0)
			{
				len=lps[len-1];//suffix has to remain *same*...therefore we need to find some prefix which is the *same* suffix..which is the definition of lps
				if(s[len]==s[i])
				{
					lps[i]=len+1;
					len++;
					break;
				}
			}
			if(len==0)
			{
				lps[i]=0;
			}
		}
	}
}
int main()
{
	//IOS;
	freopen("A-large.in","r",stdin);
	freopen("optest1.txt","w",stdout);
	int t;
	cin>>t;
	int l=0;
	while(t--)
	{
		int r,c;
		cin>>r>>c;
		vector<vector<char> > v(r,vector<char>(c));
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
				cin>>v[i][j];
		}
		char cc;
		int prev=0;
		int prer=0;
		int prej=0;
		for(int i=0;i<r;i++)
		{
			cc='1';
			int prec=0;
			for(int j=0;j<c;j++)
			{
				if(v[i][j]=='?')
				{
					//if(c!='1')
					//	v[i][j]=c;
				}
				else
				{
					
					cc=v[i][j];
					for(int k=prer;k<=i;k++)
					{
						for(int l=0;l<=j;l++)
						{
						if(v[k][l]=='?')
							v[k][l]=cc;
							
						}
					}
					
				}
			}
			if(i==r-1)
			{
				if(cc!='1')
				{
					if(v[r-1][c-1]=='?')
					{
					for(int k=prer;k<=i;k++)
					{
						for(int l=0;l<=c-1;l++)
						{
						if(v[k][l]=='?')
							v[k][l]=cc;
							
						}
					}
					prer =i+1;
					//prej=j+1;
					
					}
				}
				else
				if(v[r-1][c-1]=='?')
				{
					for(int k=0;k<c;k++)
					{
						for(int l=prer;l<r;l++)
						{
							if(v[l][k]=='?')
								v[l][k]=v[prer-1][k];
						}
					}
				}
			}
			else
			if(v[i][c-1]=='?')
			{
				if(cc!='1')
				{
					for(int k=prer;k<=i;k++)
					{
						for(int l=0;l<=c-1;l++)
						{
						if(v[k][l]=='?')
							v[k][l]=cc;
							
						}
					}
					prer =i+1;
					//prej=j+1;
				}
			}
			else
				prer=i+1;
		}
		l++;
		cout<<"Case #"<<l<<": "<<endl;;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
				cout<<v[i][j];
				cout<<endl;
		}
	}
	return 0;
}
