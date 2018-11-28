#include <iostream>
#include <string>
#include <queue>
#include <fstream>
#include <set>
#include <algorithm>
#include <map>
using namespace std;



ifstream in("test.in");
ofstream out("test.out");
void solve1(__int64 n, __int64 k) {

	map<__int64, int> vis;
	map<__int64, __int64> total;

	map<__int64, __int64> l;
	map<__int64, __int64> r;
	set<__int64> q;
	q.insert(n);
	--k;
	__int64 cur = 0;
	r[n] = 1;
	total[n] = 1;
	while (!q.empty())
	{
		__int64 c = *(--q.end());
		q.erase(--q.end());
		l[c] = cur;
		cur += total[c];
		r[c] = cur;
		if (l[c] <= k && k < r[c]) {
			cout << c / 2 << " " << c / 2 - !(c % 2);
			out << c / 2 << " " << c / 2 - !(c % 2);

			return;
		}
			q.insert(c / 2);

			total[c / 2] += total[c];

			q.insert(c / 2 - !(c % 2));
			total[c / 2 - !(c % 2)] += total[c];


		

	}

}
void solve(__int64 n, __int64 k) {
	solve1(n, k);
}

int main() {
	int n;
	in >> n;

	for (int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ": ";

		out << "Case #" << i << ": ";
		
		__int64 N, k;
		in >> N >> k;
		solve(N, k);

		
		out << endl;
		cout << endl;
	}
	
	return 0;
}