#include <iostream>
#include <cmath>
#include <vector>
#include <limits>
#include <string>
#include <iomanip>

using namespace std;

#define START 0x00
#define RED 0x01
#define YELLOW 0x02
#define BLUE 0x04
#define ORANGE (RED | YELLOW)
#define GREEN (YELLOW | BLUE)
#define VIOLET (RED | BLUE)

char num2char(int c) {
	switch(c) {
	case ORANGE:
		return 'O';
		break;
	case GREEN:
		return 'G';
		break;
	case VIOLET:
		return 'V';
		break;
	case RED:
		return 'R';
		break;
	case YELLOW:
		return 'Y';
		break;
	case BLUE:
		return 'B';
		break;
	}
	return 0;
}

class horse {
public:
	horse (int _color) {
		color = _color;
		left = this;
		right = this;
	}
	int color;
	horse *left;
	horse *right;
	void insert_right(horse *h) {
		right->left = h;
		h->right = right;
		h->left = this;
		right = h;
	}
	void insert_left(horse *h) {
		left->right = h;
		h->left = left;
		h->right = this;
		left = h;
	}
	bool isValid(int c) {
		return ! ((right->color & c) | ((color ? color : left->color) & c));
	}

	bool isValidStrict(int c) {
		return ! (((right->color ? right->color : right->right->color) & c) | ((color ? color : left->color) & c));
	}

	void report() {
		cout << "Right: " << num2char((right->color ? right->color : right->right->color)) << " Left: " << num2char((color ? color : left->color)) << endl;
	}
};

int colors[] = {ORANGE, GREEN, VIOLET, RED, YELLOW, BLUE, START};
int num[6] = {0};

string print(horse *start) {
	string s = "";
	horse *cur = start->right;
	for (cur = start->right; cur != start; cur = cur->right) {
		s += num2char(cur->color);
		// switch(cur->color) {
		// case ORANGE:
		// 	return 'O";
		// 	break;
		// case GREEN:
		// 	return 'G";
		// 	break;
		// case VIOLET:
		// 	return 'V";
		// 	break;
		// case RED:
		// 	return 'R";
		// 	break;
		// case YELLOW:
		// 	return 'Y";
		// 	break;
		// case BLUE:
		// 	return 'B";
		// 	break;
		// }
	}
	return s;
}

int main(int argc, char *argv[]) {
	int t;
	cin >> t;
	for (int _ = 0; _ < t; ++_) {
		int n;
		cin >> n >> num[3] >> num[0] >> num[4] >> num[1] >> num[5] >> num[2];
		horse *start = new horse(START);
		bool ins;
		while(n > 0) {
			ins = false;
			for (int i = 0; colors[i]; ++i) {
				if (num[i] <= 0) continue;
				horse *cur = start;
				// cout << num2char(colors[i]) << " " << num[i] << endl;
				do {
					// cur->report();
					if (n == 1 ? cur->isValidStrict(colors[i]) : cur->isValid(colors[i])) {
						// cout << "Insert: " << i << endl;
						cur->insert_right(new horse(colors[i]));
						--num[i];
						--n;
						ins = true;
						break;
					}
					cur = cur->right;
				} while(cur != start);
				
				if (ins) break;

				// // Print status
				// cur = start;
				// do {
				// 	cout << cur->color << " ";
				// 	cur = cur->right;
				// } while(cur != start);
				// cout << endl;
			}
			if (!ins && n > 0) {
				// cout << "IMPOSSIBLE" << endl;
				break;
			}
			// cout << print(start) << endl;
		}

		// horse *cur = start;
		// do {
		// 	cout << cur->color << " ";
		// 	cur = cur->right;
		// } while(cur != start);
		// cout << endl;

		// cout << "------------" << endl;

		cout << fixed << "Case #" << _ + 1 << ": " << (ins ? print(start) : "IMPOSSIBLE") << endl;
	}
}
