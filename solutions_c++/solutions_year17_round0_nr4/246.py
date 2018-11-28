/*
*/

#pragma GCC optimize("O3")
#define _CRT_SECURE_NO_WARNINGS
#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <list>
#include <ctime>

#include <memory.h>
#include <assert.h>

#define y0 sdkfaslhagaklsldk

#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
#define norm asdfasdgasdgsd
#define have adsgagshdshfhds
#define ends asdgahhfdsfshdshfd

#define eps 1e-12
#define M_PI 3.141592653589793
#define bs 1000000007
#define bsize 200

#define ldouble long double

using namespace std;

long long INF = 1e9;
const int N = 500031;

int tests,n,k,board[131][131][3];
int memo_board[131][131][3];
int have1[800],have2[800];
int mt[N];
vector<int> g[N];
int used[N];

bool try_kuhn(int v)
{
	if (used[v])
		return false;
	used[v]=1;
	for (int i=0;i<g[v].size();i++)
	{
		int to=g[v][i];
		if (mt[to]==-1||try_kuhn(mt[to]))
		{
			mt[to]=v;
			return 1;
		}
	}
	return 0;
}

bool outside(pair<int,int> p){
	return (p.first<1||p.first>n||p.second<1||p.second>n);
}

pair<int,int> solver(int a,int b){
	// x-y+n=a,x+y=b

	int x2=a+b-n;
	if (x2%2)
		return make_pair(-1,-1);
	int X=x2/2;
	int Y=b-X;
	return make_pair(X,Y);
}

int ts;
vector<pair<int,pair<int,int> > > ans;
string SS;

int main(){
	//freopen("tree.in","r",stdin);
	//freopen("tree.out","w",stdout);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	//cin.tie(0);

	SS=".x+o";

	cin>>tests;
	for (;tests;--tests)
	{
		cin>>n;
		cin>>k;
		for (int i=0;i<=n;i++)
		{
			for (int j=0;j<=n;j++)
			{
				board[i][j][0]=0;
				board[i][j][1]=0;
			}
		}

		for (int i=1;i<=k;i++)
		{
			string temp;
			int a,b;
			cin>>temp>>a>>b;
			if (temp=="o"||temp=="x")
			{
				board[a][b][0]=1;
			}
			if (temp=="o"||temp=="+")
			{
				board[a][b][1]=1;
			}
		}

		for (int i=1;i<=n;i++)
		{
			for (int j=1;j<=n;j++)
			{
				memo_board[i][j][0]=board[i][j][0];
				memo_board[i][j][1]=board[i][j][1];
			}
		}

		// vertical + horizontal

		for (int i=1;i<=n;i++)
		{
			have1[i]=have2[i]=0;
		}

		for (int i=1;i<=n;i++)
		{
			for (int j=1;j<=n;j++)
			{
				if (board[i][j][0])
				{
					have1[i]=1;
					have2[j]=1;
				}
			}
		}

		for (int i=1;i<=n;i++)
		{
			g[i].clear();
		}

		for (int i=1;i<=n;i++)
		{
			mt[i]=-1;
			for (int j=1;j<=n;j++)
			{
				if (have1[i]==0&&have2[j]==0)
				{
					g[i].push_back(j);
				}
			}
		}

		for (int i=1;i<=n;i++)
		{
			for (int j=1;j<=n;j++)
			{
				used[j]=0;
			}
			try_kuhn(i);
		}

		for (int i=1;i<=n;i++)
		{
		//	cout<<mt[i]<<" ";
			if (mt[i]!=-1)
			{
				int to=mt[i];
				board[to][i][0]=1;
			}
		}


		for (int i=1;i<=n*4;i++)
		{
			mt[i]=-1;
			g[i].clear();
			have1[i]=0;
			have2[i]=0;
		}

		for (int i=1;i<=n;i++)
		{
			for (int j=1;j<=n;j++)
			{
				if (board[i][j][1]==0)
					continue;
				have1[i-j+n]=1;
				have2[i+j]=1;
			}
		}

		for (int i=1;i<=n*4;i++)
		{
			for (int j=1;j<=n*4;j++)
			{
				if (have1[i]||have2[j])
					continue;
				pair<int,int>p=solver(i,j);
				//cout<<p.first<<"%"<<p.second<<endl;
				if (outside(p))
					continue;
			//	cout<<p.first<<" "<<p.second<<" "<<i<<" "<<j<<endl;

				g[i].push_back(j);
			}
		}

		for (int i=1;i<=n*4;i++)
		{
			for (int j=1;j<=n*4;j++)
			{
				used[j]=0;
			}
			try_kuhn(i);
		}

		for (int i=1;i<=n*4;i++)
		{
			if (mt[i]!=-1)
			{
				//cout<<"@@"<<endl;
				int to=mt[i];
				pair<int,int> p=solver(to,i);
//				cout<<p.first<<"%%"<<p.second<<" "<<i<<" "<<to<<endl;
				board[p.first][p.second][1]=1;
			}
		}

		int score=0;

		for (int i=1;i<=n;i++)
		{
			for (int j=1;j<=n;j++)
			{
				score+=board[i][j][0]+board[i][j][1];
			}
		}

		++ts;
		cout<<"Case #"<<ts<<": ";
		cout<<score<<" ";
		ans.clear();
		for (int i=1;i<=n;i++)
		{
			for (int j=1;j<=n;j++)
			{
				if (board[i][j][0]!=memo_board[i][j][0]||board[i][j][1]!=memo_board[i][j][1])
				{
					int here=0;
					if (board[i][j][0])
						here+=1;
					if (board[i][j][1])
						here+=2;
					ans.push_back(make_pair(here,make_pair(i,j)));
				}
			}
		}

		cout<<ans.size()<<endl;
		for (int i=0;i<ans.size();i++)
		{
			cout<<SS[ans[i].first]<<" "<<ans[i].second.first<<" "<<ans[i].second.second<<endl;
		}

	}

	cin.get(); cin.get();
	return 0;
}
