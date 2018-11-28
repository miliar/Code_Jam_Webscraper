// CJE2.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <climits>

using namespace std;

void fix(vector<int>& arr, int ind)
{
	if (ind == 0)
		arr[ind]--;
	else
	{
		arr[ind]--;
		if (arr[ind] < arr[ind - 1])
		{
			arr[ind] = 9;
			fix(arr, ind - 1);
		}
	}
}



int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	long T, lp;
	long long ans;
	cin >> T;
	for (lp = 1;lp <= T;lp++)
	{
		unsigned long long N;
		cin >> N;
		int i, j;
		vector<int> arr;
		while (N > 0)
		{
			arr.push_back(N % 10);
			N /= 10;
		}
		reverse(arr.begin(), arr.end());

		vector<int> ans(arr.size());


		i = 0;
		while (i < arr.size() - 1 && arr[i] <= arr[i + 1])
		{
			
			i++;
		}

		if (i == arr.size() - 1)//all increasing
		{
			//cout << arr[i];
		}
		else//
		{
			fix(arr, i);
			i++;
			while (i < arr.size())
			{
				arr[i++] = 9;
			}
		}

		cout << "Case #" << lp << ": ";
		if (arr[0] == 0)
			i = 1;
		else
			i = 0;
		while (i < arr.size())
			cout << arr[i++];
		cout << "\n";



		
	}





	return 0;
}



