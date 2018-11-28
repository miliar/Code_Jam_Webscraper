#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int main() {
	int T = 0;
	long long N = 0, tidy = 0,x=0 ,y=0;
	bool isTidy = true;
	ifstream in("B-small-attempt0.in");
	ofstream out("B-small.txt");
	in >> T;
	for (int i = 0; i < T; i++) {
		in >> N;
		for (long long j = N; j > 0; j--,N--) {
			tidy = j;
			isTidy = true;
			while (j / 10) {
				x=j%10;
				y=(j/10)%10;
				if (x < y) {
					isTidy = false;
					break;
				} else if ((j / 100) == 0) {
					isTidy = true;
					break;
				}
				j /= 10;
			}
			j=N;
			if (isTidy) {
				out << "Case #" << i + 1 << ": " << tidy << "\n";
				cout << "Case #" << i + 1 << ": " << tidy << "\n";
				break;
			}
		}
	}
	return 0;
}
