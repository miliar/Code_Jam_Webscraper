#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#define DEBUG  0

using namespace std;

char arr[25][25];

void dump(int r, int c)
{
//	cout << endl;

	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cout << arr[i][j];
		}
		cout << endl;
	}
}

void fill(int row, int col)
{
	//dump(row,col);

	for (int r = 0; r < row; r++) {
		for (int c = 0; c < col; c++) {
			char ch = arr[r][c];

			if ('?' == ch)
				continue;

			for (int i = 0; i < row; i++) {
				if ('?' == arr[i][c])
					arr[i][c] = ch;
				else if ((r < i) && (ch != arr[i][c]))
					break;
			}
		}
	}

	//dump(row,col);
	
	for (int r = 0; r < row; r++) {
		for (int c = 0; c < col; c++) {
			char ch = arr[r][c];

			if ('?' == ch)
				continue;

			for (int i = 0; i < col; i++) {
				if ('?' == arr[r][i])
					arr[r][i] = ch;
				else if ((c < i) && (ch != arr[r][i]))
					break;
			}
		}
	}
	
	dump(row,col);
}

int main()
{
	ifstream File;
	//File.open("/Users/lester/Downloads/A-small-attempt0.in");
	File.open("/Users/lester/Downloads/A-large.in");
	//File.open("./test.in");

	if (!File.is_open()) {
		cout << "faild" << endl;
		return 0;
	}

	int Times = -1;

	File >> Times;
	//cout << Times << endl;

	for (int i = 1; i <= Times; i++) {	
		int r, c;

		File >> r >> c;

		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++)
				File >> arr[i][j]; 
		}

		cout << "Case #" << i << ":" << endl;
		fill(r, c);
#if 0
		cout << "====== #"<< i << endl;
		cout << line << " " << size << endl;
		
		cout << getFlipTimes(line, size) << endl;
#endif
		//int ans = getFlipTimes(line, size);

		//cout << "Case #" << i << ": IMPOSSIBLE" << endl;
	}

	return 0;
}
