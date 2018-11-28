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

		int n, p;
		ifs >> n >> p;

		int ans = 0;
		VI a;
		REP(i,n){
			int x;
			ifs >> x;
			x %= p;
			if (x == 0) ans++;
			else a.push_back(x);
		}
		n = a.size();

		if (p == 2){
			ans += (n+1)/2;
		}else if (p == 3){
			int x = 0, y = 0;
			REP(i,n){
				if (a[i] == 1) x++;
				else y++;
			}
			int mi = min(x, y);
			ans += mi;
			x -= mi;
			y -= mi;
			ans += (x+2)/3;
			ans += (y+2)/3;
		}else{
			int x = 0, y = 0, z = 0;
			REP(i,n){
				if (a[i] == 1) x++;
				if (a[i] == 2) y++;
				if (a[i] == 3) z++;
			}
			ans += y/2;
			y %= 2;
			int mi = min(x, z);
			ans += mi;
			x -= mi;
			z -= mi;
			if (x == 0){
				if (y == 1 && z >= 2){
					ans++;
					z -= 2;
				}
				ans += (z+3)/4;
			}else{
				if (y == 1 && x >= 2){
					ans++;
					x -= 2;
				}
				ans += (x+3)/4;
			}
			if (y == 1) ans++;
		}

		cout << ans << endl;
		fprintf(fp, "%d\n", ans);
	}

	return 0;
}