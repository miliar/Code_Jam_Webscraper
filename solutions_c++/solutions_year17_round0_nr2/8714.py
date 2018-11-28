// GCJ 2017 Q b
// Template

#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;

#define REP(i,a,b) for(int i=a; i <b; i++)
#define MAX 60

// printf("");
// scanf("",&);


int T, cases;

FILE *stream1;
FILE *stream2;

int findUntidy(string str) {
	int i = 1;
	while (str[i] != 0) {
		//printf("%c,%c\n", str[i - 1], str[i]);
		if (str[i - 1] > str[i]) {
			return i;
		}
		i++;
	}
	return -1;

}


void fill(char* s, char c, int n) {
	int i = 0;
	for (i = 0; i < n; i++) {
		s[i] = c;
	}
	s[i] = 0;
}

int main() {

	freopen_s(&stream1, "B-large.in", "r", stdin);
	freopen_s(&stream2, "B-large.out", "w", stdout);

	cin >> T;
	//cin.ignore();
	while (cases++ < T) {
		string S = "";
		cin >> S;
		bool isTidy = false;
		while (!isTidy) {
			int i = findUntidy(S);
			if (i >= 0) {
				string front = S.substr(0, i);

				unsigned long long res = stoull(front) - 1;

				char behind[100];
				int len = S.length();
				//cout << len << i << endl;
				fill(behind, '9', len - i);
				if (res > 0)
				{
					S = to_string(res) + behind;
				}
				else {
					S = behind;
				}
			}
			else {
				isTidy = true;
			}
		}
		cout << "Case #" << cases << ": " << S << endl;
	}

	return 0;
}
