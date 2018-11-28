#include <fstream>
#include <iostream>
#include <list>
#include <limits>
#include <map>
#include <algorithm>
#include <sstream>
#include <string>
#include <iomanip>
#include <vector>

using namespace std;

int main()
{
	ofstream myfile;
	ifstream myReadFile;
	myReadFile.open("text.txt");
	myfile.open("b_small_out.txt");
	int t;
	  
	if (myReadFile.is_open()) 
	{
		while (!myReadFile.eof())
		{
			myReadFile >> t;
			cout << "t= " << t << " read\n";
			for (int i = 1; i <= t; ++i)
			{
				myfile << "Case #" << i << ": ";
				cout << "Case #" << i << ": ";
				// N, R, O, Y, G, B, and V.
			
				int n, r, b, y, dummy1, dummy2, dummy3;
				myReadFile >> n >> r >> dummy1 >> y >> dummy2 >> b >> dummy3;
				cout << r << " " << y << " " << b << endl;
				if (r > n / 2 || y > n / 2 || b > n / 2)
				{
					myfile << "IMPOSSIBLE\n";
				}
				else
				{
					cout << "possible \n";
					vector<pair<int, char> > mine;
					pair<int, char> rr = make_pair(r, 'R');
					pair<int, char> yy = make_pair(y, 'Y');
					pair<int, char> bb = make_pair(b, 'B');
					mine.push_back(rr); mine.push_back(yy); mine.push_back(bb);
					std::sort(mine.begin(), mine.end());
					int initialPart = mine[1].first + mine[0].first - mine[2].first;
					for (int h = 0; h < initialPart; ++h)
						myfile << mine[2].second << mine[1].second << mine[0].second;
					for (int h = 0; h < mine[1].first - initialPart; ++h)
						myfile << mine[2].second << mine[1].second;
					for (int h = 0; h < mine[0].first - initialPart; ++h)
						myfile << mine[2].second << mine[0].second;
					myfile << endl;
				}
				if (i == t)
					return 0;
			}
		}
	}
	else
	{
		cout << "could not open file\n";
	}
	myfile.close();
}







	