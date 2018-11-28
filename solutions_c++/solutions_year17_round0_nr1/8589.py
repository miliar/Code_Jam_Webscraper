#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

int run_flipper() {
  string board;
  cin >> board;
  int flipper_width;
  cin >> flipper_width;

  set<string> seen_boards;
  set<string> active_boards;
  set<string> new_boards;

  new_boards.insert(board);
  seen_boards.insert(board);

  int iter = 0;
  while (iter < 10000000) { // safety
    active_boards = new_boards;
    new_boards.clear();
    for (auto &board : active_boards) {
      {
        bool is_happy = true;
        for (char c : board) {
          if (c == '-') {
            is_happy = false;
          }
        }
        if (is_happy) {
          return iter;
        }
      }

      // apply flip operation to a state to get set of reachable states
      for (int i = 0; i <= board.size() - flipper_width; i++) {
        string flipped = board;
        for (int j = i; j < i + flipper_width; j++) {
          flipped[j] = flipped[j] == '+' ? '-' : '+';
        }

        if (seen_boards.find(flipped) == seen_boards.end()) {
          // new reachable state
          new_boards.insert(flipped);
        }

        seen_boards.insert(flipped);
      }
    }

    // no new reachable states, must be impossible
    if (new_boards.size() == 0) {
      return -1;
    }

    iter++;
  }

  return -2;
}

int main() {
  int num_trials;
  cin >> num_trials;
  for (int i = 1; i <= num_trials; i++) {
    int iter = run_flipper();
    cout << "Case #" << i << ": ";
    if (iter == -1) {
      cout << "IMPOSSIBLE";
    } else if (iter == -2) {
      cout << "MAX REACHED";
    } else {
      cout << iter;
    }

    cout << endl;
  }
  return 0;
}
