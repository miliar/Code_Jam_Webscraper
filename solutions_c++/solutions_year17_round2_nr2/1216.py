#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
#define ll long long
#define MAX 50000
using namespace std;

int A[100001];

int main(void) {

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int T;

	cin >> T;

	for (int test_case = 1; test_case <= T; test_case++) {


		int N;
		cin >> N;

		int R, O, Y, G, B, V;

		cin >> R >> O >> Y >> G >> B >> V;

		if (O > B || (B == O && B + O != N && B != 0)) {
			cout << "Case #" << test_case << ": IMPOSSIBLE\n";
			continue;
		}
		else if (G > R || (G == R && G + R != N && R != 0)) {
			cout << "Case #" << test_case << ": IMPOSSIBLE\n";
			continue;
		}
		else if (V > Y || (V == Y && Y + V != N && Y != 0)) {
			cout << "Case #" << test_case << ": IMPOSSIBLE\n";
			continue;
		}

		if (O + B == N && O == B) {
			cout << "Case #" << test_case << ": ";
			for (int i = 0; i < B; i++) {
				cout << "OB";
			}
			cout << "\n";
			continue;
		}
		if (R + G == N && R == G) {
			cout << "Case #" << test_case << ": ";
			for (int i = 0; i < G; i++) {
				cout << "RG";
			}
			cout << "\n";
			continue;
		}
		if (Y + V == N && Y == V) {
			cout << "Case #" << test_case << ": ";
			for (int i = 0; i < Y; i++) {
				cout << "YV";
			}
			cout << "\n";
			continue;
		}

		B -= O;
		R -= G;
		Y -= V;

		if (B > (B + R + Y) / 2 || R > (B + R + Y) / 2 || Y > (B + R + Y) / 2) {
			cout << "Case #" << test_case << ": IMPOSSIBLE\n";
			continue;
		}

		bool blue = true, red = true, yellow = true;
		char last_one = ' ';
		bool first_yellow = Y > B && Y > R;

		cout << "Case #" << test_case << ": ";

		while (B + R + Y > 0) {

			if (first_yellow && (Y >= R || last_one == 'R') && (Y >= B || last_one == 'B') && last_one != 'Y') {
				Y--;
				last_one = 'Y';
				if (yellow) {
					yellow = false;
					cout << "Y";
					for (int i = 0; i < O; i++) {
						cout << "VY";
					}
				}
				else {
					cout << "Y";
				}
			}

			else if ((B >= R || last_one == 'R') && (B >= Y || last_one == 'Y') && last_one != 'B') {
				B--;
				last_one = 'B';
				if (blue) {
					blue = false;
					cout << "B";
					for (int i = 0; i < O; i++) {
						cout << "OB";
					}
				}
				else {
					cout << "B";
				}
			}
			else if ((R >= B || last_one == 'B') && (R >= Y || last_one == 'Y') && last_one != 'R') {
				R--;
				last_one = 'R';
				if (red) {
					red = false;
					cout << "R";
					for (int i = 0; i < G; i++) {
						cout << "GR";
					}
				}
				else {
					cout << "R";
				}
			}
			else if ((Y >= B || last_one == 'B') && (Y >= R || last_one == 'R') && last_one != 'Y') {
				Y--;
				last_one = 'Y';
				if (yellow) {
					yellow = false;
					cout << "Y";
					for (int i = 0; i < V; i++) {
						cout << "VY";
					}
				}
				else {
					cout << "Y";
				}
			}
			

		}
		
		
		cout << "\n";

	}

	return 0;
}