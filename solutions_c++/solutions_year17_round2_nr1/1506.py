#include<iostream>
#include<iomanip>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<set>

#define Author "DemoVersion"
#define DBG(x) cout<<#x<<" = "<<x<<";\n"


using namespace std;
int dx[] = { 0,0,-1,1,1,-1,1,-1 };
int dy[] = { 1,-1,0,0,1,1,-1,-1 };
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
double solve() {

	int D, N;
	double s, q,t;
	double max_time = 0.00000001;
	cin >> D >> N;
	for (int i = 0; i < N;i++) {
		cin >> s >> q;
		t = (D - s) / q;
		max_time = max(t, max_time);
	}
	return (double)D / max_time;
}
int main() {
	ios_base::sync_with_stdio(0);
	int T; cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #"<<i<<": " <<setprecision(10)<<fixed<<solve()<< endl;
	}
	return 0;
}