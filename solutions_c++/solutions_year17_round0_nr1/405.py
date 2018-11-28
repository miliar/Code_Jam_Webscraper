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

		string s;
		int k;
		ifs >> s >> k;

		int ans = 0, n = s.length();
		REP(i,n-k+1){
			if (s[i] == '+') continue;
			ans++;
			FOR(j,i,i+k-1){
				if (s[j] == '+') s[j] = '-';
				else s[j] = '+';
			}
		}

		bool f = true;
		REP(i,n) if (s[i] == '-') f = false;

		if (f){
			cout << ans << endl;
			fprintf(fp, "%d\n", ans);
		}else{
			cout << "IMPOSSIBLE" << endl;
			fprintf(fp, "IMPOSSIBLE\n");
		}
	}

	return 0;
}