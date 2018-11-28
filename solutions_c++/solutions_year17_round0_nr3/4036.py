#include <iostream>
#include <fstream>
#include <utility>
#include <queue>

using namespace std;

ifstream infile;
ofstream outfile;

bool success;

int T;

long long K, N;

priority_queue<pair<long long, long long> > q;
long long cnt;
long long maximum, minimum;

void reset() {
  success = true;
  cnt = 0;
  while (!q.empty()) q.pop();
}

void read_from_file() {
  infile >> N >> K;
}

void write_to_file(bool success) {
  static int t = 0;
  ++t;
  outfile << "Case #" << t << ": ";

  outfile << maximum << " " << minimum;

  outfile << endl;
}

int main() {
  infile.open("file.in");
  outfile.open("file.out");

  infile >> T;

  while (T--) {
    reset();
    read_from_file();

    q.push(make_pair(N, 1LL));

    while (cnt < K) {
      long long prev_length = q.top().first;
      long long prev_cnt = q.top().second;
      q.pop();

      cnt += prev_cnt;

      if (prev_length % 2 == 1) {
        q.push(make_pair(prev_length / 2, prev_cnt * 2));
        maximum = prev_length / 2;
        minimum = prev_length / 2;
      }
      else {
        q.push(make_pair(prev_length / 2, prev_cnt));
        q.push(make_pair(prev_length / 2 - 1LL, prev_cnt));
        maximum = prev_length / 2;
        minimum = prev_length / 2 - 1LL;
      }
    }

    write_to_file(success);
  }

  infile.close();
  outfile.close();
  return 0;
}