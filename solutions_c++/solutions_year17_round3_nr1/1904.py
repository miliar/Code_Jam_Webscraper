#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

const double PI  =3.14159265358979323846264338327950288419716939937510;

int T, K, N;
pair<long long, long long> A [1000];

int main() {
	ifstream fin ("A.in");
	ofstream fout ("A.out");
	fout << fixed << setprecision(10);

	fin >> T;
	for (int t = 1; t <= T; t++) {
		fin >> N >> K;
		for (int i = 0; i < N; i++) {
			long long r, h;
			fin >> r >> h;
			long long sa = 2*r*h;
			A[i] = make_pair(sa, r*r);
		}
		long long res = 0;
		
		for (int i = 0; i <= N-K; i++) {
			long long temp = 0;
			sort(A, A+N, [](const pair<long long, long long> &left, const pair<long long, long long> &right) {
				return left.second > right.second;
			});
			sort(A+i+1, A+N, [](const pair<long long, long long> &left, const pair<long long, long long> &right) {
				return left.first > right.first;
			});
			for (int j = i; j < i+K; j++)
				temp += A[j].first;
			temp += A[i].second;
			res = max(res, temp);
		}

		// int w = K;
		// for (int i = 0; i < N; i++) {
		// 	if (A[i].first+A[i].second > A[w].first+A[w].second)
		// 		w = i;
		// }
		// res += A[w].first + A[w].second;
		// for (int i = w; i < N-1; i++)
		// 	A[i] = A[i+1];
		// sort(A, A+N-1, [](const pair<long long, long long> &left, const pair<long long, long long> &right) {
		// 	if (left.first == right.first)
		// 		return left.second > right.second;
		// 	return left.first > right.first;
		// });
		// for (int i = 0; i < K-1; i++) {
		// 	res += A[i].first;
		// }
		
		// int temp = 0;
		// for (int i = 0; i < N; i++)
		// 	if (A[i].second > A[temp].second)
		// 		temp = i;
		// if (A[temp].second - A[K-1].second + A[temp].first - A[K-1].first > 0) {
		// 	pair<long long, long long> w = A[temp];
		// 	A[temp] = A[K-1];
		// 	A[K-1] = w;
		// }
		// sort(A, A+K, [](const pair<long long, long long> &left, const pair<long long, long long> &right) {
		// 	return left.second > right.second;
		// });
		// long long res = 0.0;
		// for (int i = 0; i < K; i++) {
		// 	res += A[i].first;
		// }
		// res += A[0].second;
		fout << "Case #" << t << ": " << res*PI << endl;
	}

	fout.close();

	return 0;
}