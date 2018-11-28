#include <iostream>
#include <vector>
#include <map>

using namespace std;

const int kD = 4;

struct Ceil {
  static int n;

  int r;
  int c;

  int LeftDiagonal() const {
    return r - c + n - 1;
  }

  int RightDiagonal() const {
    return r + c;
  }

  bool operator<(const Ceil& another) const {
    if (r != another.r) {
      return r < another.r;
    }

    return c < another.c;
  }
};

struct Edge {
  int to;

  Ceil ceil;
};

using Graph = vector<vector<Edge>>;

int Ceil::n = -1;

int n;
int m;
vector<char> line_is_occupied[kD];

Graph graph;
vector<int> occupied_by;
vector<Edge> occupied_with;
vector<int> last_visited;

void ResizeGraph(int first_part, int second_part) {
  graph = Graph(first_part);
  last_visited = vector<int>(first_part, -1);

  occupied_by = vector<int>(second_part, -1);
  occupied_with = vector<Edge>(second_part);
}

void BuildStraightGraph() {
  ResizeGraph(line_is_occupied[0].size(), line_is_occupied[1].size());

  for (int i = 0; i < n; ++i) {
    if (line_is_occupied[0][i]) {
      continue;
    }
    for (int j = 0; j < n; ++j) {
      if (line_is_occupied[1][j]) {
        continue;
      }
      Ceil ceil = {i, j};

      graph[i].push_back({j, ceil});
    }
  }
}

void BuildDiagonalGraph() {
  ResizeGraph(line_is_occupied[2].size(), line_is_occupied[3].size());

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      Ceil ceil = {i, j};
      if (line_is_occupied[2][ceil.LeftDiagonal()] || line_is_occupied[3][ceil.RightDiagonal()]) {
        continue;
      }

      graph[ceil.LeftDiagonal()].push_back({ceil.RightDiagonal(), ceil});
    }
  }
}

bool Dfs(int iteration, int v) {
  if (last_visited[v] == iteration) {
    return false;
  }
  last_visited[v] = iteration;

  for (const Edge& e : graph[v]) {
    int u = e.to;
    if (occupied_by[u] == -1 || Dfs(iteration, occupied_by[u])) {
      occupied_by[u] = v;
      occupied_with[u] = e;
      return true;
    }
  }

  return false;
}

vector<Ceil> FindMaxCover() {
  for (int v = 0; v < graph.size(); ++v) {
    Dfs(v, v);
  }

  vector<Ceil> result;
  for (int u = 0; u < occupied_by.size(); ++u) {
    if (occupied_by[u] != -1) {
      result.push_back(occupied_with[u].ceil);
    }
  }

  return result;
}

void PrintVector(const vector<char>& vc) {
  for (char c : vc) {
    cerr << (c == 1) << " ";
  }
  cerr << "\n";
}

void Solve(int case_id) {
  cin >> n;
  Ceil::n = n;

  line_is_occupied[0] = vector<char>(n, 0);
  line_is_occupied[1] = vector<char>(n, 0);
  line_is_occupied[2] = vector<char>(n + n - 1, 0);
  line_is_occupied[3] = vector<char>(n + n - 1, 0);

  map<Ceil, int> ceils;
  map<Ceil, int> input_ceils;
  cin >> m;
  for (int i = 0; i < m; ++i) {
    string model;
    Ceil ceil;

    cin >> model >> ceil.r >> ceil.c;

    ceil.r -= 1;
    ceil.c -= 1;

    if (model == "x" || model == "o") {
      line_is_occupied[0][ceil.r] = true;
      line_is_occupied[1][ceil.c] = true;
      ceils[ceil] |= 1;
      input_ceils[ceil] = ceils[ceil];
    }
    if (model == "+" || model == "o") {
      line_is_occupied[2][ceil.LeftDiagonal()] = true;
      line_is_occupied[3][ceil.RightDiagonal()] = true;
      ceils[ceil] |= 2;
      input_ceils[ceil] = ceils[ceil];
    }
  }

  BuildStraightGraph();
  vector<Ceil> straight = FindMaxCover();
  BuildDiagonalGraph();
  vector<Ceil> diagonal = FindMaxCover();

  map<Ceil, int> output_ceils;
  for (const Ceil& ceil : straight) {
    ceils[ceil] |= 1;
    output_ceils[ceil] = ceils[ceil];
  }
  for (const Ceil& ceil : diagonal) {
    ceils[ceil] |= 2;
    output_ceils[ceil] = ceils[ceil];
  }

  int answer = 0;
  for (const auto& it : ceils) {
    answer += __builtin_popcount(it.second);
  }

  cout << "Case #" << case_id << ": " << answer << " " << output_ceils.size() << "\n";
  for (const auto& it : output_ceils) {
    string model;
    if (it.second == 1) {
      model = "x";
    } else if (it.second == 2) {
      model = "+";
    } else {
      model = "o";
    }

    cout << model << " " << it.first.r + 1 << " " << it.first.c + 1 << "\n";
  }
}

int main() {
  int cases_num; cin >> cases_num;

  for (int i = 0; i < cases_num; ++i) {
    Solve(i + 1);
  }

  return 0;
}
