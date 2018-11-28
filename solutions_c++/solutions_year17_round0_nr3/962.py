#include <cstdio>
#include <iostream>
#include <map>

using namespace std;

char s[1000005];
map<long long, long long> M;

int main() {
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	int test;
	scanf("%d", &test);
	int testC = 0;
	long long n, k;
	while (test --) {
		cin >> n >> k;
		printf("Case #%d: ", ++ testC);
		M.clear();
		M[n] = 1;
		while (1) {
			map<long long, long long> :: iterator it = M.end();
			it --;
			long long size = it -> first;
			long long num = it -> second;
			if (k > num) {
				k -= num;
				M[(size - 1) / 2] += num;
				M[size / 2] += num;
				M.erase(it);
			} else {
				cout << size / 2 << ' ' << (size - 1) / 2 << endl;
				break;
			}
		}
	}
	return 0;
}
