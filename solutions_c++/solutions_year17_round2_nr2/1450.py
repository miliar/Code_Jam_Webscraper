#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

struct U {
	char color; int n;
};

bool cmp(U const& a, U const& b) {
	if (a.n == b.n)
		return a.color < b.color;

	return a.n > b.n;
}

string const solve(int N, int R, int O, int Y, int G, int B, int V)
{
	if (R > N/2 || Y > N/2 || B > N/2)
		return "IMPOSSIBLE";

	vector<U> st = {{'R', R}, {'Y', Y}, {'B', B}};

	sort(st.begin(), st.end(), cmp);
	string result(1, st[0].color);
	st[0].n -= 1;

	while(--N > 0) {
		sort(st.begin(), st.end(), cmp);
		if (st[0].n == 0)
			return result;

		int i = 0;
		if (st[0].color == result.back() || (N == 2 && st[1].color == result.front()))
			i = 1;

		result = result + st[i].color;
		st[i].n -= 1;
	}
	return result;
}

int main()
{
	int T; cin >> T;
	for(int x = 1; x <= T; ++x)
	{
		int N, R, O, Y, G, B, V;
		cin >> N >> R >> O >> Y >> G >> B >> V;
		cout << "Case #" << x << ": " << solve(N, R, O, Y, G, B, V) << endl;
	}
}