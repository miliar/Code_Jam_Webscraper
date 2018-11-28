#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <assert.h>
#include <set>

using namespace std;

vector <double> try_to_average(vector <double> A, int N, double X) {

	for (int i=0; i<N; i++) {
		double upper = 1.0;
		if (i+1 < N) upper = A[i+1];
		double to_add = min(X / (i+1), upper - A[i]);

		for (int j=0; j<=i; j++) {
			X -= to_add;
			A[j] += to_add;
		}
		
	}
	
	return A;
}

double probability(vector <double> A, int N, int K, int do_not_process = -1) {
	vector <vector <double> > P(1, {1.0});
	
	for (int i=0; i<N; i++) if (i != do_not_process) {
		const vector <double> & old = P.back();
		int dim = old.size();
		vector <double> curr (dim+1, 0.0);
		
		for (int j=0; j<dim; j++) {
			curr[j+1] += A[i] * old[j];
			curr[j] += (1.0-A[i]) * old[j];
		}
		P.push_back(curr);
	}
	
	if (do_not_process >= 0) return P.back()[K];
	else return accumulate(P.back().begin()+K, P.back().end(), 0.0);
}

int main(void) {
	int num_test;
	cin>>num_test;
	
	for (int test=1; test<=num_test; test++) {
		int N, K;
		cin >> N >> K;
		
		double U;
		cin >> U;
		
		vector <double> A(N);
		for (double & a : A) cin >> a;
		
		sort(A.begin(), A.end());
		
		vector <double> B = try_to_average(A, N, U);
		
//		for (double a : B) cerr << a << "\t";
//		cerr << "\n";

		double probability_expected = probability(B,N,K);
		
		cout.precision(15);
		cout<<"Case #"<<test<<": " << probability_expected << "\n";
	}
	return 0;
}
