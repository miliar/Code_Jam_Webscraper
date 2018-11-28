/*
Problem C. Bathroom Stalls
Confused? Read the quick-start guide.
Small input 1
5 points
Solve C-small-1
You may try multiple times, with penalties for wrong submissions.
Small input 2
10 points
You must solve small input 1 first.
You may try multiple times, with penalties for wrong submissions.
Large input
15 points
You must solve all small inputs first.
You have 8 minutes to solve 1 input file. (Judged after contest.)
Problem

A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other N stalls are for users.

Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible. To avoid confusion, they follow deterministic rules: For each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.

K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.

When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?

Solving this problem

This problem has 2 Small datasets and 1 Large dataset. You must solve the first Small dataset before you can attempt the second Small dataset. You will be able to retry either of the Small datasets (with a time penalty). You will be able to make a single attempt at the Large, as usual, only after solving both Small datasets.

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with two integers N and K, as described above.

Output

For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1), y is max(LS, RS), and z is min(LS, RS) as calculated by the last person to enter the bathroom for their chosen stall S.

Limits

1 ? T ? 100.
1 ? K ? N.
Small dataset 1

1 ? N ? 1000.
Small dataset 2

1 ? N ? 106.
Large dataset

1 ? N ? 1018.
Sample


Input

Output

5
4 2
5 2
6 2
1000 1000
1000 1

Case #1: 1 0
Case #2: 1 0
Case #3: 1 1
Case #4: 0 0
Case #5: 500 499

In Case #1, the first person occupies the leftmost of the middle two stalls, leaving the following configuration (O stands for an occupied stall and . for an empty one): O.O..O. Then, the second and last person occupies the stall immediately to the right, leaving 1 empty stall on one side and none on the other.

In Case #2, the first person occupies the middle stall, getting to O..O..O. Then, the second and last person occupies the leftmost stall.

In Case #3, the first person occupies the leftmost of the two middle stalls, leaving O..O...O. The second person then occupies the middle of the three consecutive empty stalls.

In Case #4, every stall is occupied at the end, no matter what the stall choices are.

In Case #5, the first and only person chooses the leftmost middle stall.
*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <array>
#include <queue>
#include <algorithm>
#include <sstream>
#include <array>
#include <stack> 
#include <tuple>
#include <assert.h>
#include <bitset>
#include <string.h>
#include <iomanip>

// #define SHOW
// #define TIME
#ifdef TIME
//#include <ctime>
#endif // TIME
// using ordered map
#include <map>
#include <set>
#include <unordered_map>

using namespace std;

void addValue(unordered_map<long long, int> &count, const long long idx, const int val)
{
	auto pnt = count.find(idx);
	if (pnt == count.end())
		count[idx] = val;
	else
		pnt->second += val; 
}


void bathroomStalls(int caseNumber)
{
	long long N, K; 
	cin >> N >> K;
	long long one = 1LL; 
	int level = 1; 
	vector<unordered_map<long long, int>> stalls;
	unordered_map<long long, int> l0stalls;
	l0stalls[N] = 1; // 1 stall of N span
	stalls.push_back(l0stalls);
	while (K >= (one << level))
	{
		unordered_map<long long, int> &oldStalls = stalls[level - 1];
		unordered_map<long long, int> newStalls;
		for (auto pair: oldStalls)
		{
			long long span = pair.first; 
			int num = pair.second; 
			long long minS = (span - 1) / 2;
			long long maxS = span - 1 - minS;
			addValue(newStalls, maxS, num);
			addValue(newStalls, minS, num);
		}
		stalls.push_back(newStalls);
		level++; 
	}


	long long span = N; 
	K -= (one << (level - 1));
	map<long long, int> lastLevelStalls(stalls[level - 1].begin(), stalls[level - 1].end());
	// Occupy stalls from the largest to the smallest. 
	for (auto pnt = lastLevelStalls.rbegin(); pnt != lastLevelStalls.rend(); pnt++ )
	{
		if (K < pnt->second)
		{
			span = pnt->first;
			break; 
		}
		else
		{
			K -= pnt->second; 
		}
	}

	long long minS, maxS; 
	if ( span >= 1)
	{
		minS = (span - 1) / 2;
		maxS = span - 1 - minS;
	}
	else
	{
		minS = maxS = 0; 
	}

	cout << "Case #" << caseNumber << ": " << maxS << " " << minS << endl; 
}

int main() {
#ifdef TIME
	auto t1 = clock();
#endif // TIME
	int numCases;
	cin >> numCases;
	for (int i = 1; i <= numCases; i++)
		bathroomStalls(i);

	return 0;
}