#include <iostream>
#include <string>
using namespace std;

string generate(int length) {
  string output = "+";
  for (int i = 1; i < length; i++) {
    output += "+";
  }
  return output;
}

int main() {
  int N;
  cin >> N;
  for(int i = 0; i < N; i++) {
    string line;
    cin >> line;
    int n;
    cin >> n;
    int length = line.length();
    int count = 0;
    for (int i = 0; i < length - n + 1; i++) {
      if (line[i] == '-') {
        for (int j = 0; j < n; j++) {
          line[i + j] = line[i + j] == '-' ? '+' : '-';
        }
        count++;
      }
      else {
        continue;
      }
    }
    string s = generate(length);
    if (s == line) cout << "Case #" << i+1 << ": " << count << endl;
    else cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
  }
  return 0;
}
