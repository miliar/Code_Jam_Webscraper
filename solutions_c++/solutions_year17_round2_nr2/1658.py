#include <algorithm>
#include <exception>
#include <iostream>
#include <iterator>
#include <vector>


using namespace std;

class no_solution_exception : public logic_error {
  using logic_error::logic_error;
};

vector<char> findPath(int N, int R, int O, int Y, int G, int B, int V) {
  if (G == 0 && V == 0 && O == 0) { // small
    if (R > Y + B || Y > R + B || B > R + Y)
      throw no_solution_exception("IMPOSSIBLE");
    vector<char> path; path.reserve(N);
    if (R > 0) {
      path.push_back('R'); --R;
    } else if (Y > 0) {
      path.push_back('Y'); --Y;
    } else if (B > 0) {
      path.push_back('B'); --B;
    }
    int i = 0;
    while (R > 0 || Y > 0 || B > 0) {
      if (path.back() == 'R') {
        if (Y > 0 && Y >= B) {
          path.push_back('Y'); --Y;
        } else if (B > 0 && B >= Y) {
          path.push_back('B'); --B;
        }
      } else if (path.back() == 'Y') {
        if (R > 0 && R >= B) {
          path.push_back('R'); --R;
        } else if (B > 0 && B >= R) {
          path.push_back('B'); --B;
        }
      } else if (path.back() == 'B') {
        if (R > 0 && R >= Y) {
          path.push_back('R'); --R;
        } else if (Y > 0 && Y >= R) {
          path.push_back('Y'); --Y;
        }
      }
    }
    return path;
  }
  throw no_solution_exception("IMPOSSIBLE"); 
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(false); cin.tie(NULL);
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N; cin >> N;
    int R, O, Y, G, B, V;
    cin >> R >> O >> Y >> G >> B >> V;
    cout << "Case #" << t << ": ";
    try {
      vector<char> path = findPath(N, R, O, Y, G, B, V);
      copy(path.begin(), path.end(), ostream_iterator<char>(cout));
    } catch (no_solution_exception e) {
      cout << e.what();
    }
    cout << endl;
  }
  cout << flush;
  return 0;
}

