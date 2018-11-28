#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#define pb push_back
#define mp make_pair
#define int64 long long int
#define unit64 unsigned long long int
using namespace std;


const int N = 1e5 + 5;
int I[N];

void solve (int T)
{
	memset (I, 0, sizeof I);
	int n, R, B, G, O,Y, V,flag = 0;
	cin >> n >> R >> O >> Y >> G >> B >> V;
	vector <pair<int, char> > v;
	v.pb (mp (R, 'R'));
	v.pb (mp (B, 'B'));
	v.pb (mp (Y, 'Y'));
	sort (v.begin (), v.end ());
	reverse (v.begin (), v.end ());
	char one = v[2].second;
	char two = v[1].second;
	char three = v[0].second;
	int x = min (R, min (Y, B));
	vector <char> ans;
	for (int i = 0; i <  x; i++) {
		ans.pb (one);
		ans.pb (two);
		ans.pb (three);
	}
	R -= x, Y -= x, B -= x;
	vector <int> v2;
	v2.pb (R), v2.pb (Y), v2.pb (B);
	sort (v2.begin (), v2.end ());
	int xx = min (v2[1], v2[2]);
	R -= xx, Y -= xx, B -= xx;
	for (int i = 0; i < xx; i++) {
		ans.pb (two);
		ans.pb (three);
	}
	int left = max (R, max (Y, B));
	if (left > x) flag = true;
	printf ("Case #%d: ", T);
	if (flag) {
		puts ("IMPOSSIBLE");
		return;
	}
	for (int i = 1; i < ans.size (); i++) {
		if (left && ans[i] == two) {
		left--;
		I[i] = true;
		}
	}
	for (int i = 0; i < ans.size (); i++) {
		if (I[i]) putchar (three);
		putchar (ans[i]);
	}
	puts ("");
}
int main ()
{
	int t;
	scanf ("%d", &t);
	for (int i = 1; i <= t; i++) solve (i);
	return 0;
}
