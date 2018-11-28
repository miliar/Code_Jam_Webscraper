#include <iostream>
#include <sstream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
using namespace std;

int T;
long long N;
long long K;
int RN = 0;

struct Stall
{
	long long l;
	long long r;
	long long len;
	Stall(long long a=0, long long b=0): l(a), r(b), len(b - a + 1) {}
};

bool operator<(Stall a, Stall b)
{
	return (a.len <= b.len);
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
#ifdef _DEBUG
	freopen("test.in", "r", stdin);
#else
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	cin >> T;
	Stall sl;
	long long mid;
	while(T--) {
		priority_queue<Stall> q;
		cin >> N >> K;
		q.push(Stall(1, N));
		while(q.size() > 0) {
			sl = q.top();
			mid = (sl.l + sl.r)/2;
			q.pop();
			//cout << sl.l << '\t' << sl.r << '\n';
			if(--K <= 0)
				break;
			q.push(Stall(sl.l, mid-1));
			q.push(Stall(mid+1, sl.r));
		}
		long long MAX = max((mid - sl.l), (sl.r - mid));
		long long MIN = min((mid - sl.l), (sl.r - mid));
		cout << "Case #" << ++RN << ": " << MAX << " " << MIN << '\n';
	}
	return 0;
}