#include <iostream>
#include <vector>
#include <math.h>
#include <iomanip>
using namespace std;

#define PI (3.141592653589793)


double calc (vector <int> &v) {
	double d = 0;
	for (int i = 0; i < v.size(); i++) {
		d += v[i];
	}
	return d;
}

double area (vector <int> v, vector <double> &AL, vector <double> &AS, int N, int K, int i, double A, double &AM) {
	if (i == K) {
		double a = calc(v);
		AM = max(AM, A + AS[v[K - 1]]);
	} else {
		if (v[i] == K -1) {
			return 0;
		} else {
			for (int p = v[i - 1] + 1; p < N; p++) {
				v[i] = p;
				area(v, AL, AS, N, K, i + 1, A + AL[p], AM);
			}
		}
	}
}

int main() {
	int N, K, T;
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		cin >> N >> K;
		double A = 0;
		vector <double> AL(N);
		vector <double> AS(N);
		
		vector <double> R(N);
		vector <double> H(N);
		
		for (int j = 0; j < N; j++) {
			cin >> R[j] >> H[j];
		}
		
		for (int j = 0; j < N; j++) {
			for (int g = j + 1; g < N; g++)  {
				if (R[j] > R[g]) {
					swap(R[j], R[g]);
					swap(H[j], H[g]);
				}
			}
		}
		
		cout << fixed;
		cout << setprecision(9);
		for (int j = 0; j < N; j++) {
			AL[j] = 2.0*PI*R[j]*H[j];
			AS[j] = PI*R[j]*R[j];
		}
		
		/*double AM = 0;
		//maxarea(R, H, AL, H, A, AM, K, 0);
		
		for (int p = 0; p < N - K + 1; p++) {
			double am = 0;
			for (int p1 = 0; p1 < K; p1++) {
				A += AL[p + p1];
				if (am  < AS[p + p1])
					am = AS[p + p1];
			}
			A += am;
			if (AM < A)
				AM = A;
			A = 0;
		}*/
		
		vector <int> v(K);
		
		double AM = 0, AC = 0;
		for (int p = 0; p < N; p++) {
			v[0] = p;
			area (v, AL, AS, N, K, 1, AL[p], AM);
			AC = max(AM, AC);
			AM = 0;
		}
		cout << "Case #" << i + 1 << ": " << AC << endl;
	}
}