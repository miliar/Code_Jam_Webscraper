#include <iostream>
#include <tuple>
#include <sstream>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <memory>
#include <array>

using namespace std;

int solve(std::string cakes, int n)
{
	int flips = 0;
	int i = 0;
	while (i < cakes.size()) {
		if (cakes[i] == '+') {
			++i;
		} else {
			if (i + n > cakes.size())
				break;
			for (int j = i; j < i + n; ++j)
				cakes[j] = (cakes[j] == '+') ? '-' : '+';
			++flips;
		}
	}

	return (i != cakes.size()) ? -1 : flips;
}

int main(int argc, char *argv[])
{
    if (argc > 1) freopen(argv[1], "r", stdin);
    if (argc > 2) freopen(argv[2], "w", stdout);

    int numCases;
    cin >> numCases;

    int casei = 0;
	
	string cakes;
	int n;
    while (++casei, cin >> cakes >> n) {
		cout << "Case #" << casei << ": ";

		int sol = solve(cakes, n);
		if (sol < 0)
			cout << "IMPOSSIBLE";
		else
			cout << sol;

		cout << endl;
    }

    return 0;
}