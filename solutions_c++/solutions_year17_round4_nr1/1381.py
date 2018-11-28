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
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int caseNum = 1; caseNum <= t; caseNum++) {
		int n, p;
		int groups[4];
		cin >> n >> p;
		for(int i = 0; i < n; i++) {
			int numPeople;
			cin >> numPeople;
			groups[numPeople % p]++;
		}
		int answer = 0;
		answer += groups[0];
		groups[0] = 0;
		for(int i = 1; i < p; i++) {
			int remainder = p - i;
			if(remainder == i) {
				answer += groups[i] / 2;
				groups[i] %= 2;
			}
			else {
				int groupsTogether = min(groups[i], groups[remainder]);
				answer += groupsTogether;
				groups[i] -= groupsTogether;
				groups[remainder] -= groupsTogether;
			}
		}
		int leftover = 0;
		for(int i = 1; i < p; i++) {
			while(groups[i] > 0) {
				if(leftover == 0) {
					answer++;
				}
				leftover += i;
				leftover %= p;
				groups[i]--;
			}
		}
		cout << "Case #" << caseNum << ": " << answer << endl;
	}
	return 0;
}
