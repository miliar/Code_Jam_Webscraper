#include <fstream>

using namespace std;

int dist;
int N;
int start[1000];
int speed[1000];

double time_for_horse(int i) {
	return (double)(dist - start[i]) / speed[i];
}

double run() {
	double time = 0;
	double temp;
	for (int i = 0; i < N; i++) {
		temp = time_for_horse(i);
		if (temp > time)
			time = temp;
	}
	return (double)dist / time;
}

int main() {
	int T;
	ifstream in("A-large.in");
	ofstream out("output.txt");
	in >> T;
	for (int t = 0; t < T; t++) {
		//read file
		in >> dist >> N;
		for (int i = 0; i < N; i++) {
			in >> start[i] >> speed[i];
		}
		//run
		double result = run();
		//output
		out.precision(20);
		out << "Case #" << t + 1 << ": " << result << endl;
	}
	in.close();
	out.close();
	return 0;
}