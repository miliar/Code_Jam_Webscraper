#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

void swap(vector<int>& r, int i, int j)
{
	int temp = r[i];
	r[i] = r[j];
	r[j] = temp;
}

int main()
{
	const double eps = 1e-6;
	
	ifstream input;
	input.open("B-large.in");
	
	ofstream output;
	output.open("output.txt");
	
	int t;
	long long n, val;
	input >> t;
	
	for (int i = 1; i <= t; i++)
	{
		input >> n;
		
		val = n;

		long long divisor = 1, prev_divisor = 1, digit = 0, prev_digit = 10;

		do
		{
			prev_divisor = divisor;
			divisor *= 10;
			digit = (val % divisor) / prev_divisor;
			if (digit > prev_digit)
			{
				val = (val / divisor) * divisor + digit * prev_divisor - 1;
				prev_digit = (val % divisor) / prev_divisor;
			}
			else
			{
				prev_digit = digit;
			}
		} while (divisor <= val);
		
		output << "Case #" << i << ": " << val << "\n";
	}
	return 0;
}