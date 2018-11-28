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
    for (int t = 1; t <= T; ++t)
    {
		int D, N;
		cin >> D >> N;
		int *K = new int[N];
		int *S = new int[N];
		for (int i = 0; i < N; ++i)
		{
			cin >> K[i] >> S[i];
		}
		for (int i = 0; i < N; ++i)
			for (int j = i+1; j < N; ++j)
				if (K[i] < K[j]) {
					std::swap(K[i], K[j]);
					std::swap(S[i], S[j]);
				}

		double maxTime = 0.0;
		for (int i = 0; i < N; ++i)
		{
			double time = (D - K[i]) / (double)S[i];
			if (time > maxTime) maxTime = time;
		}

        cout << "Case #" << t << ": " << std::setprecision(17) << D / maxTime << endl;
    }

    return 0;
}
