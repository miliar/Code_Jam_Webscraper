#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

FILE *stream1, *stream2;

int main()
{
	errno_t f;
	errno_t g;
	f = fopen_s(&stream1, "ooo.txt", "r");
	g = fopen_s(&stream2, "2.txt", "w");
	short int T;
	fscanf_s(stream1, "%hd", &T);
	vector<vector<char>> lastnumbers;
	char buf;
	fscanf_s(stream1, "%c", &buf);
	for (short int i = 0; i < T; i++)
	{
		char a;
		vector<char> s;
		do
		{
			fscanf_s(stream1, "%c", &a);
			s.push_back(a);
		} while (a != '\n');
		s.pop_back();
		//s.erase(s.begin());
		lastnumbers.push_back(s);
	}

	for (short int i = 0; i < T; i++)
	{
		for (int j =0; j < lastnumbers[i].size()-1 ; j++)
		{
			if (lastnumbers[i][j] > lastnumbers[i][j + 1])
			{
				if (lastnumbers[i][j] == '1'&& lastnumbers[i][j + 1] == '0')
				{
					for (int ii = j; ii >= 0; ii--)
					{
						if (lastnumbers[i][ii] > '1')
						{
							lastnumbers[i][ii]--;
							for (int iii = ii + 1; iii < lastnumbers[i].size(); iii++)
							{
								lastnumbers[i][iii] = '9';
							}
							break;
						}
						else
						{
							if (ii == 0)
							{
								lastnumbers[i].erase(lastnumbers[i].begin());
								for (int iii = 0; iii < lastnumbers[i].size(); iii++)
								{
									lastnumbers[i][iii] = '9';
								}
							}
						}
					}
				}
				else
				{
					lastnumbers[i][j]--;
					for (int k = j + 1; k < lastnumbers[i].size(); k++)
					{
						lastnumbers[i][k] = '9';
					}
				}
			}
		}
	}
	for (short int i = 0; i < T; i++)
	{
		fprintf(stream2, "Case #");
		fprintf(stream2, "%d", (i + 1));
		fprintf(stream2, ": ");
		for (int j = 0; j < lastnumbers[i].size(); j++)
		{
			fprintf(stream2, "%c", lastnumbers[i][j]);
		}
		fprintf(stream2, "\n");
	}
	return 0;
}