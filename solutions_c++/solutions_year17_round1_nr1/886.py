#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <deque>
#include <string>
using namespace std;
#define txt
#ifdef txt
ofstream out("out.txt");
ifstream in("in.txt");
#else
ofstream& out = cout;
ofstream& in = cin;
#endif

int main()
{
	int T;
	in >> T;

	for (int cn = 1; cn <= T; cn++)
	{
		int R, C;
		vector<string> Grid;
		string temp;
		in >> R >> C;

		Grid.reserve(R);
		for (int i = 0; i < R; i++)
		{
			in >> temp;
			Grid.push_back(temp);
		}
		

		vector<int> row_n(R);
		for (int i = 0; i < R; i++)
		{
			const char* t_c = Grid[i].c_str();
			for (int j = 0; j < C; j++)
				if (t_c[j] != '?') row_n[i]++;
		}

		for (int i = 0; i < R; i++)
		{
			if (row_n[i] != 0 && row_n[i] != C)
			{
				for (int j = 1; j < C; j++)
					if (Grid[i][j] == '?')
						Grid[i][j] = Grid[i][j - 1];
				for (int j = C - 2; j > -1; j--)
					if (Grid[i][j] == '?')
						Grid[i][j] = Grid[i][j +1];

			}
		}
		
		for (int i = 1; i < R;i++)
			if (row_n[i] == 0)
			{
				Grid[i] = Grid[i - 1];
				if(Grid[i][0]!='?')row_n[i] = C;
			}
		for (int i = R - 2; i > -1; i--)
			if (row_n[i] == 0)
			{
				Grid[i] = Grid[i +1];
			}

		out << "Case #" << cn << ":"<<endl;
		for (int i = 0; i < R; i++)
			out << Grid[i] << endl;

			
	}
}