#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long int ll;

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
#define present(c,e) ((c).find(e) != (c).end())
#define cpresent(c,e) (find(all(c),e) != (c).end())
#define REP(i,a,b) for(int i=int(a); i<=int(b); i++)
#define mp make_pair
#define ff first
#define ss second
#define PI 3.14159265359


struct pancake {
	int r, h;
};

pancake pans[1010];
double dp[1010][1010];
int N, K;

double csa(pancake &p) {
	return 2*PI*p.r*p.h;
}

double base(pancake &p) {
	return PI*p.r*p.r;
}

bool mycomp(const pancake &p1, const pancake &p2) {
	return ((p1.r > p2.r) || (p1.r==p2.r && p1.h >= p2.h));
}

double calculate (int i, int k) {
	if (dp[i][k] >= 0) {
		return dp[i][k];
	}
	if (i == 0) {
		return csa(pans[0])+base(pans[0]);
	}
	double answer;
	if (k > 1) {
		answer = max(calculate(i-1,k), calculate(i-1,k-1)+csa(pans[i]));
	}
	else {
		answer = max(calculate(i-1,k), base(pans[i])+csa(pans[i]));
	}
	dp[i][k] = answer;
	return answer;
}


int main() {
	int T;
	cin >> T;
	REP(caseno,1,T) {
		REP(i,0,1001) {
			REP(j,0,1001) {
				dp[i][j] = -1;
			}
		}
		cout << "Case #" << caseno << ": ";
		cin >> N >> K;
		REP(i,0,N-1) {
			cin >> pans[i].r >> pans[i].h;
		}
		sort(pans, pans+N, mycomp);
		printf("%.10lf\n", calculate(N-1,K));
	}
	return 0;
}