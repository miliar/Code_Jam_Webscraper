#include <fstream>
#include <string>

std::ifstream cin("input.in");
std::ofstream cout("output.txt");

void flap(std::string & x, int ini, int fin) {

	for (int i = ini; i < fin; i++) {
		x[i] = (x[i] == '+' ? '-' : '+');
	}
}

int flipFlappers(std::string pancakes, int flip) {

	int i = 0;
	int flipCount = 0;
	bool possible = true;

	while (i < pancakes.size()) {

		while (i < pancakes.size() && pancakes[i] == '+') i++;

		if (i + flip <= pancakes.size()) {
			flap(pancakes, i, i + flip);
			flipCount++;
		}
		else if (pancakes[i] == '-') possible = false;

		i++;
	}

	return possible ? flipCount : -1;
}


int main() {

	int numCases; cin >> numCases;

	for (int i = 0; i < numCases; i++) {

		std::string pancakes; cin >> pancakes;
		int flip; cin >> flip;

		int sol = flipFlappers(pancakes, flip);

		cout << "Case #" << i + 1 << ": ";
		if (sol == -1) cout << "IMPOSSIBLE\n";
		else cout << sol << "\n";

	}
	return 0;
}