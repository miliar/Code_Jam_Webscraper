#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int caseNum = 1; caseNum <= t; caseNum++) {
		int n, p;
		int r[50], q[50][50];
		cin >> n >> p;
		for(int i = 0; i < n; i++)
			cin >> r[i];
		for(int i = 0; i < n; i++)
			for(int j = 0; j < p; j++)
				cin >> q[i][j];
		for(int i = 0; i < n; i++)
			sort(q[i], q[i] + p);
		int currentIndex[50] = {};
		int numKits = 0;
		bool hasStopped = false;
		while(!hasStopped) {
			int minServings = 1;
			for(int i = 0; i < n; i++) {
				int package = q[i][currentIndex[i]];
				int minRequiredAmount = package * 10 / 11;
				if(minRequiredAmount + minRequiredAmount / 10 < package)
					minRequiredAmount++;
				int servings = minRequiredAmount / r[i];
				if(servings * r[i] < minRequiredAmount)
					servings++;
				if(servings > minServings)
					minServings = servings;
			}
			bool isTooLittle = false;
			for(int i = 0; i < n; i++) {
				if(10 * q[i][currentIndex[i]] < 9 * minServings * r[i]) {
					isTooLittle = true;
					currentIndex[i]++;
					if(currentIndex[i] >= p)
						hasStopped = true;
				}
			}
			if(!isTooLittle) {
				numKits++;
				for(int i = 0; i < n; i++) {
					currentIndex[i]++;
					if(currentIndex[i] >= p)
						hasStopped = true;
				}
			}
		}
		cout << "Case #" << caseNum << ": " << numKits << endl;
	}
	return 0;
}
