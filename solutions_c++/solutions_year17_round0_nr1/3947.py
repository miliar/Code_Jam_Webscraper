#include <iostream>
#include <fstream>
#include <string>
#include <queue>

using namespace std;

ifstream infile;
ofstream outfile;

bool success;

int T;

string s;
int k;

int cnt;
queue<int> q;

void reset() {
  success = true;
  cnt = 0;
  while (!q.empty()) q.pop();
}

void read_from_file() {
  infile >> s >> k;
}

void write_to_file(bool success) {
  static int t = 0;
  ++t;
  outfile << "Case #" << t << ": ";

  if (success)
    outfile << cnt << endl;
  else
    outfile << "IMPOSSIBLE" << endl;
}

int main() {
  infile.open("file.in");
  outfile.open("file.out");

  infile >> T;

  while (T--) {
    reset();
    read_from_file();

    for (int i = 0; i <= s.length() - k; ++i) {
      if (!q.empty() && i == q.front() + k) q.pop();

      if ((s[i] == '-') != (q.size() % 2 == 1)) {
        ++cnt;
        q.push(i);
      }
    }

    for (int i = s.length() - k + 1; i < s.length(); ++i) {
      if (!q.empty() && i == q.front() + k) q.pop();

      if ((s[i] == '-') != (q.size() % 2 == 1)) success = false;
    }

    write_to_file(success);
  }

  infile.close();
  outfile.close();
  return 0;
}