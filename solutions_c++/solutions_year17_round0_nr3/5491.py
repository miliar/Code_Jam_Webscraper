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
int N;
void update(int arr[],int right1[], int left1[], int index) {
	arr[index] = 1;
	int it = index-1;
	while (it > 0 && arr[it]==0) {
		right1[it] = index;
		it--;
	}
	it = index + 1;
	while (it < N && arr[it] == 0) {
		left1[it] = index;
		it++;
	}
}
string solve(int u, int v) {
	int right1[1010] = {0};
	int left1[1010] = {0};
	int arr[1010] = { 0 };
	memset(right1, -1, sizeof(right1));
	memset(left1, -1, sizeof(left1));
	arr[0] = 1;
	arr[u + 1] = 1;
	update(arr, right1, left1, 0);
	update(arr, right1, left1, u+1);

	N = u + 2;
	int ml = -(1 << 28);
	int mr = -(1 << 28);
	int mi;
	int l, r;

	for (int i = 0; i < v; i++) {
		ml = -(1 << 28);
		mr = -(1 << 28);
		for (int index = 0; index < N; index++) {
			if (arr[index] == 1)continue;
			l = index - left1[index]-1;
			r = right1[index] - index-1;
			if (min(l, r) > min(ml, mr) || (min(l, r) == min(ml, mr) && max(l, r) > max(ml, mr))) {
				mi = index;
				ml = l;
				mr = r;
			}
		}
		update(arr, right1, left1, mi);

	}
	stringstream ss;
	ss << max(ml,mr) <<' '<<min(ml,mr);
	return ss.str();
}
int main() {
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		int u, v;
		cin >> u >> v;
		cout << "Case #" << test << ": "<<solve(u,v)<<"\n";
	}
	return 0;
}