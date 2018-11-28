#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

void nextConfig(string &m, int k) {
  int l = m.length();
  int i = l - 1;
  for(i=k+1; i<l; i++) {
    m[i] = '9';
  }
  // cout << k << " " << m[k] << endl;
  m[k] -= 1;
}

int isZero(const string &m) {
  int l = m.length();
  int i = 0;

  while(i<l && m[i]=='0') i++;

  return (i>=l)?1:0;
}

/*
  return 1 if n is tidy, otherwise return 0
*/
int isTidyNumber(string n, int &k) {
  int l = n.length();
  char d, last_digit = '9';
  int i = l - 1;
  k = -1;
  while(i >= 0) {
    d = n[i--];
    if(d > last_digit) {
      if(d != '0') {
        k = i + 1;
        return 0;
      } else {
        for(int j=0;j<=i; j++){
          if(n[j]!='0') {
            k = i + 1;
            return 0;
          }
        }
        return 1;
      }
    }
    last_digit = d;
  }
  return 1;
}

int main(int argc, char** args) {
  if(argc < 3) {
    cout << "Not enough parameter." << endl;
    return 1;
  }
  ifstream input(args[1]);

  if(input.fail()) {
    cout << "Could not open input file." << endl;
    return 2;
  }

  ofstream fout(args[2]);

  int num_of_case;
  string n, m;
  int k, c, zero_leading;
  int l;
  input >> num_of_case;
  getline(input, n);
  for(c=0; c < num_of_case; c++) {
    getline(input, n);
    m = n;
    // cout << "case #" << c+1 << " number: " << m << endl;
    while(!isZero(m)) {
      if(isTidyNumber(m, k)) {
        zero_leading = 0;
        l = m.length();
        while(zero_leading<l && m[zero_leading]=='0') {
          zero_leading++;
        }
        for(int i=0; i<l-zero_leading+1; i++) {
          m[i] = m[i + zero_leading];
        }
        l -= zero_leading;
        string nm = m.substr(0, l);
        fout << "Case #" << (c+1) << ": " << nm << "\n";
        cout << "Case #" << (c+1) << ": N = "<< n <<" last tidy: " << m << " zero leading: " << zero_leading << "; len-after:"<< l<< endl;
        break;
      }

      nextConfig(m, k);
    }
  }

  input.close();
  fout.close();
  return 0;
}
