#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <math.h>
#include <stdio.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int I=1;I<=T;I++)
	{
		cout << "Case #" << I << ": ";
		int n,c,m;
		cin >> n >> c >> m;
		vector<vector<int> > v(c,vector<int>(n));
		for(int i=0;i<m;i++)
		{
			int a,b;
			cin >> a >> b;
			v[b-1][a-1]++;
		}
		if(c==2)
		{
			int ntr=0;
			int nasc=0;
			for(int i=0;i<n;i++)
			{
				for(int j=i+1;j<n;j++)
				{
					if(v[0][j]&&v[1][j]){
					int asdf = min(v[0][i],v[1][j]);
					ntr+=asdf;
					v[0][i]-=asdf;
					v[1][j]-=asdf;}
				}
				for(int j=i+1;j<n;j++)
				{
					int asdf = min(v[0][i],v[1][j]);
					ntr+=asdf;
					v[0][i]-=asdf;
					v[1][j]-=asdf;
				}
			}
			for(int i=0;i<n;i++)
			{
				for(int j=i+1;j<n;j++)
				{
					if(v[0][j]&&v[1][j]){
					int asdf = min(v[0][j],v[1][i]);
					ntr+=asdf;
					v[0][j]-=asdf;
					v[1][i]-=asdf;}
				}
				for(int j=i+1;j<n;j++)
				{
					int asdf = min(v[0][j],v[1][i]);
					ntr+=asdf;
					v[0][j]-=asdf;
					v[1][i]-=asdf;
				}
			}
			for(int i=1;i<n;i++)
			{
				int asdf = min(v[0][i],v[1][i]);
				ntr+=asdf;
				nasc+=asdf;
				v[0][i]-=asdf;
				v[1][i]-=asdf;
			}
			for(int i=0;i<n;i++)
				ntr+=v[0][i]+v[1][i];
			cout << ntr << " " << nasc << endl;
		}
	}
}
