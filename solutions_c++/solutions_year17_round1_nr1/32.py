#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

string s[25];
int N,M;

void test(int tt)
{
	cin >> N >> M;
	for(int i=0;i<N;i++)
		cin >> s[i];
	for(int i=0;i<N-1;i++)
		for(int j=0;j<M;j++)
			if(s[i][j]!='?' && s[i+1][j]=='?')
				s[i+1][j] = s[i][j];
	for(int i=N-1;i>0;i--)
		for(int j=0;j<M;j++)
			if(s[i][j]!='?' && s[i-1][j]=='?')
				s[i-1][j] = s[i][j];
	for(int i=0;i<N;i++)
		for(int j=0;j<M-1;j++)
			if(s[i][j]!='?' && s[i][j+1]=='?')
				s[i][j+1] = s[i][j];
	for(int i=0;i<N;i++)
		for(int j=M-1;j>0;j--)
			if(s[i][j]!='?' && s[i][j-1]=='?')
				s[i][j-1] = s[i][j];
	cout << "Case #" << tt << ":\n";
	for(int i=0;i<N;i++)
		cout << s[i] << '\n';
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
		test(i);
}