#include <iostream>
#include <fstream>

#include <string>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

using std::vector;
using std::string;
using std::pair;

map<char, string> gr = { {'V', "Y"}, {'G', "R"}, {'O', "B"}, {'Y', "VRB"}, {'R', "GBY"}, {'B', "OYR"} };

string try_go(map<char, int> counts, char start) {
  string result;
  char curr = start;
  if (counts[curr] == 0) {
    return "";
  }
  result += start;
  --counts[curr];
  bool found = true;
  while(found) {
    found = false;
    int mx = 0;
    for (char next : gr[curr]) {
      if (counts[next] > 0) {
        mx = std::max(mx, counts[next]);
        found = true;
      }
    }
    if (found) {
      for (char next : gr[curr]) {
        if (counts[next] == mx) {
          --counts[next];
          curr = next;
          result += curr;
          break;
        }
      }
    }
  }
  for (char c : gr[curr]) {
    if (c == start) {
      found = true;
    }
  }
  if (!found) {
    return "";
  }
  for (auto& p : gr) {
    if (counts[p.first] != 0) {
      return "";
    }
  }
  return result;
}

void work(std::ifstream& in, std::ofstream& out) {

  string str = "ROYGBV";
  map<char, int> counts;
  int n;
  in >> n;
  for (char c : str) {
    in >> counts[c];
  }
  for (char c : str) {
    string res = try_go(counts, c);
    if (!res.empty()) {
      out << res << '\n';
      return;
    }
  }
  out << "IMPOSSIBLE" << '\n';
}

int main() {

  std::ifstream in("input.in");
  std::ofstream out("output.out");

  size_t T;
  in >> T;

  for (size_t i = 0; i < T; ++i) {
    out << "Case #" << i + 1 << ": ";
    work(in, out);
  }
  return 0;
}