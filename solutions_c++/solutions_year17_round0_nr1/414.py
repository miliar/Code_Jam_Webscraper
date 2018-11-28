#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

#include "InfInt.h"

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int testCase = 1; testCase <= T; ++testCase)
	{
		string S;
		int K;
		cin >> S >> K;

		size_t pos = S.find('-');
		int result = 0;

		for (;pos != string::npos && pos + K <= S.length();++result,pos = S.find('-'))
		{
			for (int i = 0; i < K; ++i)
			{
				S[i + pos] = S[i + pos] == '+' ? '-' : '+';
			}
		}

		cout << "Case #" << testCase << ": ";
		if (pos == string::npos) cout << result; else cout << "IMPOSSIBLE";
		cout << endl;
	}

	return 0;
}
