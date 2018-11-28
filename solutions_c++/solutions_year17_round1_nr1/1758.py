#include<iostream>

using namespace std;

char map[25][26];
int row, col;

void find_ans()
{
	bool previous_rows_empty = true;
	for (int i = 0; i < row; ++i)
	{
		bool empty_row = true;
		for (int j = 0; j < col; ++j)
		{
			if (map[i][j] != '?')
			{
				empty_row = false;
			}
		}

		if (empty_row)
		{
			if (!previous_rows_empty)
			{
				// Copy the last row
				strcpy(map[i], map[i - 1]);
			}
		}
		else
		{
			// find current row
			int last_idx = 0;
			char last_ch = '?';
			for (int j = 0; j < col; ++j)
			{
				int ch = map[i][j];
				if (ch != '?')
				{
					for (int k = last_idx; k < j; ++k)
						map[i][k] = ch;
					last_ch = ch;
					last_idx = j + 1;
				}
			}
			for (int k = last_idx; k < col; ++k)
				map[i][k] = last_ch;

			if (previous_rows_empty)
			{
				// Copy ans to previous rows
				for (int j = 0; j < i; ++j)
				{
					strcpy(map[j], map[i]);
				}

			}
			previous_rows_empty = false;
		}
	}
}

int main()
{
	int n_case;
	cin >> n_case;
	for (int i = 1; i <= n_case; ++i)
	{
		//int row, col;
		cin >> row >> col;
		cin.get();
		for (int j = 0; j < row; ++j)
			cin.getline(map[j], 26);

		find_ans();
		cout << "Case #" << i << ":" << endl;
		for (int j = 0; j < row; ++j)
			cout << map[j] << endl;
	}
	return 0;
}