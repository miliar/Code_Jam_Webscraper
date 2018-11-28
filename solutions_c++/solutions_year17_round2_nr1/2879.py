using namespace std;
#include <fstream>
#include <string>
#include <iostream>
#include <iomanip>

ofstream out;
ifstream in;

void Case(int n, float s) {
	out << "Case #" << n << ": " << fixed << setprecision(6) << s << "\n";
}

int main() {
	out.open("output.txt");
	in.open("A-large.in");
	
	int N;
	in >> N;
	double pos, v;
	double l, h;
	float maxTime;
	float time;
	for (int i=0; i<N; i++) {
		in >> l >> h;
		maxTime = 0;
		for (int j=0; j<h; j++) {
			in >> pos >> v;
			time = (l-pos)/v;
			if (time > maxTime) maxTime = time;
			cout << i+1 << " " << l << " " << pos << " " << v << " " << time << "\n";
		}
		
		Case(i+1, l/maxTime);
	}
}
