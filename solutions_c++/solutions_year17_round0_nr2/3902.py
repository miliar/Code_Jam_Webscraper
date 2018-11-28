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

void reset() {
  success = true;
}

void read_from_file() {
  infile >> s;
}

void write_to_file(bool success) {
  static int t = 0;
  ++t;
  outfile << "Case #" << t << ": ";

  if (success)
    outfile << s << endl;
  else {
    for (int i = 1; i < s.length(); ++i) outfile << '9';
    outfile << endl;
  }
}

bool play(int index, int minimum) {
  if (index == s.length() - 1) return s[index] - '0' >= minimum;

  if (s[index] - '0' < minimum) return false;
  if (s[index] - '0' == minimum) return play(index + 1, minimum);

  if (play(index + 1, s[index] - '0'))
    return true;
  else {
    --s[index];
    for (int i = index + 1; i < s.length(); ++i) s[i] = '9';
    return true;
  }
}

int main() {
  infile.open("file.in");
  outfile.open("file.out");

  infile >> T;

  while (T--) {
    reset();
    read_from_file();

    success = play(0, 1);

    write_to_file(success);
  }

  infile.close();
  outfile.close();
  return 0;
}