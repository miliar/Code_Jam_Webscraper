#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	for (int caseNum = 1; caseNum <= T; caseNum++) {
		int R, C;
		cin >> R >> C;
		char allocation[R][C];
		bool isFullUnallocated[R];
		for (int row = 0; row < R; row++) {
			string rowState;
			cin >> rowState;
			bool allUnallocated = true;
			for (int col = 0; col < C; col++) {
				allocation[row][col] = rowState[col];
				if (rowState[col] != '?') {
					allUnallocated = false;
				}
			}
			isFullUnallocated[row] = allUnallocated;
		}
		int startingRow = 0;
		while (isFullUnallocated[startingRow]) {
			startingRow++;
		}
		for (int row = startingRow; row < R; row++) {
			if (!isFullUnallocated[row]) {
				int firstAllocatedCol = 0;
				while (allocation[row][firstAllocatedCol] == '?') {
					firstAllocatedCol++;
				}
				for (int col = 0; col < firstAllocatedCol; col++) {
					allocation[row][col] = allocation[row][firstAllocatedCol];
				}
				int curCol = firstAllocatedCol + 1;
				while (curCol < C) {
					if (allocation[row][curCol] == '?') {
						allocation[row][curCol] = allocation[row][curCol-1];
					}
					curCol++;
				}
			} else {
				for (int col = 0; col < C; col++) {
					allocation[row][col] = allocation[row-1][col];
				}
			}
		}
		for (int row = 0; row < startingRow; row++) {
			for (int col = 0; col < C; col++) {
				allocation[row][col] = allocation[startingRow][col];
			}
		}

		cout << "Case #" << caseNum << ":" << endl;
		for (int row = 0; row < R; row++) {
			for (int col = 0; col < C; col++) {
				cout << allocation[row][col];
			}
			cout << endl;
		}
	}
	return 0;
}