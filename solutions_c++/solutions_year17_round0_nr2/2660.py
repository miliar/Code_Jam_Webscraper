#include <string>
#include <iostream>

#define REP(i,n) for(int i = 0; i < n; ++i)

using namespace std;


int main(int arcg, char **argv){
  int T;
  cin >> T;
  REP(i,T) {
    string in; 
    cin >> in; 
    int k = 0;
    while ((k < in.size()) and (in[k] <= in[k+1])) ++k;
    if (k < in.size() - 1) in[k] -= 1;
    for (int j = k+1; j< in.size(); ++j)
      in[j] = '9';
    while (in[k] < in[k-1] or in[k] == '0'){
      if (k == 0){
	break;
      } else {
	in[k] = '9';
	in[--k] -= 1;
      }
    }
    string s;
    int a = 0;
    while (in[a] == '0') ++a;
    for (; a < in.size(); ++a)
      s += in[a];
    in = s;
   cout << "Case #" << i+1 << ": " << in << endl; 
  }
  return 0;
}
