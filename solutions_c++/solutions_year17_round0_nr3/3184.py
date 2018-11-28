#include <iostream>
using namespace std;
#define int unsigned long long
unsigned leadingZeros(int x)
{
    unsigned n = 0;
    const unsigned bits = sizeof(x) * 8;
    for (int i = 1; i < bits; i ++) {
        if (i > 1 && (signed long long)x < 0) break;
        n ++;
        x <<= 1;
    }
    return n;
}
int prev(int bits) {
	return (!bits) ? 0 : 63 - leadingZeros(bits);
}
#undef int
int main() {
	#define int unsigned long long
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	int cases, fa, sa; cin >> cases;
	for (int i = 1; i <= cases; i++) {
		int n, k; cin >> n >> k;
		int p = (int)powl(2ULL, prev(k));
		int a = p * 2ULL;
		long long o = n - a - (k - p);
		if (o < 0LL) fa = 0, sa = 0;
		else {
			int tg = ((o - (o%p)) / p) + 1ULL;
			fa = (tg + 1ULL) / 2ULL;
			sa = (tg - (tg % 2ULL)) / 2ULL;
		}
		cout << "Case #" << i << ": " << fa << " " << sa << "\n";
	}
	
	return 0;
}