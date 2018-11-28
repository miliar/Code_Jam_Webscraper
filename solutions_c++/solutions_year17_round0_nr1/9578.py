#include <iostream>
#include <bitset>
#include <string>
#include <unordered_map>
#include <queue>

typedef std::bitset<11> bs1;

bs1 flip_bits(bs1 st, int dex, int k, int N) {
  if (dex + k > N) {
    return st;
  }
  for (int i = dex; i < dex + k; ++i) {
    st[i] = !st[i];
  }

  return st;
}

bool success(bs1 v, int N) {
  for(int i = 0; i < N; ++i) {
    if (!v[i]) {
      return false;
    }
  }
  return true;
}

int bfs(bs1 start, int N, int k) {
  std::unordered_map<bs1, bool> visited;

  std::queue< std::vector<bs1 > > Q;
  
  Q.push(std::vector< bs1 >({start}));
  visited[start] = true;
  
  int dist = 0;
  bool found = false;
  while (Q.size() > 0) {
    std::vector< bs1 > next;
    std::vector< bs1 > curr = Q.front();
    Q.pop();

    for (int i = 0; i < curr.size(); ++i) {
      bs1 whaddup = curr[i];
      if (success(whaddup, N)) {
	return dist;
      }
      
      for (int j = 0; j < N; ++j) {
	bs1 flipped = flip_bits(whaddup, j, k, N);

	
	if (visited.find(flipped) == visited.end()) {
	  next.push_back(flipped);
	  visited[flipped] = true;
	  if (success(flipped, N)) {
	    return dist + 1;
	  }
	}
      }
    }

    if (next.size() > 0) {
      Q.push(next);
    }
    
    ++dist;
  }

  return -1;
}

int main() {
  int tc;

  int ca = 1;
  std::cin >> tc;
  while (tc) {
    std::string state;
    int k;

    std::cin >> state >> k;

    bs1 start;

    for (int i = 0; i < state.size(); ++i) {
      if (state[i] == '+') {
	start[i] = 1;
      } 
    }
    int res = bfs(start, state.size(), k);

    std::cout << "Case #" << ca << ": ";
    ca++;
    if (res == -1) {
      std::cout << "IMPOSSIBLE" << std::endl;
    } else {
      std::cout << res << std::endl;
    }

    --tc;
  }
  
}
