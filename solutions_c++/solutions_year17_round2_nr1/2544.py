#include <fstream>
#include <algorithm>
#include <utility>
#include <vector>
#include <iomanip>
using namespace std;
ifstream fin ("A.in"); ofstream fout ("A.out");

void onerun(int t) {
	double D; int N; fin >> D >> N;
	double minS = 1e15;
	while (N--) {
		double K, S; fin >> K >> S;
		minS = min(minS, S*D/(D-K));
	}
	fout << "Case #" << t << ": " << setprecision(16) << minS << endl; 
}

int main() {
	int T; fin >> T;
	for (int t=1; t<=T; t++) onerun(t);
}