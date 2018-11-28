#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <unordered_set>
#include <bitset>
#include <queue>

using namespace std;

// int lim_dfs(int start, int lim, int n, int k, bitset<1024>& seen_path,
// 	    bitset<1024>& seen_last, bitset<1024>& seen_cum, int goal) {
//   if (start == goal) return 0;
//   if (seen.test(start)) return -1;
//   if (lim == 0) return -2;
//   seen.set(start);
//   int tmp;
//   bool hit = false;
//   for (int i = 0; i < (n-k+1); i++) {
//     tmp = lim_dfs((((1<<k)-1)<<i)^start, lim-1, n, k, seen, goal);
//     if (tmp >= 0) return tmp+1;
//     if (tmp == -2) hit = true;
//   }
//   seen.reset(start);
//   if (hit) return -2;
//   else return -1;
// }

// int it_dfs(int start, int n, int k, int goal) {
//   int soln = -2, lim = 0; // -2 hit limit; -1 impossible
//   bitset<1024> seen_path, seen_last, seen_cum;
//   while (soln == -2) {
//     seen_path.reset();
//     soln = lim_dfs(start, lim++, n, k, seen_path, seen_last, seen_cum, goal);
//     seen_last = seen_cum;
//   }
//   return soln;
// }

int bfs(int root, int n, int k, int goal) {
  bitset<1024> seen;
  queue<int> layers[2];
  int curr;
  int d = 0, i = 0, j;
  layers[i].push(root);
  while (!layers[i].empty()) {
    curr = layers[i].front();
    layers[i].pop();
    if (curr == goal) return d;
    if (!seen.test(curr)) {
      seen.set(curr);
      for (j = 0; j < (n-k+1); j++)
	layers[!i].push((((1<<k)-1)<<j)^curr);
    }
    if (layers[i].empty()) {
      i = !i;
      d++;
    }
  }
  return -1;
}

int main() {
  ifstream input("pan.in");
  ofstream output("pan.out");
  string line;
  int num, i, j, n, k, state, soln;

  getline(input, line);
  num = atoi(line.c_str());
  
  for (i = 0; i < num; i++) {
    getline(input, line);
    
    k = line[line.length()-1]-'0';
    state = 0;
    for (j = 0; j < line.length(); j++) {
      if (line[j] == '+' || line[j] == '-')
	state |= (line[j]=='+')<<j;
      else break;
    }
    n = j;
    k = atoi(line.substr(n, string::npos).c_str());
    soln = bfs(state, n, k, (1<<n)-1);
    if (soln>=0) {
      cout << "Case #" << (i+1) << ": " << soln << endl;
      output << "Case #" << (i+1) << ": " << soln << endl;
    } else {
      cout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
      output << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
