#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <string>

using namespace std;

int main() {
	ofstream fout("manesmall.out");
	ifstream fin("manesmall.in");
	int T;
	fin >> T;
	for (int t = 0; t < T; t++) {
		int N;
		fin >> N;
		int R, O, Y, G, B, V;
		fin >> R >> O >> Y >> G >> B >> V;
		B -= 2 * O;
		R -= 2 * G;
		Y -= 2 * V;
		int RED = R + G;
		int YELLOW = Y + V;
		int BLUE = B + O;
		int MAX = max(RED, max(YELLOW, BLUE));
		int C = 0;
		string d1, d2, d3, s1, s2, s3;
		int c1, c2, c3, k1,k2,k3;
		int t1, t2, t3;
		if (RED == MAX) {
			d1 = "R";
			d2 = "B";
			d3 = "Y";
			s1 = "RGR";
			s2 = "BOB";
			s3 = "YVY";
			t1 = RED;
			t3 = YELLOW;
			t2 = BLUE;
			c1 = R;
			k2 = O;
			c3 = Y;
			k1 = G;
			c2 = B;
			k3 = V;
		} else if (YELLOW == MAX) {
			d3 = "R";
			d2 = "B";
			d1 = "Y";
			s3 = "RGR";
			s2 = "BOB";
			s1 = "YVY";
			t3 = RED;
			t1 = YELLOW;
			t2 = BLUE;
			c3 = R;
			k2 = O;
			c1 = Y;
			k3 = G;
			c2 = B;
			k1 = V;
		} else if (BLUE == MAX) {
			d2 = "R";
			d1 = "B";
			d3 = "Y";
			s2 = "RGR";
			s1 = "BOB";
			s3 = "YVY";
			t2 = RED;
			t3 = YELLOW;
			t1 = BLUE;
			c2 = R;
			k1 = O;
			c3 = Y;
			k2 = G;
			c1 = B;
			k3 = V;
		}
		else cout << "ERROR" << endl;
		bool possible = true;
		string answer="";
		int n = 0;
		while (possible && n < N) {
			if (c1 > 0) {
				answer += d1;
				n++;
				c1--;
			}
			else if (k1 > 0) {
				answer += s1;
				n+=3;
				k1--;
			}else possible = false;
			if (C < t1 - t3) {
				if (c2 > 0) {
					answer += d2;
					n++;
					c2--;
				}
				else if (k2 > 0) {
					answer += s2;
					n+=3;
					k2--;
				} else possible = false;
			}
			else if (C < t2) {
				if (c2 > 0) {
					answer += d2;
					n++;
					c2--;
				}
				else if (k2 > 0) {
					answer += s2;
					n += 3;
					k2--;
				}
				else possible = false;
				if (c3 > 0) {
					answer += d3;
					n++;
					c3--;
				}
				else if (k3 > 0) {
					answer += s3;
					n += 3;
					k3--;
				}else possible = false;
			}
			else {
				if (c3 > 0) {
					answer += d3;
					n++;
					c3--;
				}
				else if (k3 > 0) {
					answer += s3;
					n += 3;
					k3--;
				}
				else possible = false;
			}
			C++;
		}
		fout << "Case #" << t + 1 << ": ";
		if (!possible) {
			fout << "IMPOSSIBLE";
		}
		else {
			fout << answer;
		}
		fout << endl;
	}
	system("pause");
}