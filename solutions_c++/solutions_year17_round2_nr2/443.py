#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 5;

#define st first
#define nd second
#define make(a,b) make_pair(a,b)

typedef pair<int,int> pun;
typedef long long ll;

string nope = "IMPOSSIBLE";

	int n, r, o, y, g, b, v;
	int ile[255];
	int opp[255];
	char rem[255];
string test() {
	scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
	string res = "";
	if (o > 0 && o + 1> b) {
		if (o == b && o + b == n) {
			for (int i = 0; i < n/2; i ++) {
				res += "OB";
			}
			return res;
		}
		return nope;
	}
	b -= o;
	if (g  > 0 && g + 1> r) {
		if (g == r && g + r == n) {
			for (int i = 0; i < n/2; i ++) {
				res += "GR";
			}
			return res;
		}
		return nope;
	}
	r -= g;
	if (v > 0 && v + 1>y) {
		if (y == v && y + v == n) {
			for (int i = 0; i < n/2; i ++) {
				res += "YV";
			}
			return res;
		}
		return nope;
	}
	y -= v;
	if (max({b, r, y}) > n/2) return nope;
	char kolor;
	char drugi;
	char trzeci;
	if (max({b, r, y}) == b) {
		kolor = 'B';
		drugi = 'R';
		trzeci = 'Y';
	}
	else if (max({b, r, y}) == y) {
		kolor = 'Y';
		drugi = 'R';
		trzeci = 'B';
	}
	else {
		kolor = 'R';
		drugi = 'B';
		trzeci = 'Y';
	}
//	printf("kolor %c:\n", kolor);
	ile['R'] = r;
	opp['R'] = g;
	rem['R'] = 'G';
	ile['B'] = b;
	opp['B'] = o;
	rem['B'] = 'O';
	ile['Y'] = y;
	opp['Y'] = v;
	rem['Y'] = 'V';
	for (int i = 0; i < b + r + y; i ++) {
		char ko = kolor;
		if (res.empty() || res.back() != kolor && ile[kolor] > 0) {
			ko = kolor;
		}
		else {
			ko = drugi;
			if (ile[trzeci] > ile[drugi] || res.back() == ko) {
				ko = trzeci;
			}
		}
		if (opp[ko] > 0) {
			for (int k = 0; k < opp[ko]; k ++) {
				res += ko;
				res += rem[ko];
			}
			opp[ko] = 0;
		}
		res += ko;
		ile[ko] --;
	}
	return res;
}

void print_test() {
	printf("%s", test().c_str());
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		print_test();
		printf("\n");
	}
}
