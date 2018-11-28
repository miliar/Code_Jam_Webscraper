#include <iostream>
#include <climits>
#include <array>
#include <map>

using namespace std;
typedef long long int Z;

int N, C, M;
int placeTix[1024];
int customerTix[1024];

int asd(int K) {
	int q = 0;
	int prom = 0;
	for(int i = N - 1; i >= 0; --i) {
		if(placeTix[i] <= K) {
			q -= min(K - placeTix[i], q);
		} else {
			q += placeTix[i] - K;
			prom += placeTix[i] - K;
		}
	}
	if(q) return -1;
	return prom;
}

int main() {
	cin.sync_with_stdio(false);
	cin.tie(nullptr);
	
	int Tc;
	cin >> Tc;
	
	for(int Ti = 1; Ti <= Tc; ++Ti) {
		cin >> N >> C >> M;
		fill(placeTix, placeTix + 1024, 0);
		fill(customerTix, customerTix + 1024, 0);
		for(int i = 0; i < M; ++i) {
			int pos, buyer;
			cin >> pos >> buyer;
			--pos;
			--buyer;
			++placeTix[pos];
			++customerTix[buyer];
		}
		int A = 0;
		for(int i = 0; i < 1024; ++i) {
			A = max(A, customerTix[i]);
		}
		int B = A;
		while(asd(B) == -1) {
			B *= 2;
		}
		while(A != B) {
			int mm = (A + B) / 2;
			if(asd(mm) == -1) {
				A = mm + 1;
			} else {
				B = mm;
			}
		}
		cout << "Case #" << Ti << ": ";
		cout << A << ' ' << asd(A);
		cout << "\n";
	}
	
	return 0;
}
