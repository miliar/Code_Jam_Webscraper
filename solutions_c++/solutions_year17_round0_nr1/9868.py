#include <iostream>
#include <assert.h>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <limits>
#include <list>
#include <map>
#include <iomanip>
#include <iostream>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std; 



void print_set(std::vector<bool> v) {
  for (auto x: v) {
    cout << x;
  }
  cout << endl;
}

int do_it(int k){
  std::map<std::vector<bool>, bool> visited;
  string s;
  int n;

  cin >> s >> n;

  std::vector<bool> start;
  for (auto x: s) {
    if (x == '+') {
      start.push_back(1);
    } else {
      start.push_back(0);
    }
  }

  // for (auto x: start) {
  //   cout << x << endl;
  // }

  queue<std::vector<bool> > queue;
  std::queue<int> queue2;
  queue.push(start);
  queue2.push(0);
  visited[start] = 1;
  

  while (!queue.empty()) {
    std::vector<bool> v = queue.front();
    std::vector<bool> temp = v;
    int cur = queue2.front();

    // print_set(v);

    bool flag = 1;
    for (auto x: v) {
      if (!x) {
        flag = 0;
        break;
      }
    }

    if (flag) {
      cout << cur << endl;
      return 0;
    }

    for (int i = 0; i < n; ++i) {
      v[i] = 1 - v[i];
    }
    if (!visited[v]) {
      queue.push(v);
      queue2.push(cur + 1);
      visited[v] = 1;
    }
    for (size_t i = 1; i <= v.size() - n; ++i) {
      // print_set(v);
      // cout << i - 1 << " " << v[i - 1] << endl;
      v[i - 1] = 1 - v[i - 1];
      // cout << i - 1 << " " << v[i - 1] << endl;
      v[i + n - 1] = 1 - v[i + n - 1];
      // print_set(v);
      if (!visited[v]) {
        queue.push(v);
        queue2.push(cur + 1);
        visited[v] = 1;
      }
    }
    queue.pop();
    queue2.pop();
  }

  cout << "IMPOSSIBLE" << endl;
  return 0;
}

int main(int argc, char const *argv[]) {
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cout << "Case #" << i + 1 << ": ";
    do_it(i);
  }
  return 0;
}
