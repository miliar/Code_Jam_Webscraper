#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;

int main() {
  ifstream myInput;
  ofstream myOutput;
  myInput.open("A-large.in");
  myOutput.open("outputa.txt");
  int n;
  myInput >> n;
  for(int testCase=1; testCase<n+1; testCase++) {
    string S;
    int k;
    myInput>>S>>k;
    string ans = "IMPOSSIBLE";
    int change = 0;

    int cur = 0;
    vector<int> lazy;
    for(int i=0; i<S.size(); i++) {
      lazy.push_back(0);
    }

    bool ok = true;
    for(int i=0; i<S.size(); i++) {
      if(S[i] == '-' && cur%2 == 0) {
        change ++;
        if(i+k-1 > S.size() - 1) {
          ok = false;
          break;
        }
        cur++;
        lazy[i+k-1] -= 1;
      } else if(S[i] == '+' && cur%2 == 1) {
        change ++;
        if(i+k-1 > S.size() - 1) {
          ok = false;
          break;
        }
        cur++;
        lazy[i+k-1] -= 1;
      }
      cur+=lazy[i];
    }
    lazy.clear();

    ans = ok ? to_string(change) : ans;
    myOutput<<"Case #"<<testCase<<": "<<ans<<endl;
  }
}
