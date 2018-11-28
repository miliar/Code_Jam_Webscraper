#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
using namespace std;

pair<pair<int, int>, int> rangetoloc(pair<int, int> x)
{
	int idx = (x.first+x.second)/2;
	int a = abs(idx-x.first), b = abs(idx-x.second);
	return {{min(a, b), max(a, b)}, idx};
}

struct custom_cmp {
	bool operator()(pair<int, int> A, pair<int, int> B)
	{
		pair<pair<int, int>, int> x = rangetoloc(A), y = rangetoloc(B);
		if(x.first.first == y.first.first)
		{
			if(x.first.second == y.first.second) return (x.second < y.second);
			return (x.first.second > y.first.second);
		}
		return (x.first.first > y.first.first);
	}
};

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int tst = 1;tst <= t;tst++) {
	int n, k;
	scanf("%d%d", &n, &k);
	set<pair<int, int>, custom_cmp> S;
	S.insert({0, n-1});
	pair<int, int> last;
	for(int i = 0;i < k;i++)
	{
		pair<int, int> top = *S.begin();
		S.erase(S.begin());
		int mid = (top.first+top.second)/2;
		last = rangetoloc(top).first;
		//cout << top.first << " " << top.second << "\n";
		if(top.first <= mid-1) S.insert({top.first, mid-1});
		if(mid+1 <= top.second) S.insert({mid+1, top.second});
	}
	printf("Case #%d: %d %d\n", tst, last.second, last.first); }
}