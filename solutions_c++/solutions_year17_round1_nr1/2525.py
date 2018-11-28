#include<iostream>
#include<fstream>
using namespace std;
void cake(char **a,int R,int C);
int main() {
	int T;
	ifstream input;
	ofstream output;
	input.open("h.txt");
	output.open("out.txt");
	input >> T;
	for (int t = 0; t < T; t++) {
		int R,C;
		input >> R >> C;
		char **a;
		a = new char*[R];
		for (int i = 0; i < R; i++)
			a[i] = new char[C];

		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				input >> a[r][c];
			}
		}
		cake(a,R,C);
		output << "Case #" << t + 1 << ":" << endl;
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				output<< a[r][c];
			}
			output << endl;
		}

	}

}

void cake(char **a,int R,int C) {
	int notdone = -1;
	bool copy = false;
	for (int r = 0; r < R; r++) {
		char temp='?';	
		for (int c = 0; c < C; c++)
			if (a[r][c] != '?') {
				temp = a[r][c];
				break;
			}

		if (temp == '?' && notdone == r - 1)
			notdone++;
		else if (temp == '?')
			a[r] = a[r - 1];

		else if (temp != '?') {
			if (notdone == r - 1)
				copy = true;

			for (int c = 0; c < C; c++) {
				if (a[r][c] == '?')
					a[r][c] = temp;
				else temp = a[r][c];

			}

		}

		if (copy == true) {
			for (int i = 0; i <= notdone; i++) {
				a[i] = a[r];
			}
			copy = false;
		}

	}
}