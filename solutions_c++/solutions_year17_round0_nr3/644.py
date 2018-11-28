#include <iostream>

using namespace std;

void calc(long long &b, long long &s, long long n)
{
	n--;
	if (n % 2) {
		b = n/2 + 1;
		s = n/2;
	} else {
		b = s = n/2;
	}
}

int main(int argc, char const *argv[])
{
	int t, cas;
	long long n, k, nbig, nsmall, ansb, anss;

	cin >> t;
	cas = 1;
	while (t) {
		cin >> n >> k;
		nbig = 0; nsmall = 1;
		while (1) {
			if (n == 0) {
				ansb = anss = 0;
				break;
			}
			if (nbig + nsmall < k) {
				k -= nbig + nsmall;
				if ((n-1) % 2) {
					nbig *= 2;
					nbig += nsmall;
				} else {
					nsmall *= 2;
					nsmall += nbig;
				}
				n = (n-1) / 2;
			} else {
				if (k <= nbig) calc(ansb, anss, n+1);
				else calc(ansb, anss, n);
				break;
			}
		}

		cout << "Case #" << cas++ << ": " << ansb << " " << anss << endl;
		t--;
	}

	return 0;
}