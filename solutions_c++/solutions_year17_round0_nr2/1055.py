#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

const char* fi = "B-large.in";
const char* fo = "B-large.out";

void check(vector<int> &a, int index) {
  a[index]--;
  if (index == 0 || a[index] >= a[index - 1]) return;
  a[index] = 9;
  check(a, index - 1);
}

void solve(vector<int> &a) {
  int p = 0;
  for (int i = 1; i < a.size(); i++) {
    if (p > 0) {
      a[i] = 9;
    } else {
      if (a[i] < a[i - 1]) {
        a[i] = 9;
        check(a, i - 1);
        p = i;
      }
    }
  }
}

int main(int argc, const char * argv[]) {
  ifstream fin;
  fin.open(fi);
  
  ofstream fout;
  fout.open(fo);
  
  int nTest;
  fin >> nTest;
  for (int test = 1; test <= nTest; test++) {
    string s;
    fin >> s;
    
    vector<int> a = vector<int>(s.length() + 1);
    a[0] = 0;
    for (int i = 0; i < s.length(); i++) {
      a[i + 1] = s[i] - 48;
    }
    
    fout << "Case #" << test << ": ";
    solve(a);
    int i = 0;
    while (a[i] <= 0 && i < a.size()) i++;
    
    for (; i < a.size(); i++) {
      fout << a[i];
    }
    fout << endl;
  }
  
  fin.close();
  fout.close();
  return 0;
}
