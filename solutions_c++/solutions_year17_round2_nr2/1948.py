#include <iostream>
#include <string>
#include <climits>
#include <vector>

using namespace std;


void print(vector<vector<int> > &v) {
    for (int j = 0; j < 6; j++) {
      for (int k = 0; k < 6; k++) {
        cout << v[j][k];
      }
      cout << endl;
    }
    cout << "----" << endl;
}

void remove_color(vector<vector<int> > &v, int idx) {
  for (int i = 0; i < 6; i++) {
    if (v[idx][i] > 0)
      v[idx][i]--;
  }
}

int main() {
  int t;
  cin >> t;

  char c[] = {'R', 'O', 'Y', 'G', 'B', 'V'};
  for (int i = 0; i < t; i++) {
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    
    vector<vector<int> > solutions {
      { 0, 0, 1, 1, 1, 0},
      { 0, 0, 0, 0, 1, 0},
      { 1, 0, 0, 0, 1, 1},
      { 1, 0, 0, 0, 0, 0},
      { 1, 1, 1, 0, 0, 0},
      { 0, 0, 1, 0, 0, 0},
    };
    vector<vector<int> > graph {
      { 0, 0, r, r, r, 0},
      { 0, 0, 0, 0, o, 0},
      { y, 0, 0, 0, y, y},
      { g, 0, 0, 0, 0, 0},
      { b, b, b, 0, 0, 0},
      { 0, 0, v, 0, 0, 0},
    };

    //print(graph);

    int min =  INT_MAX;
    int idx = 0;
    for (int j = 0; j < 6; j++) {
      int s = 0;
      for (int k = 0; k < 6; k++) {
        s += graph[j][k];
      }
      if (s < min && s != 0) {
        min = s;
        idx = j;
      }
    }

    remove_color(graph, idx);

    vector<int> res = { idx };

    bool impossible = false;
    n--;
    while (n > 0) {
      //cout << "before : " ;
      //for (int j: res)
      //  cout << c[j];
      //cout << endl;
      //print(graph);
      int first = res[0];
      int last = res[res.size() - 1];

      bool inserted = false;
      for (int l = 0; l < 6; l++) {
        bool found = false;
        for (int t = 0; t < 6; t++) {
          if (graph[l][t] > 0) {
            found = true;
            break;
          }
        }
        if (!found)
          continue;
        int idx = l;
        //cout << "trying to insert " << idx << endl;
        for (int j = 0; j < res.size(); j++) {
          int c1 = res[j];
          int c2 = res[(j + 1) % res.size()];
        //  cout << "c1 " << c1 << " c2 " << c2 << endl;

          if (solutions[idx][c1] == 1 && (solutions[idx][c2] == 1 || j == res.size() - 1)) {
            //cout << "inserting at " << j << endl;
            res.insert(res.begin() + j + 1, idx);
            remove_color(graph, idx);
            inserted = true;
            break;
          }
        }
        if (inserted) {
          break;
        }
      }

      if (!inserted) {
          impossible = true;
          break;
      }

      //cout << "after" << endl;
      //print(graph);
      n--;
    }

    if (solutions[res[0]][res[res.size() - 1]] == 0)
      impossible = true;

    cout << "Case #" << i + 1 << ": ";
    if (impossible) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      for (int j: res)
        cout << c[j];
      cout << endl;
    }
  }
}
