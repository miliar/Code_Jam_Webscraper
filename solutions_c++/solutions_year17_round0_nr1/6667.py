#include <fstream>

using namespace std;

char cakes[1001];
int K;

void swap(int index, int size) {
	for (int i = index; i < index + size; i++) {
		if (cakes[i] == '-')
			cakes[i] = '+';
		else
			cakes[i] = '-';
	}
}

int run() {
	int len = strlen(cakes);
	int count = 0;
	for (int i = 0; i <= len-K; i++) {
		if (cakes[i] == '-') {
			swap(i, K);
			count++;
		}
	}
	for (int i = 0; i < len; i++){
		if (cakes[i] == '-')
			return -1;
	}
	return count;
}

int main() {
	int T;
	ifstream in("A-large.in");
	ofstream out("output.txt");
	in >> T;
	for (int t = 0; t < T; t++) {
		//read file
		in >> cakes >> K;
		//run
		int result = run();
		//output
		if (result == -1) {
			out << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
		}
		else {
			out << "Case #" << t + 1 << ": " << result << endl;
		}
	}
	in.close();
	out.close();
	return 0;
}