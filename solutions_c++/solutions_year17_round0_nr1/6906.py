#include <fstream>
#include <iostream>
#include <string>


void solveCase(std::istream& in, std::ostream& out) {
	std::string S;
	int K;
	in >> S;
	in >> K;
	if (S.size() < K) out << "IMPOSSIBLE";
	
	auto flip = [](std::string::iterator& it, int K) {
		for (int k = 0; k < K; k++, it++) {
			*it = *it == '-' ? '+' : '-';
		}
	};
	int flips = 0;

	auto idx = std::string::npos;
	auto last = 0;
	while ((idx = S.find_first_of('-')) != std::string::npos) {
		if (idx < last || idx + K > S.size()) {
			out << "IMPOSSIBLE";
			return;
		}
		flip(S.begin()+idx, K);
		//out << S << std::endl;
		flips++;
		last = idx;
	}
	out << flips;
}

int main(int argc, char** argv) {
	using namespace std;
	ifstream in("./A-large.in", ifstream::in);
	ofstream out("./A-large.out", ofstream::out);
	//auto& out = cout;
	int T;
	in >> T;
	//cout << "Test Cases: " << T << endl;
	int t = 0;
	while (t++ < T) {
		out << "Case #" << t << ": ";
		solveCase(in, out);
		out << endl;
	}
	return 0;
}