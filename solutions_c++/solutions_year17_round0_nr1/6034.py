#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int numCases = 0;
    cin >> numCases;

    for (int q = 0; q < numCases; q++) {
	string s;
	cin >> s;
	int k;
	cin >> k;

	vector<char> pancakes;
	for (int i = 0; i < s.length(); i++) {
	    switch (s[i]) {
	    case '+':
		pancakes.push_back(1);
		break;
	    case '-':
		pancakes.push_back(0);
		break;
	    default:
		pancakes.push_back(0);
		break;
	    }
	}
	int i = 0;
	int num = 0;
	for (i = 0; i <= pancakes.size() - k; i++) {
	    if (!pancakes[i]) {
		for (int j = 0; j < k; j ++)
		    pancakes[i + j] ^= 1;
		num ++;
	    }
	}
	bool a = true;
	for (; i < pancakes.size(); i++) {
	    if (!pancakes[i]) {
		a = false;
		break;
	    }
	}
	if (a)
	    cout << "Case #" << q + 1 << ": " << num << endl;
	else
	    cout << "Case #" << q+1 << ": IMPOSSIBLE" << endl;
    }
}
