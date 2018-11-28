// 2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <map>
#include <fstream>
#include <queue>
#include <sstream>
#include <string>
#include <algorithm>



using namespace std;

int main()
{
	freopen("B3.in", "r", stdin);
	freopen("2_out.txt", "w", stdout);

	int T; cin >> T;
	for (int tt = 1; tt <= T; ++tt)
	{
		int n, r, o, y, g, b, v;
		cin >> n>> r>> o>> y>> g>> b>> v;
		//r y b

		if(r>b+y || b>r+y || y>b+r) cout << "Case #" << tt << ": "<<"IMPOSSIBLE" << endl;
		else
		{
			cout << "Case #" << tt << ": ";
			if (r <= b && r <= y)
			{
				bool lr = true;
				bool lb = false;
				bool ly = false;
				if (r) {
					cout << "R";r--;
					 lr = true;
					 lb = false;
					 ly = false;
				}
				else {
					 lr = false;
					 lb = true;
					 ly = false;
				}
				while (r || b || y)
				{
					bool llb = lb;
					bool llr = lr;
					bool lly = ly;
			//		cerr << r << " " << b << " " << y << endl;
					if (llr)
					{
					//	if (!lr && r >= b && r >= y) { cout << "R"; r--; lr = true; lb = false; ly = false; }
					 if (b >= y) { cout << "B"; b--; lr = false; lb = true; ly = false;}
					 else { cout << "Y"; y--; lr = false; lb = false; ly = true; }
					}
					else if (llb)
					{
						if (r>=y) { cout << "R"; r--;  lr = true; lb = false; ly = false;}
						else{ cout << "Y"; y--; lr = false; lb = false; ly = true; }
					}
					else if (lly)
					{
						if (r >= b) { cout << "R"; r--;  lr = true; lb = false; ly = false; }
						else { cout << "B"; b--; lr = false; lb = true; ly = false; }
					}
				}
				cout << endl;
			}

			else if (b < r && b <= y)
			{
				
				
				bool lr = false;
				bool lb = true;
				bool ly = false;
				if (b)
				{
					cout << "B";b--;
				}
				else
				{
					lr = true;
					lb = false;
					ly = false;
				}
				
				while (r || b || y)
				{
					bool llb = lb;
					bool llr = lr;
					bool lly = ly;
				//	cerr << r << " " << b << " " << y << endl;
					if (llb)
					{
						if (r >= y) { cout << "R"; r--;  lr = true; lb = false; ly = false; } //!!
						else { cout << "Y"; y--; lr = false; lb = false; ly = true; }
					}
					else if (llr)
					{
						if (b >= y) { cout << "B"; b--; lr = false; lb = true; ly = false; }
						else { cout << "Y"; y--; lr = false; lb = false; ly = true; }
					}
					else if (lly)
					{
						if (r > b) { cout << "R"; r--;  lr = true; lb = false; ly = false; }
						else { cout << "B"; b--; lr = false; lb = true; ly = false; }
					}

				}
				cout << endl;
			}
			else
			{
				bool lr = false;
				bool lb = false;
				bool ly = true;
				if (y) {
					cout << "Y";y--;
				}
				else {
					 lr = false;
					 lb = true;
					 ly = false;
				}
				while (r || b || y)
				{
					bool llb = lb;
					bool llr = lr;
					bool lly = ly;
				//	cerr << r << " " << b << " " << y << endl;
					if (llb)
					{
						if (r > y) { cout << "R"; r--;  lr = true; lb = false; ly = false; } 
						else { cout << "Y"; y--; lr = false; lb = false; ly = true; }
					}
					else if (llr)
					{
						if (b > y) { cout << "B"; b--; lr = false; lb = true; ly = false; }
						else { cout << "Y"; y--; lr = false; lb = false; ly = true; }
					}
					 else if (lly)
					{
						if (r >= b) { cout << "R"; r--;  lr = true; lb = false; ly = false; } //!!
						else { cout << "B"; b--; lr = false; lb = true; ly = false; }
					}

				}
				cout << endl;

			}
		}
	}


	return 0;
}

