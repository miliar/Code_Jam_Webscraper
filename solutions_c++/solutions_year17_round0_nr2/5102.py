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

string solve(string nums)
{
	char max = '9';
	for (auto rit = nums.rbegin(); rit != nums.rend(); ++rit) {
		char c = *rit;
		if (c > max) {
			c = (c == '0') ? '9' : c - 1;
			*rit = c;

			for (auto it = rit.base(); it != nums.end() && *it != '9'; ++it)
				*it = '9';
		}
		max = c;
	}

	if (nums[0] == '0')
		nums.erase(0, 1);

    return nums;
}

int main(int argc, char *argv[])
{
    if (argc > 1) freopen(argv[1], "r", stdin);
    if (argc > 2) freopen(argv[2], "w", stdout);

    int numCases;
    cin >> numCases;

    int casei = 0;
	string nums;
    while (++casei, cin >> nums) {
        cout << "Case #" << casei << ": ";

		cout << solve(nums);

        cout << endl;
    }

    return 0;
}