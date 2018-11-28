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

string testfile = "B-large";

const int MAXN = 50+5;
const int MAXP = 50+5;

int N,P;
int S[MAXN];
int g[MAXN][MAXP],p[MAXN];

void run() {
	cin>>N>>P;
	for (int i = 0; i<N; ++i) {
		cin>>S[i];
	}
	for (int i = 0; i<N; ++i) {
		for (int j = 0; j<P; ++j) {
			cin>>g[i][j];
		}
		sort(g[i],g[i]+P);
	}
	memset(p,0,sizeof(p));
	int serve = 1;
	int ans = 0;
	while (true) {
		bool flag = true;
		//printf("serves %d\n",serve);
		for (int i = 0; i<N; ++i) {
			double L = 0.9*serve*S[i];
			double R = 1.1*serve*S[i];
			//cout<<L<<' '<<R<<endl;
			while (p[i]<P && L>g[i][p[i]]) {
				//printf("p[%d] = %d, g[i][p[i]]=%d\n",i,p[i],g[i][p[i]]);
				++p[i];
			}
			if (p[i]<P && g[i][p[i]]<=R);
			else flag = false;
		}
		if (!flag) ++serve;
		else {
			++ans;
			for (int i = 0; i<N; ++i)
				++p[i];
		}

		bool end = false;
		for (int i = 0; i<N; ++i)
			if (p[i]>=P) {
				end = true;
				break;
			}
		if (end) break;
	}
	cout<<ans<<endl;
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
