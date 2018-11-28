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
	


	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	//3
	//-- - +-++ - 3
	
	int T;
	cin >> T;
	//scanf_s("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {

		//scanf_s("%s", g);
		int flipsize;
		cin >> g >> flipsize;
		vector<bool> digits;
		
		for (int j = 0; j < MAXSIZE; ++j)
		{

			char temp = g[j];
			if (temp == '\0')
				break;
			if (temp == '+')
				digits.push_back(true);
			else
				digits.push_back(false);
		}
		//scanf_s("%d", &flipsize);

		int res = MinMoves(digits,flipsize);
		string simp = "IMPOSSIBLE";
		if(res == -1)
			printf("Case #%d: IMPOSSIBLE\n", Ti);
		else
            printf("Case #%d: %d\n", Ti, res);
		fflush(stdout);


	}
	fflush(stdout);




}
