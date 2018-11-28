#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define ll long long int
#define nn 2001
#define inf -15000000000000ll
#define logn 21
#define ff first
#define se second
#define mod 1000000007ll
#define pdd pair<double,double>
#define db double
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pll pair<ll,ll>
#define mt make_tuple
using namespace std;
using namespace __gnu_pbds;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> OST;

char s[35][35];

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	ifstream fin;
	ofstream fout;
	fin.open("/home/nishant/Downloads/A-large.in");
	fout.open("/home/nishant/Downloads/loutputA.txt");
	int t;
	fin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		fout<<"Case #"<<tt<<":"<<endl;
		int r,c;
		fin>>r>>c;
		memset(s,0,sizeof s);
		for(int i=0;i<r;i++)
			fin>>s[i];
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(s[i][j]=='?')
					continue;
				int pj=j+1;
				while(pj<c && s[i][pj]=='?')
				{
					s[i][pj]=s[i][j];
					pj++;
				}
				pj=j-1;
				while(pj>=0)
				{
					if(s[i][pj]!='?')
						break;
					s[i][pj]=s[i][j];
					pj--;
				}
			}
		}
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(s[i][j]!='?')
					continue;
				char ch='?';
				int pi=i;
				while(pi>0 && s[pi][j]=='?')
					pi--;
				if(s[pi][j]!='?')
				{
					s[i][j]=s[pi][j];
					continue;
				}
				while(pi<r && s[pi][j]=='?')
					pi++;
				s[i][j]=s[pi][j];
			}
		}
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				fout<<s[i][j];
				assert(s[i][j]!='?');
			}
			fout<<endl;
		}
	}
	return 0;
}