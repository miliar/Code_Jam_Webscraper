
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <limits>
#include <iomanip>
#include <cstdarg>
#define UINT64 unsigned __int64
using namespace std;
ifstream  fin("b.txt");
ofstream  fout("c.txt");
#define MAX(a,b) (((a) > (b)) ? (a) : (b))

UINT64 gArrayLoca[2000];
UINT64 gArraySpeed[2000];

// "", "ONE", "", "THREE", "", "", "", "SEVEN", "", "NINE"

char gAns[2000];

void solve(int n, int r, int o, int y, int g, int b, int v)
{
	int i;
	int j;
	int spB = 0;
	int spR = 0;
	int spY = 0;

	int tB = 0;
	int tR = 0;
	int tY = 0;


	bool bIsPossible = true;

	do
	{

		if (n == 1)
		{
			if (y)
			{
				fout << 'Y'<<endl;
			}
			else if (r)
			{
				fout << 'R' << endl;
			}
			else if (b)
			{
				fout << 'B' << endl;
			}
			else if (v)
			{
				fout << 'V' << endl;
			}
			else if (o)
			{
				fout << 'O' << endl;
			}
			else if (g)
			{
				fout << 'G' << endl;
			}
			
			break;
		}

		//spb
		if ((o > b && b != 0) || (o == b && b != 0 && n != (o + b)))
		{
			bIsPossible = false;

		}
		else
		{
			spB = o;
			//b--;
			b = b - o;
			n = n - o;
		}

		//spr
		if ((g > r && r != 0) || (g == r && r != 0 && n != (g + r)))
		{
			bIsPossible = false;

		}
		else
		{
			spR = g;
			//r--;
			r = r - g;
			n = n - g;
		}

		//spy
		if ((v > y && y != 0) || (v == y && y != 0 && n != (y + v)))
		{
			bIsPossible = false;

		}
		else
		{
			spY = v;
			//y--;
			y = y - v;
			n = n - v;
		}

		if (n / 2 < b && n != 1)
		{
			bIsPossible = false;
		}

		if (n / 2 < y && n != 1)
		{
			bIsPossible = false;
		}
		if (n / 2 < r&& n != 1)
		{
			bIsPossible = false;
		}

		int last = 0;
		int first = 0;
		//b 1
		//y 2
		//r 3
		if (bIsPossible)
		{
			for (i = 0; i <n; i++)
			{
				if (i == 1)
				{
					first = last;
				}

				if (((last == 3) && ((r > y  && r > b) == false) && ((y > r  && y > b) == false) && (first == 1)) || (b > r  && b > y) || ((first == 1) && (b >= r  && b >= y)))
				{
					if (last != 1 && spB)
					{
						for (j = 0; j< spB; j++)
						{
							fout << 'B';
							fout << 'O';
						}
						if (b)
						{
							fout << 'B';
							b--;
						}

						spB = 0;
						last = 1;
						continue;
					}

					if (last != 1 && b>0)
					{
						fout << 'B';
						b--;
						last = 1;
						continue;
					}

					if (last != 2 && spR)
					{
						for (j = 0; j< spR; j++)
						{
							fout << 'R';
							fout << 'G';
						}
						if (r)
						{
							fout << 'R';
							r--;
						}
						spR = 0;
						last = 2;
						continue;
					}

					if (last != 2 && r >0)
					{
						fout << 'R';
						r--;
						last = 2;
						continue;
					}

					if (last != 3 && spY)
					{
						for (j = 0; j< spY; j++)
						{
							fout << 'Y';
							fout << 'V';
						}
						if (y)
						{
							fout << 'Y';
							y--;
						}
						spY = 0;
						last = 3;
						continue;
					}

					if (last != 3 && y>0)
					{
						fout << 'Y';
						y--;
						last = 3;
						continue;
					}
				}
				else if ((last == 1 && (false == (r > b && r > y)) || (y > b && y > r)&& (first == 3)) || ((first == 3) && (y >= r  && y >= b)))

				{
					if (last != 3 && spY)
					{
						for (j = 0; j< spY; j++)
						{
							fout << 'Y';
							fout << 'V';
						}
						if (y)
						{
							fout << 'Y';
							y--;
						}
						spY = 0;
						last = 3;
						continue;
					}

					if (last != 3 && y>0)
					{
						fout << 'Y';
						y--;
						last = 3;
						continue;
					}

					if (last != 1 && spB)
					{
						for (j = 0; j< spB; j++)
						{
							fout << 'B';
							fout << 'O';
						}
						if (b)
						{
							fout << 'B';
							b--;
						}
						spB = 0;
						last = 1;
						continue;
					}

					if (last != 1 && b>0)
					{
						fout << 'B';
						b--;
						last = 1;
						continue;
					}

					if (last != 2 && spR)
					{
						for (j = 0; j< spR; j++)
						{
							fout << 'R';
							fout << 'G';
						}
						if (r)
						{
							fout << 'R';
							r--;
						}
						spR = 0;
						last = 2;
						continue;
					}

					if (last != 2 && r >0)
					{
						fout << 'R';
						r--;
						last = 2;
						continue;
					}

				}
				else
				{
					if (last != 2 && spR)
					{
						for (j = 0; j< spR; j++)
						{
							fout << 'R';
							fout << 'G';
						}
						if (r)
						{
							fout << 'R';
							r--;
						}
						spR = 0;
						last = 2;
						continue;
					}

					if (last != 2 && r >0)
					{
						fout << 'R';
						r--;
						last = 2;
						continue;
					}

					if (last != 3 && spY)
					{
						for (j = 0; j< spY; j++)
						{
							fout << 'Y';
							fout << 'V';
						}
						if (y)
						{
							fout << 'Y';
							y--;
						}
						spY = 0;
						last = 3;
						continue;
					}

					if (last != 3 && y>0)
					{
						fout << 'Y';
						y--;
						last = 3;
						continue;
					}

					if (last != 1 && spB)
					{
						for (j = 0; j< spB; j++)
						{
							fout << 'B';
							fout << 'O';
						}
						if (b)
						{
							fout << 'B';
							b--;
						}
						spB = 0;
						last = 1;
						continue;
					}

					if (last != 1 && b>0)
					{
						fout << 'B';
						b--;
						last = 1;
						continue;
					}

				}

			}

			fout << endl;
		}
		else
		{
			fout << "IMPOSSIBLE" << endl;
		}

	} while (false);


}


int main(void)
{
	int i;
	int j;
	int numOfTests;
	int k;
	int c;
	//int r;
	
	int length;
	int n;
	int r;
	int o;
	int y;
	int g;
	int v;
	int b;
//	UINT64 k;
	//UINT64 d;
	fin >> numOfTests;

	for (i = 0; i<numOfTests; i++)
	{
		fin >> n >> r >> o >> y >> g >> b>>v;

		fout << "Case #"<<i+1<<": ";
		solve(n, r, o, y, g, b, v);
	}
}
