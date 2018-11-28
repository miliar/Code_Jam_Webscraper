
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;

void doTest( const string expected, const string result ) {
  if( expected.compare(result) != 0 )
    cout << "Test FAILED: Expected( " << expected << " ) Result(" << result << ")" << endl;
  else
    cout << "Test SUCCEDED" << endl;
}

bool isTidy(const string& number) {
  // cout << number << endl;
  bool tidy = true;
  for(auto it = number.begin(); it != number.end() - 1; it++) {
    if( *it > *(it+1) ) {
      tidy = false;
      break;
    }
  }
  return tidy;
}

string calcTidy(ull n) {
  for(ull i = n; i >= 1; i--) {
    stringstream ss;
    ss << i;
    string number = ss.str();
    if( isTidy( number ) ) {
      return number;
    }
  }
  return string();
}
/*
string trimZeros(string str) {
  size_t startpos = str.find_first_not_of("0");
  if( string::npos != startpos )
      str = str.substr( startpos );
  return str;
}
*/

string calcTidy2(ull n) {
  stringstream number;
  number << n;

  if( isTidy(number.str()) ) {
    return number.str();
  }


  // vector<string> s0 = { "1", "2", "3", "4", "5", "6", "7", "8", "9" };
  vector<ull> s1 = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

  auto f = [](vector<ull> set1, vector<ull> set2) {
    vector<ull> set3;
    for( auto p : set1 ) {
      for( auto q : set2 ) {
        // if( p.back() <= q.front() )
        if( p % 10 <= q )
          set3.push_back(p * 10 + q);
      }
    }
    return set3;
  };

  std::function< vector<ull>(vector<ull>, int) > g = [&](vector<ull> currentSet, int digits) {
    if( digits == 1)
      return currentSet;
    else
      return g(f(currentSet, s1), --digits);
  };


  auto candidates = g(s1, number.str().size());

  stringstream ss;

  for(auto it = candidates.begin(); it != candidates.end() - 1; it++) {
    if( *it <= n && *(it + 1) > n ) {
      ss << *it;
      return ss.str();
    }
  }

  ss << candidates.front();

  return ss.str();
}

void test() {
  doTest(string("129"), calcTidy2(132));
  doTest(string("999"), calcTidy2(1000));
  doTest(string("7"), calcTidy2(7));
  doTest(string("99999999999999999"), calcTidy2(111111111111111110));
}

int main(int argc, char* argv[]) {

  if( argc > 1 && string(argv[1]).compare("test") == 0 ) {
    cout << "Begin test" << endl;
    test();
  } else {
    int numCases;
    cin >> numCases;

    for(int i = 0; i < numCases; i++) {
      ull testCase;
      cin >> testCase;

      cout << "Case #" << i + 1 << ": " << calcTidy2(testCase) << endl;
    }
  }

  return 0;
}
