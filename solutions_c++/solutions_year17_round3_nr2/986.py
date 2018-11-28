#include <stdio.h>
#include <string.h>

#include <map>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

#define FOR(i,n) for(int i=0;i<(n);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define CLR(A,x) memset(A,(x),sizeof(A))

typedef long long LL;
typedef pair<int,int> pii;
int INT(){int x;scanf("%d",&x);return x;}

int span(pii x, pii y) {
	if (x.first<y.second)return y.second-x.first;
	return y.second+(24*60)-x.first;
	
}

int span(vector<pii> a) {
	return min(span(a[0], a[1]), span(a[1], a[0]));
}

int main() {
	int T=INT();
	for (int t=1;t<=T;++t) {
		int nC=INT();int nJ=INT();
		vector<pii> aC;
		FOR(i,nC){
			int st=INT();
			int en=INT();
			aC.push_back(pii(st,en));
		}
		vector<pii> aJ;
		FOR(i,nJ){
			int st=INT();
			int en=INT();
			aJ.push_back(pii(st,en));
		}

		int ans=0;
		if (nC+nJ<2){
			ans=2;
		} else if (nC==2) {
			if (span(aC) <= 12*60)ans=2; else ans=4;
		} else {
			if (span(aJ) <= 12*60)ans=2;else ans=4;
		}

		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
