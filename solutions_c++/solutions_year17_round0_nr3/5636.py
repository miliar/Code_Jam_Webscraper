#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <string>
#include <stack>
#include <set>
#include <assert.h>
#include <queue>


using namespace std;

FILE *fp;

#define READ                  freopen_s(&fp,"input.txt", "r", stdin);
#define WRITE                 freopen_s(&fp,"output.txt", "w", stdout);

pair<uint64_t,uint64_t> solve(uint64_t n, uint64_t k)
{
	priority_queue<uint64_t> q;
	q.push(n);
	if (k == n) return pair<uint64_t,uint64_t>(0,0);
	uint64_t ls = 0;
	uint64_t rs = 0;
	for (uint64_t i = 0; i < k; ++i)
	{

		ls = q.top() / 2;
		if ((q.top() % 2) == 0) ls--;

		rs = q.top() / 2;
		q.pop();
		q.push(ls), q.push(rs);
	}

	return pair<uint64_t, uint64_t>(rs, ls);
}


int main(int argc, char* argv[])
{
	READ;
	WRITE;

	int t; cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		uint64_t n,k; cin >> n >> k;
		auto r = solve(n, k);
		cout << "Case #" << i << ": " << r.first << " " << r.second << endl;
	}

return 0;
}