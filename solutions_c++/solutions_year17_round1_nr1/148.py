#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i=0; i<n; ++i)
#define FOR(i,a,b) for(int i=a; i<=b; ++i)
#define FORR(i,a,b) for (int i=a; i>=b; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long ll;
typedef vector<int> VI;
typedef vector<ll> VL;
typedef vector<VI> VVI;
typedef pair<int,int> P;
typedef pair<ll,ll> PL;

int main(void) {
	ifstream ifs("input.txt");
	ofstream ofs("out.txt");
	FILE *fp;
	fp = fopen("out.txt","w");
	int num_of_cases;
	ifs >> num_of_cases;
	REP(cas,num_of_cases){
		fprintf(fp,"Case #%d: ",cas+1);
		printf("Case #%d: ",cas+1);

		fprintf(fp, "\n");
		cout << endl;

		int r, c;
		ifs >> r >> c;
		vector<string> s(r);
		REP(i,r) ifs >> s[i];
		int x = 0;
		REP(i,r){
			vector<pair<char,int> > v;
			REP(j,c) if (s[i][j] != '?') v.push_back(make_pair(s[i][j], j));
			if (v.empty()) continue;
			REP(k,v.size()){
				char ch = v[k].first;
				int p, q;
				if (k == 0) p = 0;
				else p = v[k].second;
				if (k == v.size()-1) q = c-1;
				else q = v[k+1].second-1;
				FOR(ii,x,i) FOR(jj,p,q) s[ii][jj] = ch;
			}
			x = i+1;
		}
		REP(j,c) FOR(i,x,r-1) s[i][j] = s[x-1][j];
		REP(i,r) cout << s[i] << endl;
		REP(i,r) fprintf(fp, "%s\n", s[i].c_str());
	}

	return 0;
}