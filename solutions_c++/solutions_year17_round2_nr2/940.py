#include <iostream>
#include <queue>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <cmath>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

	double col[50][50];
	int R[50];
void printcl(int r, int c)
{
	 for (int i = 0; i < r; i++)
	 {
		 for (int j = 0; j < c; j++)
			 cout << col[i][j];
		 cout << endl;
	 }

}


void p1(int begx, int begy, int endx, int endy)
{
	 int letter = 0;
	 char ch;
	 for (int i = begx; i != endx; i++)
		 for (int j = begy; j != endy; j++)
		 {
		 	if (col[i][j] != '?')
			 {
			   letter++;
			   ch = col[i][j];
	   		   }
		 }
	 //cout << begx << begy << endx << endy << endl;
	 //printcl(4, 4);
	 int a;
	 //cin >> a;
	 if (letter == 1)
	 {
		for (int i = begx; i != endx; i++)
			for (int j = begy; j != endy; j++)
				col[i][j] = ch;
	 }
	 else
	 {
		 for (int i = begx; i != endx; i++)
			 for (int j = begy; j != endy; j++)
			 {
				 if (col[i][j] != '?')
				 {
				 	if (endy - begy > 1)
				 	{
					p1(begx, begy, endx, j + 1);
					p1(begx, j + 1, endx, endy);
					}
                    else
                    {
					 p1(begx, begy, i + 1, endy);
					 p1(i + 1, begy, endx, endy);
					}
					return;
				 }
			 }
	 }
}

int findmin(int n)
{
	int min = 0;
	for (int i = 0; i < n; i++)
		if (col[i][R[i]] < col[min][R[min]])
		   min = i;
	return min;
}

bool check(string s)
{
	if (s.size() <= 2) return true;
	char last = s[0];
	for (int i = 1; i < s.size(); i++)
	{
		if (last == s[i]) return false;
		last = s[i];
	}
	return s[0] != s[s.size() - 1];
}

char A[6] = { 'R', 'O', 'Y', 'G', 'B', 'V' };
int main()
{
	ifstream ifs;
	ofstream ofs;
	ifs.open("B-large.in");
	ofs.open("B-large.out");

	int T;
	ifs >> T;
	for (int i = 1; i <= T; i++)
	{
		int a[6], N, M = 0;
		ifs >> N;
		for (int j = 0; j < 6; j++)
		{
			ifs >> a[j];
			M = max(a[j], M);
		}

		if (M > (N >> 1))
		{
			ofs << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}
		int n = N, r = a[0] - a[3], y = a[2] - a[5], b = a[4] - a[1];

		if (r < 0 || y < 0 || b < 0 || r > y + b || y > r + b || b > r + y)
		{
			ofs << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}
		if (a[0] == a[3] && a[0] != 0 && N > a[0] * 2)
		{
			ofs << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}
		if (a[2] == a[5] && a[5] != 0 && N > a[5] * 2)
		{
			ofs << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}
		if (a[4] == a[1] && a[4] && N > a[4] * 2)
		{
			ofs << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}


		string ret;
		string RG;
		for (int j = 0; j < a[3] * 2 + (a[3] != a[0]); j++)
		{
			if (j & 1)
				RG += 'G';
			else RG += 'R';
		}

		string VY;
		for (int j = 0; j < a[5] * 2 + (a[5] != a[2]); j++)
			if (j & 1)
				VY += 'V';
			else
				VY += 'Y';

		string OB;
		for (int j = 0; j < a[1] * 2 + (a[4] != a[1]); j++)
			if (j & 1)
				OB += 'O';
			else
				OB += 'B';

		a[0] -= a[3];
		a[2] -= a[5];
		a[4] -= a[1];
		n = a[0] + a[2] + a[4];
		if (n == 0)
		{
			ret = a[3] != 0 ? RG : (a[5] != 0 ? VY : OB);
		}
		else
		{
			M = -1;
			if (a[0] >= a[2] && a[0] >= a[4])
				M = 0;
			else if (a[2] >= a[0] && a[2] >= a[4])
				M = 2;
			else
				M = 4;

			for (int j = 0; j < a[M]; j++)
				ret += A[M];

			M = (M + 2) % 6;
			for (int j = 0; j < a[M]; j++)
				ret.insert(j * 2 + 1, 1, A[M]);

			M = (M + 2) % 6;
			for (int j = 0; j < a[M]; j++)
				ret.insert(ret.size() - j * 2, 1, A[M]);


			for (int j = 0; j < ret.size(); j++)
				if (ret[j] == 'R')
				{
					ret.replace(j, 1, RG);
					break;
				}
			for (int j = 0; j < ret.size(); j++)
				if (ret[j] == 'Y')
				{
					ret.replace(j, 1, VY);
					break;
				}
			for (int j = 0; j < ret.size(); j++)
				if (ret[j] == 'B')
				{
					ret.replace(j, 1, OB);
					break;
				}
		}
		cout << i << ":" << check(ret) << endl;
		ofs << "Case #" << i << ": " << ret << endl;


	}
	cin >> T;
	ifs.close();
	ofs.close();
	return 0;
}


