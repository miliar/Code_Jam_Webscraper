#include <iostream>
#include <string.h>
using namespace std;

int s[4005];
bool chk[4];
int G, V, O, R, Y, B;
void dodo1() {
	int i;
	for (i = 0; i < R; i++) {
		s[3 * i] = 1;
		s[3 * i + 1] = 2;
		s[3 * i + 2] = 3;
	}
	for (i = 0; i < R - Y; i++) {
		s[3 * i + 1] = 0;
	}
	for (i = R - Y; i < R - Y + R - B; i++) {
		s[3 * i + 2] = 0;
	}
	for (i = 0; i < 3 * R; i++) {
		if (s[i] == 1) {
			if (!chk[1]) {
				chk[1] = 1;
				for (int j = 0; j < G; j++) cout << "RG";
				cout << "R";
			}
			else {
				cout << "R";
			}
		}
		if (s[i] == 2) {
			if (!chk[2]) {
				chk[2] = 1;
				for (int j = 0; j < V; j++) cout << "YV";
				cout << "Y";
			}
			else {
				cout << "Y";
			}
		}
		if (s[i] == 3) {
			if (!chk[3]) {
				chk[3] = 1;
				for (int j = 0; j < O; j++) cout << "BO";
				cout << "B";
			}
			else {
				cout << "B";
			}
		}
	}
}
void dodo2() {
	int i;
	for (i = 0; i < Y; i++) {
		s[3 * i] = 1;
		s[3 * i + 1] = 2;
		s[3 * i + 2] = 3;
	}
	for (i = 0; i < Y-R; i++) {
		s[3 * i + 1] = 0;
	}
	for (i = Y-R; i <Y-R+Y-B; i++) {
		s[3 * i + 2] = 0;
	}
	for (i = 0; i < 3 * Y; i++) {
		if (s[i] == 1) {
			if (!chk[1]) {
				chk[1] = 1;
				for (int j = 0; j < V; j++) cout << "YV";
				cout << "Y";
			}
			else {
				cout << "Y";
			}
		}
		if (s[i] == 2) {
			if (!chk[2]) {
				chk[2] = 1;
				for (int j = 0; j < G; j++) cout << "RG";
				cout << "R";
			}
			else {
				cout << "R";
			}
		}
		if (s[i] == 3) {
			if (!chk[3]) {
				chk[3] = 1;
				for (int j = 0; j < O; j++) cout << "BO";
				cout << "B";
			}
			else {
				cout << "B";
			}
		}
	}
}
void dodo3() {
	int i;
	for (i = 0; i < B; i++) {
		s[3 * i] = 1;
		s[3 * i + 1] = 2;
		s[3 * i + 2] = 3;
	}
	for (i = 0; i < B - Y; i++) {
		s[3 * i + 1] = 0;
	}
	for (i = B - Y; i < B - Y + B - R; i++) {
		s[3 * i + 2] = 0;
	}
	for (i = 0; i < 3 * B; i++) {
		if (s[i] == 1) {
			if (!chk[1]) {
				chk[1] = 1;
				for (int j = 0; j < O; j++) cout << "BO";
				cout << "B";
			}
			else {
				cout << "B";
			}
		}
		if (s[i] == 2) {
			if (!chk[2]) {
				chk[2] = 1;
				for (int j = 0; j < V; j++) cout << "YV";
				cout << "Y";
			}
			else {
				cout << "Y";
			}
		}
		if (s[i] == 3) {
			if (!chk[3]) {
				chk[3] = 1;
				for (int j = 0; j < G; j++) cout << "RG";
				cout << "R";
			}
			else {
				cout << "R";
			}
		}
	}
}
int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, tc;
	cin >> tc;
	for (t = 1; t <= tc; t++) {
		int N, flg=0, nn, i;
		memset(chk, 0, sizeof(chk));
		memset(s, 0, sizeof(s));
		cin >> N >> R >> O >> Y >> G >> B >> V;
		if (B < O) flg = 1;
		if (R < G) flg = 1;
		if (Y < V) flg = 1;
		if (B == O &&B != 0&& (R + Y + G + V != 0)) flg = 1;
		else if (B == O && B!=0) flg = 2;
		if (R == G && R != 0 && (B + Y + O + V != 0)) flg = 1;
		else if (R == G && R!=0) flg = 2;
		if (Y == V && Y!=0 && (R + O + G + B != 0)) flg = 1;
		else if (Y == V && Y!=0) flg = 2;
		if (flg == 2) {
			cout << "Case #" << t << ": ";
			if (B == O && B!=0) {
				for (i = 0; i < B; i++) cout << "BO";
				cout << endl;
			}
			else if (R == G && R!=0) {
				for (i = 0; i < R; i++) cout << "RG";
				cout << endl;
			}
			else if (Y == V && Y!=0) {
				for (i = 0; i < Y; i++) cout << "YV";
				cout << endl;
			}
			continue;
		}


		if (flg == 0) {
			B -= O;
			R -= G;
			Y -= V;
			nn = B + R + Y;
			if (B > (nn / 2)) flg = 1;
			if (R > (nn / 2)) flg = 1;
			if (Y > (nn / 2)) flg = 1;
		}
		cout << "Case #" << t << ": ";
		if (flg == 1) cout << "IMPOSSIBLE" << endl;
		else {
			if (R >= Y&&R >= B) {
				dodo1();
			}
			else if (Y >= R&&Y >= B) {
				dodo2();
			}
			else {
				dodo3();
			}
			cout << endl;
		}
	}

	return 0;
}