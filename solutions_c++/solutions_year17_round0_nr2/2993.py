#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>
#include <sstream>
#include <cassert>
#include <queue>
#include <cassert>
#include <map>


#include <set>
using namespace std;

int mat_size(int n)
{
	int i = 1;
	while ((i*i) < n)
		i++;
	return i;
}


int main()
{

	//freopen("input.txt", "r", stdin);

	int ncase;  cin >> ncase;
	for (int icase = 0; icase < ncase; icase++)
	{
		string msg; cin >> msg;
		vector<vector<char> > m(mat_size(msg.size()), vector<char> (mat_size ( msg.size()), '*'));

		int n = mat_size(msg.size());

		int it = 0;
		for (int i = 0; i < n && it < msg.size(); i++)
		{
			for (int j = 0; j < n && it < msg.size(); j++)
				m[i][j] = msg[it++];
		}

		for (int i = 0; i<n / 2; i++)
			for (int j = 0; j < (n + 1) / 2; j++)
			{
				char temp = m[i][j];
				m[i][j] = m[n - 1 - j][i];
				m[n - 1 - j][i] = m[n - 1 - i][n - 1 - j];
				m[n - 1 - i][n - 1 - j] = m[j][n - 1 - i];
				m[j][n - 1 - i] = temp;
			}	


		for (int i = 0; i < m.size(); i++)
		{
			for (int j = 0; j < m[i].size(); j++)
			{
				if (m[i][j] != '*')
				{
					cout << m[i][j];
				}
			}
		}
		cout << endl;

	}






}