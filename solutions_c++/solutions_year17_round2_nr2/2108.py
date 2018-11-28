#define _USE_MATH_DEFINES

#include <cstdlib>
#include <climits>
#include <cmath>

#include <iostream>
#include <string>

#include <vector>
#include <map>
#include <list>
#include <set>

using namespace std;

class Mane {
public:
	Mane(int& count, char desc)
		: count(count), desc(desc), orig(count)
	{}

	int& count;
	int orig;
	vector<Mane*> successors;
	char desc;
};

class Comp {
public:
	bool operator()(Mane* lhs, Mane* rhs) {
		if (lhs->count == rhs->count) {
			if (lhs->orig == rhs->orig) {
				return lhs > rhs;
			}
			return lhs->orig > rhs->orig;
		}
		return lhs->count > rhs->count;
	}
};

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		// read input
		int N, R, O, Y, G, B, V;
		cin >> N >> R >> O >> Y >> G >> B >> V;

		Mane rm(R, 'R'), om(O, 'O'), ym(Y, 'Y'), gm(G, 'G'), bm(B, 'B'), vm(V, 'V');
		rm.successors = { &ym, &bm, &gm };
		om.successors = { &bm };
		ym.successors = { &rm, &bm, &vm };
		gm.successors = { &rm };
		bm.successors = { &rm, &ym, &om };
		vm.successors = { &ym };
		set<Mane*, Comp> allowed_manes = { &rm, &om, &ym, &gm, &bm, &vm };

		cout << "Case #" << (t + 1) << ": ";

		// calculate solution
		int r = R + O + V;
		int y = Y + O + G;
		int b = B + G + V;

		// output solution
		string solution = "";
		if (r > y + b || y > r + b || b > r + y) {
			solution = "IMPOSSIBLE";
		}
		else {
			for (int i = 0; i < N; i++) {
				Mane* mane = nullptr;
				while (true) {
					if (allowed_manes.empty()) {
						solution = "IMPOSSIBLE";
						break;
					}
					auto mane_it = allowed_manes.begin();
					if ((*mane_it)->count > 0) {
						mane = *mane_it;
						allowed_manes.erase(mane_it);
						break;
					}
					else {
						allowed_manes.erase(mane_it);
					}
				}

				if (mane == nullptr) {
					break;
				}

				solution += mane->desc;
				mane->count--;
				allowed_manes.clear();
				for (auto succ : mane->successors) {
					allowed_manes.insert(succ);
				}
			}

			if (solution != "IMPOSSIBLE" && solution[0] == solution[N - 1]) {
				solution = "IMPOSSIBLE";
			}
		}

		cout << solution;


		cout << endl;
	}
}