#include <stdio.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <string.h>
#include <queue>
#include <list>
#include <iomanip>
#include <string>

using namespace std;

#define ll long long

int N, P;
vector<int> R;
vector<vector<int>> Q;

int RoundToInt(float t)
{
	return (int)(t + 0.5);
}

bool isInRange(int ratio,int r,int q)
{
	if (ratio <= 0) return false;
	int amount = r*ratio;
	int detail =amount - q;
	if (detail < 0) detail = -detail;
	if (detail <= amount * 0.1) return true;
	return false;
}


void SingleProcess(ofstream& fout)
{
	vector<int> path(100, -1);
	int count = 0;
	for (int i = 0; i < Q.size(); i++)
	{
		sort(Q[i].begin(), Q[i].end());
	}

	for (int i = 0; i < P; i++)
	{
		int ratio = RoundToInt(Q[0][i] / (float)(R[0]));
		int down, up;
		down = up = ratio;
		int m = 0;
		while (Q[0][i] >= 0 && isInRange(ratio + m, R[0], Q[0][i]))
		{
			up = ratio + m;
			m++;
		}
		m = -1;
		while (Q[0][i] >= 0 && isInRange(ratio + m, R[0], Q[0][i]))
		{
			down = ratio +m;
			m--;
		}


		for (int r = down; r <= up; r++)
		{
			int newRatio = r;
			if (!(Q[0][i] >= 0 && isInRange(newRatio, R[0], Q[0][i]))) continue;

			Q[0][i] = -Q[0][i];
			path[0] = i;
			bool findone = true;
			for (int j = 1; j < N; j++)
			{
				bool fd = false;
				for (int k = 0; k < P; k++)
				{
					if (Q[j][k] >= 0 && isInRange(newRatio, R[j], Q[j][k]))
					{
						Q[j][k] = -Q[j][k];
						path[j] = k;
						fd = true;
						break;
					}
				}
				if (!fd)
				{
					findone = false;
					break;
				}
			}

			if (findone)
			{
				for (int j = 0; j < path.size(); j++)
				{
					path[j] = -1;
				}
				count++;
			}
			else
			{
				for (int j = 0; j < path.size(); j++)
				{
					if (path[j] >= 0)
					{
						Q[j][path[j]] = -Q[j][path[j]];
						path[j] = -1;
					}
				}
			}
		}
	}

	fout << count;
}


int main()
{
	FILE* fp = freopen("in.txt", "r", stdin);
	ofstream fout("out.txt");
	int Cases = 0;
	scanf("%d", &Cases);
	for (int time = 0; time < Cases; time++)
	{
		cin >> N >> P;

		R.clear();
		R.resize(N);

		for (int i = 0; i < N; i++)
		{
			cin >> R[i];
		}

		Q.clear();
		for (int i = 0; i < N; i++)
		{
			vector<int> temp(P, 0);
			for (int j = 0; j < P; j++)
			{
				cin >> temp[j];
			}
			Q.push_back(temp);
		}

		fout << "Case #" << (time + 1) << ": ";
		SingleProcess(fout);
		fout << endl;
		std::cout << time << endl;
	}
	fclose(fp);
	fout.close();

	return 0;

}