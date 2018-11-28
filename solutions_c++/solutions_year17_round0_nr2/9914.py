//============================================================================
// Name        : PractiseBeastX11.cpp
// Author      : neo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>



using namespace std;

#define _CRT_SECURE_NO_DEPRECATE

int MinMoves(vector<bool>& list, int flipsize)
{
	int countmoves = 0; int curr = flipsize;
	for (int i = list.size() - 1; i > flipsize -2  && i>= 0 ; --i)
	{
		if (i == flipsize - 2)
			break;
		if (list[i] == false)
		{
			countmoves++;
			for (int j = 0; j < flipsize; ++j)
			{
				list[i-j] = !list[i - j];
			}
		}

    }

	for (int i = list.size() - 1; i >= 0; --i)
		if (list[i] == false)
			return -1;

	return countmoves;

}

const int MAXSIZE = 1000;

char g[MAXSIZE];
int main() {
	


	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	//3
	//-- - +-++ - 3
	
	int T;
	cin >> T;
	//scanf_s("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {

		//scanf_s("%s", g);
		int flipsize;
		cin >> flipsize;
		int store = 0;
		
		for (int i = 1; i <= flipsize; ++i)
		{
			vector<int> digits;
			int curr = i;
			while (curr)
			{
				digits.push_back(curr % 10);
				curr /= 10;
			}
			bool res = true;
			for (int j = 1; j < digits.size(); ++j)
			{
				if (digits[j - 1] < digits[j])
				{
					res = false;
					break;
				}
					
			}
			if (res == true)
				store = i;
		}
	
		//scanf_s("%d", &flipsize);
		printf("Case #%d: %d\n", Ti, store);
		fflush(stdout);


	}
	fflush(stdout);




}
