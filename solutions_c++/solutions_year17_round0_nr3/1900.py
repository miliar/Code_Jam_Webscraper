#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
#include<queue>
#include<algorithm>
using namespace std;
const long long MAX = 1e18 + 1;
long long t[100];
void init() {
	long long x = 1;
	for (int i = 0; x < MAX; i++) {
		t[i] = x;
		x *= 2;
	}
}
int main() {
	int T;
	long long N, K;
	int kase = 0;
	int i, x;
	init();
	ofstream out("answer.txt");
	cin >> T;
	long long a, b, c, v;
	long long ans1, ans2;
	while (T--) {
		cin >> N >> K;
		out << "Case #" << (++kase) << ": ";
		for (x = 0;; x++) {
			if (t[x] > K)
				break;
		}
		a = N - t[x] + 1;
		v = a / t[x];
		b = a % t[x];
		c = K - t[x - 1] + 1;
		ans1 = ans2 = v;
		//cout<<a<<' '<<v<<' '<<b<<' '<<c<<endl;
		if (c <= b)
			ans1++;
		if (t[x - 1] + c <= b)
			ans2++;
		out << ans1 << ' ' << ans2 << endl;
	}
	out.close();
	return 0;
}
