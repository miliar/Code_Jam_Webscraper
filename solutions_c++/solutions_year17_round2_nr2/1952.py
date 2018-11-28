// problemA.cpp : Defines the entry point for the console application.
//

#include <iostream> 
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <assert.h>

using namespace std;

void main() {
	int t = 0;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		int n;
		int r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		int R = r - g;
		int Y = y - v;
		int B = b - o;
		int minX = max(max(0, B - R), Y - R);
		int maxX = min(min(B, Y), Y - R + B);
		if (R < 0 
			|| Y < 0 
			|| B < 0 
			|| R > Y + B 
			|| Y > R + B 
			|| B > Y + R
			|| R == 0 && r > 0 && y + b > 0
			|| Y == 0 && y > 0 && r + b > 0
			|| B == 0 && b > 0 && y + r > 0
			|| minX > maxX)
		{
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}
		int YB = minX;
		int YR = Y - YB;
		int RY = R - B + minX;
		int RB = R - RY;
		int BY = Y - R + B - minX;
		int BR = B - BY;
		cout << "Case #" << i << ": ";
		char currLetter = 0;
		if (YB > 0 || YR > 0) {
			currLetter = 'Y';
		} else if (RY > 0 || RB > 0) {
			currLetter = 'R';
		} else if( BY > 0 || BR > 0 ) {
			currLetter = 'B';
		} else if (b > 0) {
			currLetter = 'B';
		} else if (r > 0) {
			currLetter = 'R';
		} else if (y > 0) {
			currLetter = 'Y';
		}
		while(n > 0) {
			if (currLetter == 'Y') {
				if (Y <= 1) {
					while (v > 0) {
						cout << "YV";
						y--;
						v--;
						n -= 2;
					}
				}
				if (Y > 0) {
					cout << "Y";
					Y--;
					y--;
					n--;
				}
				if (YB > YR) {
					YB--;
					currLetter = 'B';
				} else {
					YR--;
					currLetter = 'R';
				}
			}
			else if (currLetter == 'B') {
				if (B <= 1) {
					while (v > 0) {
						cout << "BO";
						b--;
						o--;
						n -= 2;
					}
				}
				if (B > 0) {
					cout << "B";
					B--;
					b--;
					n--;
				}
				if (BY > BR) {
					BY--;
					currLetter = 'Y';
				}
				else {
					BR--;
					currLetter = 'R';
				}
			} else {
				if (R <= 1) {
					while (g > 0) {
						cout << "RG";
						r--;
						g--;
						n -= 2;
					}
				}
				if (R > 0) {
					cout << "R";
					R--;
					r--;
					n--;
				}
				if (RY > RB) {
					RY--;
					currLetter = 'Y';
				} else {
					RB--;
					currLetter = 'B';
				}
			}

		}
		assert(n == 0);
		assert(y == 0);
		assert(r == 0);
		assert(b == 0);
		assert(o == 0);
		assert(g == 0);
		assert(v == 0);
		assert(B == 0);
		assert(R == 0);
		assert(Y == 0);
		assert(BR == 0);
		assert(RB == 0);
		assert(YB == 0);
		assert(BY == 0);
		assert(RY == 0);
		assert(YR == 0);
		cout << endl;
	}
}