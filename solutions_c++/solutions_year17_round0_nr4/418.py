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

		int n, m;
		ifs >> n >> m;
		VVI a(n,VI(n));
		int ci = -1, cj = -1;
		map<char, int> mp;
		mp['+'] = 1;
		mp['x'] = 2;
		mp['o'] = 3;
		REP(x,m){
			char c;
			int i, j;
			ifs >> c >> i >> j;
			i--;
			j--;
			a[i][j] = mp[c];
			if (c == 'o'){
				ci = i;
				cj = j;
			}
		}

		VI ansx, ansy;
		vector<char> ansc;

		REP(j,n){
			if (a[0][j] == 2){
				a[0][j] = 3;
				ci = 0;
				cj = j;
				ansx.push_back(0);
				ansy.push_back(j);
				ansc.push_back('o');
			}
		}

		if (ci == -1){
			a[0][n-1] = 3;
			ansx.push_back(0);
			ansy.push_back(n-1);
			ansc.push_back('o');
			ci = 0;
			cj = n-1;
		}

		REP(j,n){
			if (a[0][j] == 0){
				a[0][j] = 1;
				ansx.push_back(0);
				ansy.push_back(j);
				ansc.push_back('+');
			}
		}

		FOR(i,1,n-1){
			int j = cj + i;
			ansx.push_back(i);
			ansc.push_back('x');
			if (j >= n) j = n - i - 1;
			ansy.push_back(j);
			a[i][j] = 2;
		}

		FOR(j,1,n-2){
			a[n-1][j] = 1;
			ansx.push_back(n-1);
			ansy.push_back(j);
			ansc.push_back('+');
		}

		int score = 3*n-2;
		if (n == 1){
			score = 2;
		}

		cout << score << " " << ansx.size() << endl;
		fprintf(fp, "%d %d\n", score, (int)ansx.size());
		REP(i,ansx.size()){
			cout << ansc[i] << " " << ansx[i]+1 << " " << ansy[i]+1 << endl;
			fprintf(fp, "%c %d %d\n", ansc[i], ansx[i]+1, ansy[i]+1);
		}
	}

	return 0;
}