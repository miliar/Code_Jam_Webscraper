#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
class Horse{
public :
	double K, S;
};
struct pred {
	bool operator()(Horse const & a, Horse const & b) const {
		return a.K < b.K;
	}
};
void Solve(ifstream* inp, ofstream* out) {
	long D, N;
	vector<Horse> horses;
	*inp >> D >> N;
	for (int i = 0; i < N; i++)
	{
		Horse h;
		*inp >> h.K >> h.S;
		horses.push_back(h);
	}
	sort(horses.begin(), horses.end(), pred());
	double maxS = _HUGE_ENUF;
	for (int i = 0; i < N; i++) {
		double H = (D - horses[i].K) / horses[i].S;
		double thisS = (horses[i].K / H) + horses[i].S;
		if (maxS > thisS)
			maxS = thisS;
	}
	(*out).precision(numeric_limits<double>::digits10 + 1);
	*out << maxS;
}

void main() {
	ifstream input = ifstream(fopen("d:\\input.txt", "r"));
	ofstream output = ofstream(fopen("d:\\output.txt", "w"));
	int T;
	input >> T;
	for (int i = 0; i < T; i++) {
		output << "Case #" << (i + 1) << ": ";
		Solve(&input, &output);
		output << endl;
	}
	//system("pause");
}
