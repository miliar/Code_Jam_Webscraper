#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
#define ll long long
#define MAX 50000
using namespace std;

int A[100001];

int main(void) {

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int T;

	cin >> T;

	for (int test_case = 1; test_case <= T; test_case++) {

		long double G[101], R[101][2] , D[101][101];


		for (int i = 0; i < 101; i++) {
			for (int j = 0; j < 101; j++) {
				G[i] = 10000000000000;
				D[i][j] = -1;
			}
			R[i][0] = 0;
			R[i][1] = 0;
		}

		int N, Q, U, V;

		cin >> N;

		cin >> Q;

		for (int i = 0; i < N; i++) {
			cin >> R[i][0] >> R[i][1];
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> D[i][j];
			}
		}

		cin >> U >> V;
		G[0] = 0;
		for (int i = 0; i < N; i++) {
			long double dist = R[i][0], speed = R[i][1], time = 0;

			for (int j = i+1; j < N; j++) {
				dist -= D[j - 1][j];
				if (dist < 0) {
					break;
				}
				time += D[j - 1][j] / speed;
				G[j] = min(G[j], G[i] + time);
			}
		}

		cout << setprecision(20) << "Case #" << test_case << ": " << G[N - 1] << "\n";

	}

	return 0;
}