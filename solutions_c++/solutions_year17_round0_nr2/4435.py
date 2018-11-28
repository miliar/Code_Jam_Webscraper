#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <queue>
using namespace std;

//ifstream fin("B-small-attempt0.in");
///ofstream fout("B-small.out");

ifstream fin("B-large.in");
ofstream fout("B-large.out");

unsigned long long digit(vector<unsigned long long> v) {
  unsigned long long k = 1;
  unsigned long long out = 0;
  for (int i = 0; i < v.size(); ++i) {
    out += v[i] * k;
    k *= 10;
  }
  return out;
}

bool tidy(vector<unsigned long long> q) {
  int i = 0;
  while (i < q.size() - 1 && q[i] >= q[i + 1]) {
    ++i;
  }
  if (i == q.size() - 1) {
    return true;
  }
  return false;
}

void task() {
  unsigned long long n = 0;
  fin >> n;

  if (n < 10) {
    fout << n;
    return;
  }

  vector<unsigned long long> q;
  unsigned long long m = n;

  while (m != 0) {
    q.push_back(m % 10);
    m /= 10;
  }

  if (tidy(q)) {
    fout << n;
    return;
  }

  m = n - 1;
  vector<unsigned long long> v;
  while (m != 0) {
    v.push_back(m % 10);
    m /= 10;
  }

  for (int i = 0; i < v.size(); ++i) {
    if (tidy(v) == true && digit(v) <= n) {  // 131 -> 139 -> 129
      fout << digit(v);
      return;
    }

    do {
      if (v[i] == 0) {
        v[i] = 9;
        break;
      }
      else
        v[i] -= 1;
    } while (tidy(v) == false);

    if (tidy(v) == true && digit(v) <= n) {  // 131 -> 139 -> 129
      fout << digit(v);
      return;
    }
  }
  
}

int main() {

  long long t = 0;
  fin >> t;

  for (long long i = 0; i < t; i++) {
    fout << "case #" << i + 1 << ": ";
    task();
    fout << endl;
  }
  fout.close();
  cout << "OK";
  return 0;
}