#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>


using namespace std;


long long lastNum(long long val) {
    long long pos = 9;
    long long rem = 10;
    long long res = 0;
    long long tens = 1;
    while (val > 0) {
        if (val%rem < (val/10)%rem) {
            res = pos;
            val = val - 10;
        } else {
            res += (val%rem)*tens;
        }
        tens *= 10;
        pos = pos*10 + 9;
        val /= 10;
    }
    return res;
}

int main() {
    string name = "B-large";
	string path = "";

	freopen((path + name + ".in").c_str(), "r", stdin);
	freopen((path + name + ".out").c_str(), "w", stdout);


	int N; // test cases
	cin >> N;
	for (int prob = 1; prob <= N; prob++) {
		long n; // last number counted
        cin >> n;
        cout << "Case #" << prob << ": " << lastNum(n) << "\n";
	}

	return 0;
}
