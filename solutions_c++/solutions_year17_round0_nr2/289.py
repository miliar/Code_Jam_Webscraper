#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <string>
using namespace std;

void solve(int test) {
	string N;
	cin >> N;
	bool can = false;
	string N1 = "", N2 = "";
	for (int i = 0; i < N.length(); ++i) {
		N1 += '1';
		if (i != N.length() - 1)
			N2 += '9';
	}
	printf("Case #%d: ", test);
	if (N1 > N) {
		cout << N2 << endl;
		return;
	}
	for (int fig = 0; fig < N.length(); ++fig) {
		char maxfig = N[fig];
		string Ncopy = N1;
		for (int a = fig; a < N.length(); ++a) {
			Ncopy[a] = maxfig;
		}
		if (Ncopy > N) {
			N1[fig] = maxfig - 1;
			for (int a = fig + 1; a < N.length(); ++a) {
				N1[a] = '9';
			}
			cout << N1 << endl;
			return;
		}
		else {
			N1 = Ncopy;
		}
	}
	cout << N1 << endl;
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
		solve(i + 1);
	return 0;
}