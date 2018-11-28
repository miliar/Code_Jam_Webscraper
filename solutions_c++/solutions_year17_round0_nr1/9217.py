
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

string calcFlips(string pancakes, int flipSize) {
  stringstream ss;
  if( flipSize > pancakes.size() )
    ss << "IMPOSSIBLE";
  else {
    int numFlips = 0;
    for(auto i = 0; i < pancakes.size(); i++) {
      // cerr << "Before: " << pancakes << endl;
      if( pancakes[i] == '+' )
        continue;
      if( pancakes.size() - i < flipSize ) {
        ss << "IMPOSSIBLE";
        return ss.str();
      }
      // do flip
      for(auto j = 0; j < flipSize; j++)
        pancakes[i+j] = (pancakes[i+j] == '-') ? '+' : '-';

      // cerr << "After : " << pancakes << endl;
      ++numFlips;
    }
    ss << numFlips;
  }
  return ss.str();
}

void testFlips( const string expected, const string result ) {
  if( expected.compare(result) != 0 )
    cout << "Test FAILED: Expected( " << expected << " ) Result(" << result << ")" << endl;
  else
    cout << "Test SUCCEDED" << endl;
}

void test() {
  testFlips(string("3"), calcFlips(string("---+-++-"), 3));
  testFlips(string("0"), calcFlips(string("+++++"), 4));
  testFlips(string("IMPOSSIBLE"), calcFlips(string("-+-+-"), 4));
  testFlips(string("5"), calcFlips(string("-+++--+--+--"), 5));
}

int main(int argc, char* argv[]) {

  if( argc > 1 && string(argv[1]).compare("test") == 0 ) {
    cout << "Begin test" << endl;
    test();
  } else {
    int numCases;
    cin >> numCases;

    for(int i = 0; i < numCases; i++) {
      string testCase;
      cin >> testCase;
      int flipSize;
      cin >> flipSize;

      cout << "Case #" << i + 1 << ": " << calcFlips(testCase, flipSize) << endl;
    }
  }

  return 0;
}
