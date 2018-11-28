#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<cassert>
using namespace std;

#define LL long long
#define PII pair<int,int>
#define x first
#define y second
#define mkp(a,b) make_pair(a,b)

int opt[26][26][26][26];
int chs[26][26][26][26], typ[26][26][26][26];
int n, m;
char S[30][30];
int ind[256];
int X[26],Y[26], k;

void go(int x1, int x2, int y1, int y2, vector<PII > p) {
	if(p.size()==1){
		for(int i=x1;i<=x2;++i)
			for(int j=y1;j<=y2;++j)
				S[i][j]=S[p[0].x][p[0].y];
		return ;
	}
	set<int> X,Y;
	for(int i=0;i<p.size();++i) {
		X.insert(p[i].x);
		Y.insert(p[i].y);
	}
	// do x
	vector<PII > L, R;
	for(auto x: X) {
		L.clear();R.clear();
		for(int i=0;i<p.size();++i)
			if (p[i].x <= x) L.push_back(p[i]);
			else R.push_back(p[i]);
		if (L.size()>0 && R.size()>0) {
			go(x1, x, y1, y2, L);
			go(x+1, x2, y1, y2, R);
			return ;
		}
		break;
	}
	
	// do y
	for(auto y: Y) {
		L.clear();R.clear();
		for(int i=0;i<p.size();++i)
			if (p[i].y <= y) L.push_back(p[i]);
			else R.push_back(p[i]);
		if (L.size()>0 && R.size()>0) {
			go(x1, x2, y1, y, L);
			go(x1, x2, y+1, y2, R);
			return ;
		}
		break;
	}
	
	assert(false);
}

int run() {
	scanf("%d %d", &n, &m);
	memset(opt,-1,sizeof(opt));
	k = 0;
	vector<PII > P;
	for(int i=0;i<n;++i){
		scanf("%s",S[i]);
		for(int j=0;j<m;++j){
			if(isupper(S[i][j]))
				P.push_back(mkp(i,j));
		}
	}
	go(0,n-1,0,m-1,P);
	for(int i=0;i<n;++i)
		printf("%s\n",S[i]);
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	cin >>T;
	for (int i=1;i<=T;++i) {
		printf("Case #%d:\n", i);
		run();
	}
}
