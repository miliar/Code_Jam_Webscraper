#include <iostream>
#include <fstream>

using namespace std;
int N;
int R[1001];
int End;

bool root[6][6] =
{ {0,0,1,1,1,0},
{0,0,0,0,1,0},
{1,0,0,0,1,1},
{1,0,0,0,0,0},
{1,1,1,0,0,0},
{0,0,1,0,0,0} };

/*void func(int *color,int i,int cnt)
{
	if (End == 1)return;
	if (cnt == N)
	{
		if (root[R[0]][i])
			End = 1;
		return;
	}

	for (int j = 0; j < 6 && End == 0; j++)
	{
		if (root[j][i] && color[j])
		{
			color[j]--;
			R[cnt] = j;
			func(color, j, cnt + 1);
			color[j]++;
		}
	}
}*/

void insert(int i, int c)
{
	for (int x = N; x > i; x++)
		R[x] = R[x - 1];

	R[i] = c;
}

int main()
{
	ifstream in("B-small-attempt2.in");
	ofstream out("output.txt");

	int T;
	in >> T;
	for (int Case = 1; Case <= T; Case++)
	{
		int color[6];
		in >> N;
		for (int i = 0; i < 6; i++)
			in >> color[i];

		for (int i = 0; i <= N; i++)
			R[i] = -1;

		out << "Case #" << Case << ": ";
		if (color[0] > color[2] + color[4] || color[2] > color[0] + color[4] || color[4] > color[0] + color[2])
			out << "IMPOSSIBLE";
		else
		{
			if (color[0] >= color[2] && color[0] >= color[4])
			{
				int cnt = 0;
				for (int i = 0; i < color[0]; i++)
				{
					R[cnt++] = 0;
					if (i < color[2])
						R[cnt++] = 2;
					if (i >= color[0] - color[4])
						R[cnt++] = 4;
				}
			}
			else if (color[2] >= color[0] && color[2] >= color[4])
			{
				int cnt = 0;
				for (int i = 0; i < color[2]; i++)
				{
					R[cnt++] = 2;
					if (i < color[0])
						R[cnt++] = 0;
					if (i >= color[2] - color[4])
						R[cnt++] = 4;
				}

			}
			else if (color[4] >= color[0] && color[4] >= color[2])
			{
				int cnt = 0;
				for (int i = 0; i < color[4]; i++)
				{
					R[cnt++] = 4;
					if (i < color[2])
						R[cnt++] = 2;
					if (i >= color[4] - color[0])
						R[cnt++] = 0;
				}
			}

			for (int i = 0; i < N; i++)
			{
				switch (R[i])
				{
				case 0:
					out << 'R';
					break;
				case 1:
					out << 'O';
					break;
				case 2:
					out << 'Y';
					break;
				case 3:
					out << 'G';
					break;
				case 4:
					out << 'B';
					break;
				case 5:
					out << 'V';
					break;
				}
			}
		}

		out << endl;
	}

	return 0;
}