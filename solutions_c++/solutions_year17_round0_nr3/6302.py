#include<iostream>
#include<fstream>
#include<queue>

using namespace std;

int main(void) {
	ifstream inputfile("C-small-2-attempt0.in");
	ofstream outputfile("out.txt");
	int T;

	inputfile >> T;

	for (int t = 1; t <= T; t++) {
		priority_queue<long long> estall;
		long long N, K;
		inputfile >> N >> K;
		estall.push(N);

		long long g;
		for (int i = 1; i <= K; i++) {
			g = estall.top();
			estall.pop();
			if (g % 2 == 0) {
				estall.push(g / 2);
				estall.push(g / 2 - 1);
			}
			else {
				estall.push(g / 2);
				estall.push(g / 2);
			}
		}
		long long int mi, ma;
		mi = (g - 1) / 2;
		ma = g - 1 - mi;
		cout << ma << " " << mi << endl;
		outputfile << "Case #" << t << ": " << ma << " " << mi << endl;
	}

	system("pause");
	return 0;
}
