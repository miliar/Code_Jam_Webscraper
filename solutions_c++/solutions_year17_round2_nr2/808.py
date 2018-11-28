#include <iostream>
#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

int main() {
	int nTests;
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		cout << "Case #" << test << ": ";
		int n;
		cin >> n;
		int R, O, Y, G, B, V;
		cin >> R >> O >> Y >> G >> B >> V;
		int nB, nY, nR;
		if (O > B || G > R || V > Y) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			nB = B - O;
			nR = R - G;
			nY = Y - V;
			//cout << "nB = " << nB << endl;
			//cout << "nR = " << nR << endl;
			//cout << "nY = " << nY << endl;
			bool onlyB = (B > 0) && (nB == 0);
			bool onlyR = (R > 0) && (nR == 0);
			bool onlyY = (Y > 0) && (nY == 0);
			if (onlyB && B + O == n) {
				for (int i = 0; i < n; ++i) {
					cout << ((i % 2) ? 'B' : 'O');
				}
				cout << endl;
			} else if (onlyY && Y + V == n) {
				for (int i = 0; i < n; ++i) {
					cout << ((i % 2) ? 'Y' : 'V');
				}
				cout << endl;
			} else if (onlyR && R + G == n) {
				for (int i = 0; i < n; ++i) {
					cout << ((i % 2) ? 'R' : 'G');
				}
				cout << endl;
			}
			/*if (onlyB && !onlyY && !onlyR) {
			 for (int i = 0; i < n; ++i) {
			 cout << ((i % 2) ? 'B' : 'O');
			 }
			 cout << endl;
			 } else if (!onlyB && onlyY && !onlyR) {
			 for (int i = 0; i < n; ++i) {
			 cout << ((i % 2) ? 'Y' : 'V');
			 }
			 cout << endl;
			 } else if (!onlyB && !onlyY && onlyR) {
			 for (int i = 0; i < n; ++i) {
			 cout << ((i % 2) ? 'R' : 'G');
			 }
			 cout << endl;
			 } */
			else if (onlyB || onlyY || onlyR) {
				cout << "IMPOSSIBLE" << endl;
			} else {
				vector<pair<int, char> > P;
				P.push_back(make_pair(nB, 'B'));
				P.push_back(make_pair(nR, 'R'));
				P.push_back(make_pair(nY, 'Y'));
				sort(P.begin(), P.end());
				string S;
				S.push_back(P[2].second);
				if (P[1].first - P[0].first > P[2].first) {
					cout << "IMPOSSIBLE" << endl;
				} else {
					for (int i = 0; i < P[1].first - P[0].first; ++i) {
						S.push_back(P[1].second);
						S.push_back(P[2].second);
					}
					S.pop_back();
					int used = P[1].first - P[0].first;
					P[2].first -= used;
					P[1].first -= used;
					if (P[2].first > P[0].first + P[1].first) {
						cout << "IMPOSSIBLE" << endl;
					} else {
						int j = 0;
						while (P[2].first > 0) {
							S.push_back(P[2].second);
							--P[2].first;
							if (j % 2 == 0) {
								assert(P[0].first > 0);
								S.push_back(P[0].second);
								--P[0].first;
							} else {
								assert(P[1].first > 0);
								S.push_back(P[1].second);
								--P[1].first;
							}
							++j;
						}
						while (P[0].first > 0 || P[1].first > 0) {
							if (j % 2 == 0) {
								assert(P[0].first > 0);
								S.push_back(P[0].second);
								--P[0].first;
							} else {
								assert(P[1].first > 0);
								S.push_back(P[1].second);
								--P[1].first;
							}
							++j;
						}
						bool seenB = false, seenR = false, seenY = false;
						assert(S.length() == nB + nR + nY);
						for (int i = 0; i < S.length(); ++i) {
							cout << S[i];
							if (S[i] == 'B' && !seenB) {
								seenB = true;
								for (int k = 0; k < O; ++k) {
									cout << "OB";
								}
							}
							if (S[i] == 'R' && !seenR) {
								seenR = true;
								for (int k = 0; k < G; ++k) {
									cout << "GR";
								}
							}
							if (S[i] == 'Y' && !seenY) {
								seenY = true;
								for (int k = 0; k < V; ++k) {
									cout << "VY";
								}
							}
						}
						cout << endl;
						//for (int i = 0; i < P[2].first; ++i) {
						//S.push_back(P[2].second);
						//S.push_back(i % 2 ? P[0].second : P[1].second);
						//}
						//used = P[2].first;
					}
				}
			}
		}
	}
	return 0;
}
