#include <string>
#include <iostream>

using namespace std;

bool ok(long long i) {
	long long x;
	x = i%10;
	for(;i;) {
		i/=10;
		if((i%10) > x) return false;
		x = i%10;
	}
	return true;
}

long long solve(long long a) {
	if(a<10) return a;

	long long r = 0;
	long long base = 1;
	for(;a;) {
		if(ok(a)) {
			r += base * a;
			break;
		} else {
			for(;;) {
				if(a%10==9) break;
				if(ok(a)) break;
				a--;
			}
			r += base * (a%10);
			a /= 10;
		}
		//cout << "r " << r << endl;
		base *= 10;
	}
	return r;
}

long long solve1(long long a) {
	long long r = 1;
	for(long long i = 1; i <= a; i++) {
		if(ok(i)) r = i;
	}
	return r;
}


void go() {
	long long a;
	cin >> a;
	cout << solve(a) << endl;
	return;
	for(int a = 1; a <= 10000; a++) {
		long long b = solve(a);
		long long c = solve1(a);
		if(b!=c) cout << b << " " << c <<" " << a << endl;
	}
}

int main() {
	ios::sync_with_stdio(false); cin.tie(0);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		go();
	}
	return 0;
}


