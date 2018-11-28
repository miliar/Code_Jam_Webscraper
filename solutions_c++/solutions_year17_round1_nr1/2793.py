#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <functional>

using namespace std;

struct Coord {
	int x, y;
};

class Op {
public:
	char type;
	Coord upLeft, downRight;
	int area;
	Op(char type, Coord upLeft, Coord downRight) :
		type(type), upLeft(upLeft), downRight(downRight) {
		int width = downRight.x - upLeft.x + 1;
		int height = downRight.y - upLeft.y + 1;
		this->area = width * height;
	}
	bool operator<(const Op &right) const {
		if (area == right.area) return type < right.type;
		else return area < right.area;
	}
	bool operator>(const Op &right) const {
		if (area == right.area) return type > right.type;
		else return area > right.area;
	}
};


bool canOp(const vector<string> &board, const vector<Coord> &appearPos, const Op &op) {
	int x = appearPos[op.type - 'A'].x;
	int y = appearPos[op.type - 'A'].y;
	char type = op.type;
	if (op.upLeft.x <= x && x <= op.downRight.x &&
		op.upLeft.y <= y && y <= op.downRight.y) {
		for (int i = op.upLeft.x; i <= op.downRight.x; i++) {
			for (int j = op.upLeft.y; j <= op.downRight.y; j++) {
				if (board[j][i] != type && board[j][i] != '?') return false;
			}
		}
		return true;
	}
	return false;
}

void solve(vector<string> board) {
	int R = board.size();
	int C = board[0].size();
	set<char> appearType;
	vector<Coord> appearPos(26);
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (board[i][j] == '?') continue;
			appearType.insert(board[i][j]);
			appearPos[board[i][j] - 'A'] = { j, i };
		}
	}
	vector<Op> availOp;
	for (char type : appearType) {
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				for (int m = i; m < R; m++) {
					for (int n = j; n < C; n++) {
						Op op(type, { j, i }, { n, m });
						if (canOp(board, appearPos, op)) {
							availOp.push_back(op);
						}
					}
				}
			}
		}
	}
	sort(availOp.begin(), availOp.end(), greater<Op>());
	vector<bool> used(26, false);
	for (int i = 0; i < availOp.size(); i++) {
		Op &op = availOp[i];
		if (!used[op.type - 'A'] && canOp(board, appearPos, op)) {
			for (int i = op.upLeft.x; i <= op.downRight.x; i++) {
				for (int j = op.upLeft.y; j <= op.downRight.y; j++) {
					board[j][i] = op.type;
				}
			}
			used[op.type - 'A'] = true;
		}
	}
	for (int i = 0; i < R; i++) {
		cout << board[i] << endl;
	}
}

int main(void) {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int r, c;
		cin >> r >> c;
		vector<string> board;
		for (int i = 0; i < r; i++) {
			string line; cin >> line;
			board.push_back(line);
		}
		cout << "Case #" << (t + 1) << ":" << endl;
		solve(board);
	}
	return 0;
}