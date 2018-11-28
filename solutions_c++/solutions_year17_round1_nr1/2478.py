/*
ID: meet2dinesh
PROG: 
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>


using namespace std;


int main() {
	//ofstream fout("outp.txt");
	//ifstream fin("gift1.in");
//	ifstream fin("input.txt");
	int T;// N, Nn;

	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int R, C;
		char cake[25][25];
		cin >> R >> C;
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				cin >> cake[i][j];

		int total = R*C, used[25][25], use = 0;
		char ch ;
		memset((char*)used, 0, 25*25*sizeof(int));
	//	while (use < total)
		{
			for (int i = 0; i < R; i++)
				for (int j = 0; j < C; j++)
				{
					if (used[i][j] == 0 && cake[i][j] >= 'A' && cake[i][j] <= 'Z')
					{//now try to fill this max in a row
						// mark used
						used[i][j] = 1;
						ch = cake[i][j];
						int j_left = j, j_right = j;
						//go back
						for (int jj = j - 1; jj >= 0 && used[i][jj] == 0 && cake[i][jj] == '?'; jj--)
						{
							cake[i][jj] = ch;
							used[i][jj] = 1;
							j_left = jj;
						}
						//go forwrd
						for (int jj = j + 1; jj < C && used[i][jj] == 0 && cake[i][jj] == '?'; jj++)
						{
							cake[i][jj] = ch;
							used[i][jj] = 1;
							j_right = jj;
						}
						//fill up
						
						for (int ii = i - 1; ii >= 0; ii--)
						{
							int check = 0;
							//check available
							for (int jj = j_left; jj <= j_right; jj++)
							{
								if (used[ii][jj] == 1 || cake[ii][jj] != '?')
								{
									check = 1;
									break;								}
							}
							//fill now
							if (check == 0)
							{
								for (int jj = j_left; jj <= j_right; jj++)
								{
									cake[ii][jj] = ch;
									used[ii][jj] = 1;
								}
							}
							else
								break;
						}

						//fill down
						for (int ii = i + 1; ii < R; ii++)
						{
							int check = 0;
							//check available
							for (int jj = j_left; jj <= j_right; jj++)
							{
								if (used[ii][jj] == 1 || cake[ii][jj] != '?')
								{
									check = 1;
									break;
								}
							}
							//fill now
							if (check == 0)
							{
								for (int jj = j_left; jj <= j_right; jj++)
								{
									cake[ii][jj] = ch;
									used[ii][jj] = 1;
								}
							}
							else
							{
								break;
							}
						}
					}
				}
		}
		
		cout << "Case #" << i + 1 <<":"<< endl;
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				cout << cake[i][j];
			}
			cout << endl;
		}
		
	}
	return 0;
}