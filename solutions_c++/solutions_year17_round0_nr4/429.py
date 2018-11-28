#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

#define TYPE_NONE 0
#define TYPE_X    1
#define TYPE_T    2
#define TYPE_O    TYPE_X|TYPE_T

typedef pair<int, int> Position;

bool operator==(const Position& p1, const Position& p2) {
	return (p1.first == p2.second) && (p1.first == p2.second);
}

namespace std {
template <>
struct hash<Position>
{
	size_t operator()(const Position& k) const
	{
		return k.first*101 + k.second;
	}
};
}

typedef int ModelType;

ModelType char2type(const char c) {
		switch (c) {
		case 'o':
			return TYPE_O;
		case 'x':
			return TYPE_X;
		case '+':
			return TYPE_T;
		default:
			return TYPE_NONE;
		}
}

char type2char(const ModelType type) {
		switch (type) {
		case TYPE_O:
			return 'o';
		case TYPE_X:
			return 'x';
		case TYPE_T:
			return '+';
		default:
			return '.';
		}
}

typedef unordered_map<Position, ModelType> Board;

void readBoard(Board& board, int& iBoardSize) {
	int iModels = 0;
	char c = '\0';
	int x = 0, y = 0;
	cin >> iBoardSize >> iModels;
	// input init board
	for (int i = 0; i < iModels; i++) {
		cin >> c >> x >> y;
		Position p(x-1,y-1);
		board[p] = char2type(c);
	}
}

void addHelper(Board& board, int x, int y, ModelType type) {
	auto it = board.find(Position(x,y));
	if (it == board.end()) {
		board[Position(x,y)] = type;
	} else{
		it->second |= type;
	}
}

void solveBoard(Board& board, int iBSize) {
	vector<int> flagRow(iBSize, 0);
	vector<int> flagCol(iBSize, 0);
	vector<int> flagDiag1(iBSize*2-1, 0);
	vector<int> flagDiag2(iBSize*2-1, 0);
	// init flags
	auto it = board.begin();
	while (it != board.end()) {
		if (it->second & TYPE_X) {
			flagCol[it->first.first] = 1;
			flagRow[it->first.second] = 1;
		}
		if (it->second & TYPE_T) {
			flagDiag1[it->first.first + it->first.second] = 1;
			flagDiag2[it->first.first - it->first.second + iBSize - 1] = 1;
		}
		it++;
	}

	// add 'x's
	int i = 0;
	int j = 0;
	for (i = 0; i < iBSize; i++) {
		if(flagCol[i] != 0) {
			continue;
		}
		while (flagRow[j] != 0) {
			j++;
		}
		addHelper(board, i, j, TYPE_X);
		flagRow[j] = 1;
		j++;
	}
	// add '+'s
	// TODO: i cannot prove this heuristic...
	i = 0;
	j = 0;
	for (i = 0; i < iBSize; i++) {
		if(flagDiag1[i] != 0) {
			continue;
		}
		for (j = 0; j < iBSize*2-1; j++) {
			if (flagDiag2[j] != 0) {
				continue;
			}
			int px = (i+j-iBSize+1);
			int py = (i-j+iBSize-1);
			if (px % 2 != 0 || py % 2 != 0) {
				continue;
			}
			px /= 2;
			py /= 2;
			if (iBSize > px && px >= 0 &&
				iBSize > py && py >= 0) {
				addHelper(board, px, py, TYPE_T);
				flagDiag2[j] = 1;
				break;
			}
		}
	}
	for (i = iBSize; i < iBSize*2-1; i++) {
		if(flagDiag1[i] != 0) {
			continue;
		}
		for (j = iBSize*2-2; j >= 0; j--) {
			if (flagDiag2[j] != 0) {
				continue;
			}
			int px = (i+j-iBSize+1);
			int py = (i-j+iBSize-1);
			if (px % 2 != 0 || py % 2 != 0) {
				continue;
			}
			px /= 2;
			py /= 2;
			if (iBSize > px && px >= 0 &&
				iBSize > py && py >= 0) {
				addHelper(board, px, py, TYPE_T);
				flagDiag2[j] = 1;
				break;
			}
		}
	}
}

void dumpDiff(const Board& board, const Board& initBoard) {
	auto it = board.begin();
	int iDiffCount = 0;
	// FIXME: please
	while (it != board.end()) {
		auto pInitState = initBoard.find(it->first);
		if(pInitState == initBoard.end()) {
			// new ones
			iDiffCount++;
		} else if (pInitState->second != it->second) {
			// upgrade
			iDiffCount++;
		} else {
			// do nothing
		}
		it++;
	}
	cout << iDiffCount << endl;
	it = board.begin();
	while (it != board.end()) {
		auto pInitState = initBoard.find(it->first);
		if(pInitState == initBoard.end()) {
			// new ones
			cout << type2char(it->second) << " " << it->first.first+1 << " " << it->first.second+1 << endl;
		} else if (pInitState->second != it->second) {
			// upgrade
			cout << type2char(it->second) << " " << it->first.first+1 << " " << it->first.second+1 << endl;
		} else {
			// do nothing
		}
		it++;
	}
}

int calScore(const Board& board) {
	auto it = board.begin();
	int iScore = 0;
	while (it != board.end()) {
		switch(it->second) {
		case TYPE_X:
			iScore += 1;
			break;
		case TYPE_T:
			iScore += 1;
			break;
		case TYPE_O:
			iScore += 2;
			break;
		}
		it++;
	}
	return iScore;
}

int main(int argc, char** argv) {
	int iRounds = 0;
	cin >> iRounds;
	for (int r = 0; r < iRounds; r++) {
		Board result;
		Board initBoard;
		int iBSize;
		readBoard(initBoard, iBSize);
		result = initBoard;
		solveBoard(result, iBSize);
		cout << "Case #" << r+1 << ": ";
		cout << calScore(result) << " ";
		dumpDiff(result, initBoard);
	}
	
	return 0;
}
