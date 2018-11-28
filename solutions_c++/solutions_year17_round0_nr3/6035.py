#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <fstream>
#include <map>
#include <cmath>
#include <vector>
using namespace std;
vector<pair<int,int> > tree;
void dfs(int n)
{
	if(n==0) return;
	pair<int,int> tmp;
	int a,b;
	if(n%2==0)
	{
		a = n/2;
		dfs(a);
		b = n/2-1;
		dfs(b);
		tree.push_back(make_pair(a,b));
	}
	else
	{
		a = b = (n-1)/2;
		dfs(a);
		dfs(b);
		tree.push_back(make_pair(a,b));
	}
}
int main()
{
	fstream outfile,infile;
	infile.open("C-small-2-attempt1.in",ios::in);
	outfile.open("output.txt",ios::out);
	int cas,ansa,ansb;
	infile >> cas;
	for(int t=1;t<=cas;t+=1)
	{
		tree.clear();
		int n,k;
		infile >> n >> k;
		dfs(n);
		sort(tree.begin(),tree.end());
		reverse(tree.begin(),tree.end());
		// for(int i=0;i<tree.size();i++) cout << tree[i].first << ' ' << tree[i].second << endl;
		ansa=tree[k-1].first;
		ansb=tree[k-1].second;
		outfile << "Case #" << t << ": " << ansa << ' ' << ansb << endl;
	}

	return 0;
}