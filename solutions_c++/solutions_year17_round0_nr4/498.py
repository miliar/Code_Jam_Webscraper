#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
static int sum=0;
static int count1=0;
static vector<pair<char,ii> > solve1(int n,int m,vector<ii> plus,vector<ii> mul)
{
	vector<vector<int> > board(n,vector<int>(n));//.,+,x,o
	vector<bool> visited(n);
	for(int i=0;i<plus.size();i++)
		board[plus[i].first][plus[i].second]++;
	bool line=false;
	for(int i=0;i<mul.size();i++)
	{
		board[mul[i].first][mul[i].second]+=2;
		visited[mul[i].second]=true;
		line=true;
	}
	vector<pair<char,ii> > res(0);
	sum=plus.size()+mul.size();
	count1=0;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			bool check1=false;
			bool check2=false;
			if(i==0&&board[i][j]%2==0)
				check1=true;
			if(i==n-1&&j>0&&j<n-1)
				check1=true;
			if(!visited[j]&&!line)
			{
				visited[j]=true;
				line=true;
				check2=true;
			}
			if(check2&&check1)
			{
				sum+=2;
				count1++;
				res.push_back(pair<char,ii>('o',ii(i+1,j+1)));
				continue;
			}
			if(check1|check2)
			{
				sum++;
				count1++;
				char cer='o';
				if(board[i][j]==0)
				{
					cer='x';
					if(check1)
						cer='+';
				}
				res.push_back(pair<char,ii>(cer,ii(i+1,j+1)));
			}
		}
		line=false;
	}
	return res;
	//.,+,x,o,
}
int main()
{
	ofstream fout;
	ifstream fin;
	fout.open("output.txt");
	fin.open("D-small-attempt0.in");
	ll t;
	fin >> t;
	for(int i=0;i<t;i++)
	{
		int n,m;
		fin >> n >> m;
		vector<ii> plus(0);
		vector<ii> mul(0);
		for(int j=0;j<m;j++)
		{
			char c;
			fin >> c;
			int ri,ci;
			fin >> ri >> ci;
			if(c=='+'||c=='o')
				plus.push_back(ii(ri-1,ci-1));
			if(c=='x'||c=='o')
				mul.push_back(ii(ri-1,ci-1));
		}
		vector<pair<char,ii> > res=solve1(n,m,plus,mul);
		fout << "Case #" << i+1 << ": ";
		fout << sum << " " << count1 << endl;
		for(int i=0;i<res.size();i++)
		{
			fout << res[i].first << " " << res[i].second.first << " " << res[i].second.second << endl;
		}
	}
}