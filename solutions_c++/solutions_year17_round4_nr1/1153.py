#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <string>
#include <cstdio>
#include <vector>
#include <deque>
#include <cmath>
#include <list>
#include <set>
#include <map>
#define rep(i,m,n) for(int i=(m),_end=(n);i < _end;++i)
#define repe(i,m,n) for(int i=(m), _end =(n);i <= _end;++i)
typedef long long ll;
using namespace std;


int g[5];

void sol(ifstream& sr, ofstream& sw) {

	sw.precision(17);

	int N, P;
	sr >> N >> P;

	for (int i = 0; i < P; i++)
	{
		g[i] = 0;
	}
	for (int i = 0; i < N; i++)
	{
		int h;
		sr >> h;
		g[h%P]++;
	}

	if (P == 2)
	{
		sw << g[0] + (g[1] + 1) / 2;
	}
	if (P == 3)
	{
		int x = std::min(g[1], g[2]);
		g[1] -= x;
		g[2] -= x;
		sw << g[0] + x + (g[1] + 2) / 3 + (g[2] + 2) / 3;
	}
	if (P == 4)
	{
		int r = 0;
		r += g[0];
		g[0] = 0;
		int x = std::min(g[1], g[3]);
		r += x;
		g[1] -= x;
		g[3] -= x;
		r += g[2] / 2;
		g[2] %= 2;
		if (g[1] > 1 && g[2] == 1)
		{
			r++;
			g[1] -= 2;
			g[2] = 0;
		}
		if (g[3] > 1 && g[2] == 1)
		{
			r++;
			g[3] -= 2;
			g[2] = 0;
		}
		if (g[2] == 1 && g[1] == 0 && g[3] == 0)
			r++;
		r += (g[3] + 3) / 4 + (g[1] + 3) / 4;
		sw << r;
	}
}

int main() {

	ifstream sr = ifstream("D:\\in.in");
	ofstream sw = ofstream("D:\\out.out");

	int T;
	sr >> T;
	for (int i = 0; i < T; i++)
	{
		sw << "Case #" << i + 1 << ": ";
		sol(sr, sw);
		sw << endl;
		cout << i << endl;
	}
	sr.close();
	sw.close();
	cout << "FINISHED type a number and enter to exit";
	cin >> T;

	return 0;
}
