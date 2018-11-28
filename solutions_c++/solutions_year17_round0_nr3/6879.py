#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <fstream>
#include <queue>
#include <sstream>
using namespace std;

int clearQ(priority_queue<long long> &q) {
  priority_queue<long long> empty;
  swap(q, empty);
  return 0;
}

int main() {
  ifstream in("C-small.in");
  streambuf *cinbuf = cin.rdbuf();
  cin.rdbuf(in.rdbuf());

  ofstream out("C-small.out");
  streambuf *coutbuf = cout.rdbuf(); //save old buf
  cout.rdbuf(out.rdbuf());

  int t;
  priority_queue<long long> qc;
  long long n, k, cs;

  cin >> t;
  for(int i = 1; i <= t; i++) {
    cin >> n >> k;
    qc.push(n);
    while(!qc.empty() && k > 0) {
      cs = qc.top();
      qc.pop();
      if(cs == 0) {
        continue;
      }
      if(cs % 2) {
        qc.push(cs / 2);
        qc.push(cs / 2);
      } else {
        qc.push(cs / 2);
        qc.push((cs / 2) - 1);
      }
      k--;
    }
    clearQ(qc);
    cout << "Case #" << i << ": ";
    if(cs % 2) {
      cout << (cs / 2) << " " << (cs / 2) << endl;
    } else {
      cout << (cs / 2) << " " << (cs / 2) - 1 << endl;
    }
  }

  return 0;
}
