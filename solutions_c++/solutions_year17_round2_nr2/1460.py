#include "bb.h"


bool Related(std::string c1, std::string c2) {
  if (c1 == c2) return true;
  if ((c1 == "R" && c2 == "O") ||
    (c1 == "O" && c2 == "R") ||
    (c1 == "R" && c2 == "V") ||
    (c1 == "V" && c2 == "R") ||
    (c1 == "Y" && c2 == "O") ||
    (c1 == "O" && c2 == "Y") ||
    (c1 == "Y" && c2 == "G") ||
    (c1 == "G" && c2 == "Y") ||
    (c1 == "B" && c2 == "G") ||
    (c1 == "G" && c2 == "B") ||
    (c1 == "B" && c2 == "O") ||
    (c1 == "O" && c2 == "B")) {
    return true;
  }
  return false;
}

/*
bool MaybePossible(std::map<std::string, int> counts, int n) {
  std::map<std::string, int> subCounts = GetSubCounts(counts);
  for (auto it = subCounts.begin(); it != subCounts.end(); ++it) {
    if (it->second > n / 2) return false;
  }
  return true;
}

bool MaybeRestPossible(std::map<std::string, int> counts, int n) {
  std::map<std::string, int> subCounts = GetSubCounts(counts);
  for (auto it = subCounts.begin(); it != subCounts.end(); ++it) {
    if (it->second > n / 2 + 1) return false;
  }
  return true;
}

std::string OrderRest(std::map<std::string, int> counts, int n, std::string current = "") {
  if (!MaybeRestPossible(counts, n)) return "IMPOSSIBLE";

  std::string next;
}

std::string Order(std::map<std::string, int> counts, int n) {
  if (!MaybePossible(counts, n)) return "IMPOSSIBLE";


}
*/

bool MaybePossibleSimple(std::map<std::string, int> counts, int n) {
  for (auto it = counts.begin(); it != counts.end(); ++it) {
    if (it->second > n / 2) return false;
  }
  return true;
}


std::string OrderSimpleRest(std::map<std::string, int> counts, int n, std::string current, std::string first) {
  if (n == 0) return "";

  std::string common;
  int commonCount = 0;
  for (auto it = counts.begin(); it != counts.end(); ++it) {
    if ((it->second > commonCount || (it->second == commonCount && it->first == first))
         && it->first != current) {
      common = it->first;
      commonCount = it->second;
    }
  }
  counts[common]--;
  std::string rest = OrderSimpleRest(counts, n - 1, common, first);
  return common + rest;
}

std::string OrderSimple(std::map<std::string, int> counts, int n) {
  if (!MaybePossibleSimple(counts, n)) return "IMPOSSIBLE";

  std::string common;
  int commonCount = 0;
  for (auto it = counts.begin(); it != counts.end(); ++it) {
    if (it->second > commonCount) {
      common = it->first;
      commonCount = it->second;
    }
  }
  counts[common]--;
  std::string rest = OrderSimpleRest(counts, n - 1, common, common);
  return common + rest;
}

void Small() {
  int tests;
  std::cin >> tests;
  for (int i = 1; i <= tests; i++) {
    int n, r, o, y, g, b, v;
    std::map<std::string, int> counts;
    std::cin >> n >> r >> o >> y >> g >> b >> v;
    counts["R"] = r;
    counts["Y"] = y;
    counts["B"] = b;
    std::cout << "Case #" << i << ": ";
    std::cout << OrderSimple(counts, n) << std::endl;
  }
}

void BB() {
  Small();
}
