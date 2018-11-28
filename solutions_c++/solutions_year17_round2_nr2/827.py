#include <iostream>
#include <cstdio>
#include <stack>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <set>

#define INF 2000000000

using namespace std;

int n, r, o, y, g, b, v;

int arr[6];
char c[6] = {'R', 'Y', 'B', 'G', 'V', 'O'};
//{R, O, Y, G, B, V}.
int main() {
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum << ": ";
		cin >> n;
		vector<char> vec;
		cin >> arr[0] >> arr[5] >> arr[1] >> arr[3] >> arr[2] >> arr[4];
		bool done = false;
		for (int i = 0; i < 3; i++) {
			if (arr[i] < arr[i + 3]) {
				done = true;
				cout << "IMPOSSIBLE" << endl;
				break;
			}
			if (arr[i] == arr[i + 3] && arr[i] > 0) {
				done = true;
				if (arr[i] + arr[i + 3] == n) {
					for (int j = 0; j < arr[i]; j++) 
						cout << c[i] << c[i + 3];
					cout << endl;
				}
				else {
					cout << "IMPOSSIBLE" << endl;
				}
				break;
			}
		}
		if (done)
			continue;
		for (int i = 0; i <= arr[3]; i++) {
			int cnt = 0;
			int fl = 0;
			if (i > 0) {
				cnt = i + 1;
				fl = 1;
			}
			if (arr[0] < cnt + (arr[3] - i) * 2)
				continue;
			r = arr[0] - (cnt + (arr[3] - i) * 2) + fl + (arr[3] - i);
			for (int j = 0; j <= arr[4]; j++) {
				int cnt1 = 0;
				int fl1 = 0;
				if (j > 0) {
					cnt1 = j + 1;
					fl1 = 1;
				}
				if (arr[1] < cnt1 + (arr[4] - j) * 2)
					continue;
				y = arr[1] - (cnt1 + (arr[4] - j) * 2) + fl1 + (arr[4] - j);
				for (int k = 0; k <= arr[5]; k++) {
					if (done)
						continue;
					int cnt2 = 0;
					int fl2 = 0;
					if (k > 0) {
						cnt2 = k + 1;
						fl2 = 1;
					}
					if (arr[2] < cnt2 + (arr[5] - k) * 2)
						continue;
					b = arr[2] - (cnt2 + (arr[5] - k) * 2) + fl2 + (arr[5] - k);
					pair<int, char> p[3];
					p[0] = make_pair(r, 'R');
					p[1] = make_pair(y, 'Y');
					p[2] = make_pair(b, 'B');
					sort(p, p + 3);
					reverse(p, p + 3);
					if (p[0].first > p[1].first + p[2].first)
						continue;
					for (;p[0].first > 0;) {
						vec.push_back(p[0].second);
						p[0].first--;
						if (p[1].first > p[2].first) {
							vec.push_back(p[1].second);
							p[1].first--;
						}
						else {
							vec.push_back(p[2].second);
							p[2].first--;
						}
					}
					while (p[1].first + p[2].first > 0) {
						if (p[1].first > p[2].first) {
							vec.push_back(p[1].second);
							p[1].first--;
						}
						else {
							vec.push_back(p[2].second);
							p[2].first--;
						}
					}
					bool rr = false, yy = false, bb = false;
					int cntr = 0, cnty = 0, cntb = 0;
					for (int w = 0; w < vec.size(); w++) {
						if (vec[w] == 'R') {
							if (i > 0) {
								if (!rr) {
									for (int ww = 0; ww < i; ww++) 
										cout << "RG";
									cout << "R";
									cntr += i;
								}
								else {
									if (arr[3] > cntr) {
										cout << "RGR";
										cntr++;
									}
									else {
										cout << "R";
										cntr++;
									}
								}
							}
							else if (arr[3] > cntr) {
								cout << "RGR";
								cntr++;
							}
							else {
								cout << "R";
								cntr++;
							}
							rr = true;
						}
						if (vec[w] == 'Y') {
							if (j > 0) {
								if (!yy) {
									for (int ww = 0; ww < j; ww++) 
										cout << "YV";
									cout << "Y";
									cnty += j;
								}
								else {
									if (arr[4] > cnty) {
										cout << "YVY";
										cnty++;
									}
									else {
										cout << "Y";
										cnty++;
									}
								}
							}
							else if (arr[4] > cnty) {
								cout << "YVY";
								cnty++;
							}
							else {
								cout << "Y";
								cnty++;
							}
							yy = true;
						}
						if (vec[w] == 'B') {
							if (k > 0) {
								if (!bb) {
									for (int ww = 0; ww < k; ww++) 
										cout << "BO";
									cout << "B";
									cntb += k;
								}
								else {
									if (arr[5] > cntb) {
										cout << "BOB";
										cntb++;
									}
									else {
										cout << "B";
										cntb++;
									}
								}
							}
							else if (arr[5] > cntb) {
								cout << "BOB";
								cntb++;
							}
							else {
								cout << "B";
								cntb++;
							}
							bb = true;
						}
					}
					cout << endl;
					done = true;
				}
			}
		}
 		if (!done) {
			cout << "IMPOSSIBLE" << endl;
		}		
	}
	return 0;
}