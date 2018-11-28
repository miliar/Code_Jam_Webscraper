#include <stdio.h>
#include <stack>
#include <map>
#include <string.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <math.h>
#include <vector>
#include <set>
#include <queue>
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
//#define ld long double
const double sn = 1e-6;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("round1alarge.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int r, c;
		scanf("%d%d", &r, &c);
		char arr[35][35];
		for (int i = 0; i < r; i++) {
			scanf("%s", arr[i]);
		}
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (arr[i][j] == '?')
					continue;
				for (int k = j - 1; k >= 0; k--) {
					if (arr[i][k] == '?')
						arr[i][k] = arr[i][j];
					else
						break;
				}
				for (int k = j + 1; k < c; k++) {
					if (arr[i][k] == '?')
						arr[i][k] = arr[i][j];
					else
						break;
				}
			}
		}
		for (int i = 0; i < c; i++) {
			for (int j = 0; j < r; j++) {
				if (arr[j][i] == '?')
					continue;
				for (int k = j - 1; k >= 0; k--) {
					if (arr[k][i] == '?')
						arr[k][i] = arr[j][i];
					else
						break;
				}
				for (int k = j + 1; k < r; k++) {
					if (arr[k][i] == '?')
						arr[k][i] = arr[j][i];
					else
						break;
				}
			}
		}
		printf("Case #%d:\n", i+1);
		for (int i = 0; i < r; i++) {
			printf("%s\n", arr[i]);
		}
	}
	return 0;
}