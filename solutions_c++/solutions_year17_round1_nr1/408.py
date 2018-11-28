#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <sstream>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

#define MP make_pair
#define PB push_back
typedef long long LL;

string testfile = "A-large";

const int MAXN = 30;

int N,M;
string S[MAXN];

void expand_LR(int a,int b) {
	for (int i = b-1; i>=0; --i)
		if (S[a][i]=='?') S[a][i] = S[a][b];
		else break;
	for (int i = b+1; i<M; ++i)
		if (S[a][i]=='?') S[a][i] = S[a][b];
		else break;
}

void expand(int a,int l) {
	int r = l;
	while (r+1<M && S[a][r+1]==S[a][l]) ++r;
	for (int i = a-1; i>=0; --i) {
		bool flag = true;
		for (int k = l; k<=r && flag; ++k)
			flag &= (S[i][k]=='?');
		if (flag) {
			for (int k = l; k<=r && flag; ++k)
				S[i][k] = S[a][l];
		}
		else break;
	}
	for (int i = a+1; i<N; ++i) {
		bool flag = true;
		for (int k = l; k<=r && flag; ++k)
			flag &= (S[i][k]=='?');
		if (flag) {
			for (int k = l; k<=r && flag; ++k)
				S[i][k] = S[a][l];
		}
		else break;
	}
}

void run() {
	cin>>N>>M;
	for (int i = 0; i<N; ++i)
		cin>>S[i];
	for (int i = 0; i<N; ++i) {
		for (int j = 0; j<M; ++j) {
			if (S[i][j]!='?') {
				expand_LR(i,j);
			}
		}
	}
	for (int i = 0; i<N; ++i) {
		for (int j = 0; j<M; ++j)
			if (S[i][j]!='?')
				expand(i,j);
	}
	cout<<endl;
	for (int i = 0; i<N; ++i)
		cout<<S[i]<<endl;
}

int main() {
	freopen((testfile+".in").c_str(),"r",stdin);
	freopen((testfile+".out").c_str(),"w",stdout);
	int testn;
	cin>>testn;
	for (int loop = 1; loop<=testn; ++loop) {
		cout<<"Case #"<<loop<<": ";

		run();
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
