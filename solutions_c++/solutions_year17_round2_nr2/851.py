
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <vector>

using namespace std;

bool ok(char a, char b) {
  if (a == b) return false;
  return true;
}

bool bylen(const vector<string>& a,
           const vector<string>& b) {
  return a.size() < b.size();
}

struct Compare { 
  bool operator()(const vector<string>& a, const vector<string>& b) {
    return a.size() < b.size();
  }
};

vector<string> generate(std::string primary, std::string secondary, int primary_count,
                        int secondary_count) {
  string t;
  for(int i = 0; i < secondary_count; ++i) {
    t += primary + secondary;
  }
  primary_count -= secondary_count;
  if(primary_count > 0) {
    t += primary;
    --primary_count;
  }
  vector<string> result(primary_count, primary);
  result.push_back(t);
  return result;
}

void solve(int t, int N, int R, int O, int Y, int G, int B, int V) {
  // special cases.
  if(N == 1) {
    string result;
    if(R == 1) { result = "R"; }
    if(O == 1) { result = "O"; }
    if(Y == 1) { result = "Y"; }
    if(G == 1) { result = "G"; }
    if(B == 1) { result = "B"; }
    if(V == 1) { result = "V"; }        
    cout << "Case #" << t << ": " << result << endl;
    return;
  }
  bool impossible = false;
  if(R == G && R > 0 && N > R + G) {
    impossible = true;
  }
  if(B == O && B > 0 && N > B + O) {
    impossible = true;
  }
  if(Y == V && Y > 0 && N > Y + V) {
    impossible = true;
  }

  auto Bp = B - O;
  auto Rp = R - G;
  auto Yp = Y - V;
  if (N > 1 && (
          Bp > Rp + Yp ||
          Rp > Bp + Yp ||
          Yp > Bp + Rp)) {
    impossible = true;
  }

  if(impossible) {
    cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    return;
  }
  priority_queue<vector<string>, vector<vector<string>>, Compare> possible;
  possible.push(generate("R", "G", R, G));
  possible.push(generate("B", "O", B, O));
  possible.push(generate("Y", "V", Y, V));

  vector<string> parts;
  auto s = possible.top();
  possible.pop();

  for(auto c: s) {
    parts.push_back(c);
  }
  // cout << "parts: " << parts.size() << endl;
  size_t i = 0;

  while(!possible.empty()) {
    auto s = possible.top();
    possible.pop();
    for(auto c : s) {
      parts[i] += c;
      i += 1;
      if (i == parts.size()) {
        i = 0;
      }
    }
  }
  
  string result;
  for(auto p : parts) {
    result += p;
  }

  cout << "Case #" << t << ": " << result << endl;

}

int main() {
  int t_num;
  cin >> t_num;
  for (auto t = 1; t <= t_num; ++t) {
    int N, R, O, Y, G, B, V;
    cin >> N >> R>> O>> Y>> G>> B>> V;
    solve(t, N, R, O, Y, G, B, V);
  }
}
