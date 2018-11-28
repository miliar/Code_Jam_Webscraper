#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

typedef long long ll;

FILE* streamOut = stdout;
FILE* streamIn = stdin;

pair<ll, ll> ans;
multiset<ll> buffer;

pair<ll, ll> solveBruteForce(ll n, ll k)
{
	if (n == -1 && k == -1)
		fscanf(streamIn, "%I64d %I64d", &n, &k);

	buffer.clear();
	buffer.insert(n);

	ll cur;
	while (k--)
	{
		cur = *buffer.rbegin();

		auto it = buffer.find(cur);
		buffer.erase(it);
		buffer.insert((cur - 1) / 2);
		buffer.insert(cur / 2);
		ans = { cur / 2, (cur - 1) / 2 };
	}
	fprintf(streamOut, "%I64d %I64d\n", ans.first, ans.second);

	return ans;
}

pair<ll, ll> solve(ll n, ll k)
{
	return make_pair(0, 0);
}

int main()
{
	fopen_s(&streamIn, "input.txt", "r");
	fopen_s(&streamOut, "output.txt", "w");

	int TC;
	fscanf(streamIn, "%d", &TC);
	for (int i = 1; i <= TC; ++i) {
		fprintf(streamOut, "Case #%d: ", i);
		solveBruteForce(-1, -1);
	}

	return 0;
}