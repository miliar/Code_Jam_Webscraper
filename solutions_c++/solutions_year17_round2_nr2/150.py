#include <iostream>
#include <algorithm>
using namespace std;

struct color {
	int amount;
	int oamount;
	char name;
	char opponent;

	int real_amount() {
		return amount-oamount;
	}

	void use() {
		cout << name;
		amount--;

		while (oamount > 0) {
			cout << opponent << name;
			oamount--;
			amount--;
		}
	}
};

bool operator<(color a, color b) {
	return a.real_amount() > b.real_amount();
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N;
		int red, orange, yellow, green, blue, violet;

		cin >> N >> red >> orange >> yellow >> green >> blue >> violet;

		cout << "Case #" << t << ": ";

		color colors[3] = { { red, green, 'R', 'G' }, { yellow, violet, 'Y', 'V' }, { blue, orange, 'B', 'O' } };

		bool done = false;
		for (int c = 0; c < 3; c++) {
			if (colors[c].oamount > 0 && colors[c].oamount >= colors[c].amount) {
				if (colors[c].oamount == colors[c].amount && colors[c].amount+colors[c].oamount == N) {
					for (int i = 0; i < colors[c].amount; i++) cout << colors[c].name << colors[c].opponent;
				} else {
					cout << "IMPOSSIBLE";
				}
				cout << '\n';
				done = true;
				break;
			}
		}
		if (done) continue;

		sort(colors, colors+3);

		if (colors[0].real_amount() > colors[1].real_amount()+colors[2].real_amount()) {
			cout << "IMPOSSIBLE\n";
			continue;
		}

		while (colors[0].real_amount() > 0) {
			if (colors[0].real_amount() < colors[1].real_amount()+colors[2].real_amount()) {
				colors[0].use();
				colors[1].use();
				colors[2].use();
			} else if (colors[1].real_amount() > 0) {
				colors[0].use();
				colors[1].use();
			} else {
				colors[0].use();
				colors[2].use();
			}
		}
		cout << '\n';
	}

	return 0;
}
