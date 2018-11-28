#include <fstream>
#include <iostream>
#include <string>

#define TIDY_NUM_MAX 1E18

 bool isTidy(int N) {//nondecreasing left to right
	while (N > 0) {
		if ((N / 10) % 10 <= N % 10) {
			N /= 10;
		}
		else return false;
	}
	return true;
}

int highestTidyNum(int N) {
	for (int i = N; i > N / 2; i--) {
		if (isTidy(i)) return i;
	}
}

int main() {
	std::filebuf fb;
	std::ifstream inp;
	inp.open("test.txt");
	if (inp.is_open()) {
		fb.open("output.txt", std::ios::out);
		if (fb.is_open()) {
			std::ostream out(&fb);
			int T = 0;
			int N = 0;
			inp >> T;
			for (int i = 0; i < T; i++) {
				inp >> N;
				out << "Case #" << i + 1 << ": " << highestTidyNum(N) << std::endl;
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