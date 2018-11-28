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

bool isTidy(InfInt N)
{
	for (size_t i = 0; i < N.numberOfDigits() - 1; ++i)
	{
		if (N.digitAt(i) < N.digitAt(i + 1))
		{
			return false;
		}
	}
	return true;
}

int main()
{
	int T;
	cin >> T;
	for (int testCase = 1; testCase <= T; ++testCase)
	{
		InfInt N;
		cin >> N;
		for (int i = 0; i < N.numberOfDigits() - 1; ++i)
		{
			if (isTidy(N)) break;
			InfInt delta = N.digitAt(i) + 1;
			for (int j = 0; j < i; ++j) delta *= 10;
			N -= delta;
		}
		cout << "Case #" << testCase << ": " << N << endl;
	}

	return 0;
}
