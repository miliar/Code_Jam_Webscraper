#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <map>
#include <sstream>
#include <string>
// www.boost.org
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/utility/binary.hpp>
using namespace std;
using namespace boost::multiprecision;

string repeat(char ch, unsigned int n) {
  string r;

  for (unsigned int i = 0; i < n; i++) {
    r += ch;
  }

  return r;
}

string lastTidy(string nst) {
  if (nst.size() == 1) {
    return nst;
  }

  unsigned long long n = stoull(nst);
  string minSolutionSt = repeat('9', nst.size() - 1);
  string candidateSt = repeat('1', nst.size());
  unsigned long long candidate = stoull(candidateSt);

  if (candidate > n) {
    return minSolutionSt;
  }

  string nextCandidateSt = candidateSt;
  unsigned long long nextCandidate = candidate;
  for (unsigned int i = 0; i < nextCandidateSt.size(); i++) {
    char nextDigit = nextCandidateSt[i];

    nextCandidateSt = candidateSt;
    nextCandidate = candidate;

    while (nextDigit <= '9') {
      nextCandidateSt.replace(i, nst.size() - i, nst.size() - i, nextDigit);
      nextCandidate = stoull(nextCandidateSt);

      if (nextCandidate <= n) {
        candidateSt = nextCandidateSt;
        candidate = nextCandidate;
      } else {
        break;
      }

      nextDigit++;
    }
  }
  
  return candidateSt;
}

int main() {
  int t;
  scanf("%d\n", &t);

  for (int i = 1; i <= t; i++) {
    string n;
    cin >> n;

    cout << "Case #" << i << ": ";
    cout << lastTidy(n) << endl;
  }
}
