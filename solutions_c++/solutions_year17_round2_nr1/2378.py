#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	for (int caseNum = 1; caseNum <= T; caseNum++) {
		long D;
		int N;
		cin >> D >> N;
		double longestTime = 0;
		for (int i = 0; i < N; i++) {
			long K, S;
			cin >> K >> S;
			double timeNeeded = (D - K) * 1.0 / S;
			if (timeNeeded > longestTime) {
				longestTime = timeNeeded;
			} 
		}
		cout << "Case #" << caseNum << ": " << setiosflags(ios::fixed) << setprecision(6) << D / longestTime << endl;
	}
	return 0;
}