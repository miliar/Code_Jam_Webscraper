/*
CodeJam 1C
Problem A. Ample Syrup
Confused? Read the quick-start guide.
Small input
9 polong longs
Solve A-small
You may try multiple times, with penalties for wrong submissions.
Large input
16 polong longs
You must solve the small input first.
You have 8 minutes to solve 1 input file. (Judged after contest.)
Problem

The kitchen at the Infinite House of Pancakes has just received an order for a stack of K pancakes! The chef currently has N pancakes available, where N ? K. Each pancake is a cylinder, and different pancakes may have different radii and heights.

As the sous-chef, you must choose K out of the N available pancakes, discard the others, and arrange those K pancakes in a stack on a plate as follows. First, take the pancake that has the largest radius, and lay it on the plate on one of its circular faces. (If multiple pancakes have the same radius, you can use any of them.) Then, take the remaining pancake with the next largest radius and lay it on top of that pancake, and so on, until all K pancakes are in the stack and the centers of the circular faces are aligned in a line perpendicular to the plate, as illustrated by this example:

A stack of pancakes with varying radii and thicknesses, obeying the rules in the statement.

You know that there is only one thing your diners love as much as they love pancakes: syrup! It is best to maximize the total amount of exposed pancake surface area in the stack, since more exposed pancake surface area means more places to pour on delicious syrup. Any part of a pancake that is not touching part of another pancake or the plate is considered to be exposed.

If you choose the K pancakes optimally, what is the largest total exposed pancake surface area you can achieve?

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each begins with one line with two long longegers N and K: the total number of available pancakes, and the size of the stack that the diner has ordered. Then, N more lines follow. Each contains two long longegers Ri and Hi: the radius and height of the i-th pancake, in millimeters.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum possible total exposed pancake surface area, in millimeters squared. y will be considered correct if it is within an absolute or relative error of 10-6 of the correct answer. See the FAQ for an explanation of what that means, and what formats of real numbers we accept.

Limits

1 ? T ? 100.
1 ? K ? N.
1 ? Ri ? 106, for all i.
1 ? Hi ? 106, for all i.
Small dataset

1 ? N ? 10.
Large dataset

1 ? N ? 1000.
Sample


Input

Output

4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4

Case #1: 138230.076757951
Case #2: 150796.447372310
Case #3: 43982.297150257
Case #4: 625.176938064

In Sample Case #1, the "stack" consists only of one pancake. A stack of just the first pancake would have an exposed area of ? × R02 + 2 × ? * R0 × H0 = 14000? mm2. A stack of just the second pancake would have an exposed area of 44000? mm2. So it is better to use the second pancake.

In Sample Case #2, we can use both of the same pancakes from case #1. The first pancake contributes its top area and its side, for a total of 14000? mm2. The second pancake contributes some of its top area (the part not covered by the first pancake) and its side, for a total of 34000? mm2. The combined exposed surface area is 48000? mm2.

In Sample Case #3, all of the pancakes have radius 100 and height 10. If we stack two of these together, we effectively have a single new cylinder of radius 100 and height 20. The exposed surface area is 14000? mm2.

In Sample Case #4, the optimal stack uses the pancakes with radii of 8 and 9.
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
#define _USE_MATH_DEFINES
#include <math.h>

// #define SHOW
#define TIME
#ifdef TIME
//#include <ctime>
#endif // TIME
// using ordered map
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

using namespace std;

bool comparePancake(const pair<long long, long long> &p1, const pair<long long, long long> &p2)
{
	const long long R1 = p1.first;
	const long long H1 = p1.second;
	const long long R2 = p2.first;
	const long long H2 = p2.second;
	const long long RH1 = R1 * H1; 
	const long long RH2 = R2 * H2; 
	if (RH1 < RH2)
		return true;
	else if (RH1 > RH2)
		return false;
	else
		return R1 < R2; 
}

bool compareR(const pair<long long, long long> &p1, const pair<long long, long long> &p2)
{
	const long long R1 = p1.first;
	const long long H1 = p1.second;
	const long long R2 = p2.first;
	const long long H2 = p2.second;
	if (R1 < R2)
		return true;
	else if (R1 > R2)
		return false;
	else
		return H1 < H2; 
}

void ampleSyrup(long long caseNumber)
{
	auto t1 = clock();
	int N, K;
	cin >> N >> K;
	vector<pair<long long,long long>> pancakes(N);
	for (int i = 0; i < N; i++)
	{
		long long R, H; 
		cin >> R >> H;
		pancakes[i] = make_pair(R, H);
	}

	sort(pancakes.begin(), pancakes.end(), comparePancake);

	// Max R of the pancakes. 
	long long maxR = 0;
	double sumRH = 0.0; 
	long long smallestRH = numeric_limits<long long>::max(); 
	int k = N - 1;
	for (; k >= N - K; k--)
	{
		long long R = pancakes[k].first; 
		long long H = pancakes[k].second;
		if (maxR < R)
		{
			maxR = R; 
		}
		long long thisRH = 2 * R * H;
		sumRH += M_PI * thisRH;
		smallestRH = thisRH; 
	}
	sumRH += M_PI * maxR * maxR; 
	
	// Any improvement?
	for (; k >= 0; k--)
	{
		long long R = pancakes[k].first;
		long long H = pancakes[k].second;
		long long thisRH = 2 * R * H;
		if (R > maxR)
		{
			// possible if this pancake has a larger radius. 
			if (R * R + thisRH > maxR * maxR + smallestRH)
			{
				sumRH += M_PI * ( R * R + thisRH - maxR * maxR - smallestRH) ;
				smallestRH = thisRH;
				maxR = R; 
			}
		}
	}

	cout.precision(10);
	cout << "Case #" << caseNumber << ": "<< fixed << sumRH<<endl;
}

int main() {
#ifdef TIME
	auto t1 = clock();
#endif // TIME
	long long numCases;
	cin >> numCases;
	for (long long i = 1; i <= numCases; i++)
		ampleSyrup(i);

	return 0;
}