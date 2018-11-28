#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <algorithm>
#include <string>
#include <memory.h>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
#include <queue>
#include <numeric>
#include <math.h>
#include <fstream>
#include <set>

using namespace std;

#define PI 3.14159265358979323846264338327950288419716939937510

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int qqq;
	cin >> qqq;
	for (int qq = 0; qq < qqq; qq++)
	{
		cout << "Case #" << qq+1 << ": ";
		int ac, aj;
		cin >> ac >> aj;
		vector <pair <int, int> > q;
		vector <int> ans(1440, 0);
		for (int i = 0; i < ac; i++)
		{
			int st, fin;
			cin >> st >> fin;
			q.push_back(make_pair(st, fin));
			for (int j = st; j < fin; j++)
			{
				ans[j] = 1;
			}
		}
		for (int i = 0; i < aj; i++)
		{
			int st, fin;
			cin >> st >> fin;
			q.push_back(make_pair(st, fin));
			for (int j = st; j < fin; j++)
			{
				ans[j] = 1;
			}
		}
		if (ac != 2 && aj != 2)
		{
			cout << 2 << endl;
		}
		else
		{

			if (q[0].first > q[1].first)
				swap(q[0], q[1]);
			vector <int> try1 = ans;
			for (int j = q[0].second; j < q[1].first; j++)
				ans[j] = 2;
			vector <int> sum(3, 0);
			for (auto x :ans)
			{
				sum[x]++;
			}
			if (sum[2]>=720 || sum[0]>=720)
			{
				cout << 2 << endl;
			}
			else
			{
				cout << 4 << endl;
			}
		}

	}




}