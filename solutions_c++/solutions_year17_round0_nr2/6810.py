#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include <math.h>

using namespace std;

int main(){
	int N;
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		string ret;
		long long num;
		cin >> num;

		while (num != 0)
		{
			if (((num / 10) % 10) > num % 10)
			{
				for (int j = 0; j < ret.size(); j++)
				{
					ret.at(j) = '9';
				}
				ret = "9" + ret;
				num = num - 10;
				
			}
			else
			{
				ret = to_string(num % 10) + ret;
			}

			num /= 10;
		}

		cout << "Case #" << i + 1 << ": " << ret <<endl;

	}

	return 0;
}