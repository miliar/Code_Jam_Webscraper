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

int main() {
    string name = "A-large";
	string path = "";

	freopen((path + name + ".in").c_str(), "r", stdin);
	freopen((path + name + ".out").c_str(), "w", stdout);


	int N;
	cin >> N;
	for (int prob = 1; prob <= N; prob++) {
        double maxSpeed;
        double maxTime = 0;
        double time;
        double d;
        double k, s;
        int n;

        cin >> d >> n;
        for (int i = 0; i < n; ++i) {
            cin >> k >> s;
            time = (d - k)/s;
            if (time > maxTime)
                maxTime = time;
        }

		printf("Case #%d: %f\n", prob, (d/maxTime));


	}

	return 0;
}
