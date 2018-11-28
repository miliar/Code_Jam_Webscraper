#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <queue>
#include <cmath>

using namespace std;

long long int K;

vector<int> LL_to_VEC(long long int M) {
	vector<int>V;
	while (M > 0) {
		V.push_back(M % 10);
		M /= 10;
	}
	reverse(V.begin(), V.end());
	return V;
}

long long int VEC_to_LL(vector<int> V) {
	long long M = 0;
	for (int i = 0; i<int(V.size()); i++) {
		M *= 10;
		M += V[i];
	}
	return M;
}



int CHANGE(void) {
	vector<int> V;
	V = LL_to_VEC(K);
	for (int i = 1; i<int(V.size()); i++) {
		if (V[i - 1] > V[i]) { // tidy‚Å‚È‚¢‚½‚ßA•ÏŠ·‚ª•K—v‚Æ‚È‚é‰ÓŠ
			V[i - 1]--; 
			for (int j = i; j<int(V.size()); j++) { V[j] = 9; }
			K = VEC_to_LL(V); //cout << "K= " << K << endl;
			return 1;
		}
	}
	return 0;
}

int main()
{
	ifstream ifs("B-large.in");
	ofstream ofs("answer_B_large");
	int T;
	ifs >> T; cout << "T= " << T << endl;

	for (int t = 0; t<T; t++) {  // test cases
		ifs >> K; //cout << "K= " << K << endl;

		int sig=1;

		while (sig == 1) {
			sig = CHANGE();
			//cout << "sig= " << sig;
			//cout << "   K= " << K << endl;
		}
		
		cout << "Case #" << t + 1 << ": " <<K<< endl;
		ofs << "Case #" <<t+1<<": " <<K<<endl;

	} // end of test cases



	system("pause");
	return 0;
}