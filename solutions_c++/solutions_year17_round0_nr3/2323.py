#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;

#define LL long long

int T, nCase;
LL N, K;

struct Comb
{
	LL width, cnt;
	Comb(LL w = 0, LL c = 0) : width(w), cnt(c) {}
};

vector<Comb> c;

void push_to(LL width, LL cnt, int offset)
{
	for (int i=offset;i<c.size();++i) {
		if (c[i].width == width) {
			c[i].cnt += cnt;
			return;
		}
	}
	c.push_back(Comb(width, cnt));
}

void solv()
{
	c.clear();
	c.push_back(Comb(N,1));
	for (int p = 0; p < c.size(); ++p) {
		K -= c[p].cnt;
		if (K <= 0) {
			cout << c[p].width / 2 << " " << (c[p].width-1)/2 << endl;
			return;
		}
		push_to(c[p].width / 2, c[p].cnt, p + 1);
		push_to((c[p].width-1) / 2, c[p].cnt, p + 1);
	}
}


int main ()
{
	cin >> T;
	for (nCase = 1; nCase <= T; ++nCase) {
		cin >> N >> K;
		cout << "Case #" << nCase << ": " ;
		solv();
	}
	return 0;
}