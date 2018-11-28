#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <queue>

using namespace std;

long long n, k;

void read() {
	cin >> n >> k;
}

long long ra, rb;
void process2() {
	long long nn = n;
	long long kk = k;
	kk--;
	priority_queue<long long> heap;
	heap.push(nn);

	for (long long i = 0; i < kk; i++) {
		long long xx = heap.top();
		heap.pop();
		
		heap.push(xx / 2);
		heap.push((xx-1) / 2);
	}
	long long xx = heap.top();
	ra = xx / 2;
	rb = (xx-1) / 2;
}

void process() {
	//process2();
	long long a = 0, b = 1;
	k--;

	while (k > 0) {
		if (k < b) {
			break;
		} else {
			k -= b;
			long long nb = n % 2 ? 2 * b : b;
			long long na = n % 2 ? 0 : b;
			long long nn = n / 2;
			n--;
			if (k < a) {
				break;
			} else {
				k -= a;
				if (n % 2) {
					na += 2 * a;
				} else {
					nb += a;
					na += a;
				}
			}
			a = na;
			b = nb;
			n = nn;
		}
	}
	/*if (ra != n/2 || rb != (n-1)/2) {
		printf("Error for n = %lld, k = %lld => %lld %lld\n", m, mk, ra, rb);
	}*/
	cout << n / 2 << " " << (n - 1) / 2	<< endl;
}

int main() {

	int cases;

	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	
	return 0;
}