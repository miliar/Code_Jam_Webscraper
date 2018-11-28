#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
	int T; cin >> T;

	for (int t = 0; t < T; t++) {
		int N, R, O, Y, G, B, V; cin >> N >> R >> O >> Y >> G >> B >> V;
		bool flag = true;

		R -= G;
		B -= O;
		Y -= V;
		/*
		if ((R < 0 || B < 0 || Y < 0) && ((O > 0 && G == 0 && V == 0) || (O == 0 && G > 0 && V == 0) || (O == 0 && G == 0 && V > 0)))flag = false;
		else if (R == 0 && O == 0 && V == 0)flag = false;
		else if (B == 0 && G == 0 && V == 0)flag = false;
		else if (Y == 0 && O == 0 && G == 0)flag = false;
		*/
		int tmpR = R, tmpB = B, tmpY = Y;
		vector<int>RBY;
		RBY.reserve(N);
		int a = 0;
		for (int i = 0; i < R + B + Y;i++) {
			if (a == 0) {
				if (tmpR > tmpB) {
					if(tmpR>tmpY)RBY.push_back(1), a = 1, tmpR--;
					else if(tmpR<tmpY)RBY.push_back(3), a = 3, tmpY--;
					else RBY.push_back(1), a = 1, tmpR--;
				}
				else if (tmpR < tmpB) {
					if (tmpB > tmpY)RBY.push_back(2), a = 2, tmpB--;
					else if (tmpB < tmpY)RBY.push_back(3), a = 3, tmpY--;
					else RBY.push_back(2), a = 2, tmpB--;
				}
				else {
					if (tmpR>tmpY)RBY.push_back(1), a = 1, tmpR--;
					else if (tmpR<tmpY)RBY.push_back(3), a = 3, tmpY--;
					else RBY.push_back(1), a = 1, tmpR--;
				}
			}
			else if (a == 1) {
				if (tmpB > tmpY)RBY.push_back(2), a = 2, tmpB--;
				else if (tmpB < tmpY)RBY.push_back(3), a = 3, tmpY--;
				else {
					if (RBY[0] == 2)RBY.push_back(2), a = 2, tmpB--;
					else if (RBY[0] == 3)RBY.push_back(3), a = 3, tmpY--;
					else RBY.push_back(2), a = 2, tmpB--;
				}
			}
			else if (a == 2) {
				if (tmpR > tmpY)RBY.push_back(1), a = 1, tmpR--;
				else if (tmpR < tmpY)RBY.push_back(3), a = 3, tmpY--;
				else {
					if (RBY[0] == 1)RBY.push_back(1), a = 1, tmpR--;
					else if (RBY[0] == 3)RBY.push_back(3), a = 3, tmpY--;
					else RBY.push_back(1), a = 1, tmpR--;
				}
			}
			else if (a == 3) {
				if (tmpB > tmpR)RBY.push_back(2), a = 2, tmpB--;
				else if (tmpB < tmpR)RBY.push_back(1), a = 1, tmpR--;
				else {
					if (RBY[0] == 2)RBY.push_back(2), a = 2, tmpB--;
					else if (RBY[0] == 1)RBY.push_back(1), a = 1, tmpR--;
					else RBY.push_back(2), a = 2, tmpB--;
				}
			}
		}

		cout << "Case #" << t + 1 << ": ";

		if (tmpR < 0 || tmpB < 0 || tmpY < 0)flag = false;
		else if (RBY.size() && RBY[0] == RBY[RBY.size() - 1])flag = false;
		else if (R == 0 && G > 0) {
			if (O > 0 || V > 0 || B > 0 || Y > 0)flag = false;
			else {
				for (int j = 0; j < G; j++) {
					cout << "GR";
				}
			}
		}
		else if (B == 0 && O > 0) {
			if (G > 0 || V > 0 || R > 0 || Y > 0)flag = false;
			else {
				for (int j = 0; j < O; j++) {
					cout << "OB";
				}
			}
		}
		else if (Y == 0 && V > 0) {
			if (O > 0 || G > 0 || B > 0 || R > 0)flag = false;
			else {
				for (int j = 0; j < V; j++) {
					cout << "VY";
				}
			}
		}

		if (flag) {
			vector<bool>OGV(4);
			for (int i = 0; i < RBY.size(); i++) {
				if (RBY[i] == 1) {
					cout << 'R';
				}
				else if (RBY[i] == 2) {
					cout << 'B';
				}
				else if (RBY[i] == 3) {
					cout << 'Y';
				}

				if (OGV[RBY[i]] == false) {
					if (RBY[i] == 1) {
						for (int j = 0; j < G; j++) {
							cout << "GR";
						}
					}
					else if (RBY[i] == 2) {
						for (int j = 0; j < O; j++) {
							cout << "OB";
						}
					}
					else if (RBY[i] == 3) {
						for (int j = 0; j < V; j++) {
							cout << "VY";
						}
					}
				}
			}

			cout << endl;

		}
		else {
			cout << "IMPOSSIBLE" << endl;
		}
	}

    return 0;
}

