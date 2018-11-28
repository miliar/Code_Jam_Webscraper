#include <iostream>
#include <fstream>
#include <string>
#define STR_MAX 11


void flipLeft(std::string &S, int K) {
	for (int i = 0; i < K; i++) {
		S[i] = ((S[i] == '+') ? '-' : '+');
	}
}

int flipsRequired(std::string S, int K, int n) {
	if (S.length() == K) {
		for (int i = 0; i < K - 1; i++) {
			if (S[S.length() - 1] != S[i]) return -1; //cannot match
		}
		if (S[0] == '+') return n;
		else return n + 1;
	}
	else if (S[0] == '-') {
		flipLeft(S, K);
		return flipsRequired(S, K, n + 1);
	}
	else {
		return flipsRequired(S.substr(1, S.length() - 1), K, n); //no flip
	}
	return -1;
}

int flipsRequired(std::string S, int K) {
	return flipsRequired(S, K, 0);
}

int main() {
	std::filebuf fb;
	std::ifstream inp;
	inp.open("test.txt");
	if (inp.is_open()) {
		fb.open("output.txt", std::ios::out);
		if (fb.is_open()) {
			std::ostream out(&fb);

			int T = 0, K = 0, temp;
			std::string S = "";
			inp >> T;
			for (int i = 0; i < T; i++) {
				inp >> S >> K;
				if ((temp = flipsRequired(S, K)) >= 0)
					out << "Case #" << i + 1 << ": " << temp << std::endl;
				else
					out << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << std::endl;
			}
			fb.close();
		}
		else {
			printf("output buffer failed to open.");
		}
		inp.close();
	}
	else {
		printf("input file failed to open.");
	}
	system("PAUSE");
}