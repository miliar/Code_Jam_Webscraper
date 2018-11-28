// cruise.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <iomanip>

using namespace std;

int _DBG_LOG_ = 0;

char max3(int r, int b, int y, int r2, int b2, int y2)
{
	int ret = 'R';
	if(b > r)
	{
		ret = 'B';
		if(y > b)
		{
			ret = 'Y';
		}
		else if(y == b)
		{
			if(y2 > b2)
			{
				ret = 'Y';
			}
		}
	}
	else if(b == r)
	{
		if(y > r)
		{
			ret = 'Y';
		}
		else if(y == r) // all equal
		{
			if(b2 > r2)
			{
				ret ='B';
				if(y2 > b2)
				{
					ret = 'Y';
				}
			}
			else
			{
				if(y2 > r2)
				{
					ret = 'Y';
				}
			}
		}
		else //if(y < r) // b == r
		{
			if(b2 > r2)
			{
				ret = 'B';
			}
		}
	}
	else //if(b < r)
	{
		if(y > r)
		{
			ret = 'Y';
		}
		else if(y == r)
		{
			if(y2 > r2)
			{
				ret = 'Y';
			}
		}
	}

	return ret;
}

int main(int argc, char* argv[])
{
	// inputs
	int T, N, R, O, Y, G, B, V;
	
	string inFileName = "D:\\DEV\\VS2012\\GoogleCodeJam\\20170422\\02\\stable\\input.txt";

	ifstream inFile(inFileName);
	
	inFile >> T;

	for(int i = 0; i < T; i++)
	{
		inFile >> N >> R >> O >> Y >> G >> B >> V;

		// sanity check for small dataset
		if(O != 0 || G != 0 || V != 0)
		{
			int ff = 0;
			return 1/ff;
		}

		int max_allowed = N / 2;

		cout << "Case #" << i + 1 << ": ";
		if((R > max_allowed) || (B > max_allowed) || (Y > max_allowed))
		{
			cout << "IMPOSSIBLE";
		}
		else
		{
			int R2 = 0, B2 = 0, Y2 = 0;
			char last;
			
			// find first color
			char x = 'R';
			if(B > R)
			{
				x = 'B';
				if(Y > B)
				{
					x = 'Y';
				}
			}
			else
			{
				if(Y > R)
				{
					x = 'Y';
				}
			}
			// print first
			cout << x;
			last = x;
			N--;

			while(N > 0)
			{
				if(last == 'R')
				{
					R2++;
					R--;
					
					if(B > Y)
					{
						x = 'B';
					}
					else if(B < Y)
					{
						x = 'Y';
					}
					else
					{
						x = Y2 > B2 ? 'Y' : 'B';
					}
				}
				else if(last == 'B')
				{
					B2++;
					B--;
					
					if(R > Y)
					{
						x = 'R';
					}
					else if(R < Y)
					{
						x = 'Y';
					}
					else
					{
						x = Y2 > R2 ? 'Y' : 'R';
					}
				}
				else //if(last == 'Y')
				{
					Y2++;
					Y--;
					
					if(R > B)
					{
						x = 'R';
					}
					else if(R < B)
					{
						x = 'B';
					}
					else
					{
						x = B2 > R2 ? 'B' : 'R';
					}
				}

				cout << x;
				last = x;				
				N--;
			}
		}
		
		cout << endl;
	}

	return 0;
}

