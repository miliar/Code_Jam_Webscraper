#include <iostream>
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text


void flip(std::string& pancakes, int k, int position) {
	for (int i = position; i < position + k; ++i) {
		pancakes[i] == '-' ? pancakes[i] = '+' : pancakes[i] = '-';
	}
	return;
}

int numMoves(std::string pancakes, int k) {
	int moves = 0;
	for (int i = 0; i <= pancakes.size() - k; ++i) {
		if (pancakes[i] == '-') {
			flip(pancakes, k, i);
			moves++;
		}
	}

	if (pancakes != std::string(pancakes.size(), '+')) {
		moves = -1;
	}
	return moves;
}

int main() {
  int N;

  std::cin >> N;
  for (int i = 0; i < N; ++i) {
  	std::string pancakes;
  	int flipper;
  	std::cin >> pancakes >> flipper;


  	int moves = numMoves(pancakes, flipper);
  	if (moves < 0) {
  		std::cout << "Case #" << i + 1 << ": IMPOSSIBLE" << std::endl;
  	} else {
  		std::cout << "Case #" << i + 1 << ": " << moves << std::endl;
  	}
  }
  return 0;
}