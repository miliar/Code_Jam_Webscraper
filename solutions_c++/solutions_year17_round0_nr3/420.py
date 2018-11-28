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
		InfInt N, K;
		cin >> N >> K;

		while (K > 1)
		{
			N = K % 2 == 1 ? (N - 1) / 2 : N / 2;
			K /= 2;
		}

		cout << "Case #" << testCase << ": " << N/2 << " " << (N-1)/2 << endl;
	}

	return 0;
}
