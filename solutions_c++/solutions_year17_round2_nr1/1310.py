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


		int N, D;

		cin >> D >> N;

		long double time = 0;

		for (int i = 0; i < N; i++) {
			int K, S;
			cin >> K >> S;
		
			time = max(time, (D - K) / (long double)S);
		}

		cout << setprecision(20) <<  "Case #" << test_case << ": " << D / time << "\n";


	}

	return 0;
}