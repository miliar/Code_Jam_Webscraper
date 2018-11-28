#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;

vector <int> v;
int n;

bool valid(string answer) {
  for(int j=0; j<n; j++) {
    if(answer[j]=='-') return false;
  }
  return true;
}

string dfs(int pos, string answer, char now) {
  return answer;
}




int main () {
  ofstream myfile;
  ifstream input;
  input.open("input.txt");
  myfile.open ("output.txt");
  int t;
  input>>t;
  for(int i=1; i<=t; i++){
    int r, o, y, g, b, v;
		input>>n>>r>>o>>y>>g>>b>>v;

    string answer = "";
    bool ok = true;

    for(int j=0; j<n+10; j++) {
      answer += '-';
    }

    if (r > n/2 || b > n/2 || y> n/2 || g > n/2 || o > n/2 || v> n/2 ) ok=false;
    else {
      if (r == max(r, max(b, y))){

        int rest = n;
        int pos = 0;
        while (r>rest/3) {
          answer[pos] = 'R';
          r--;
          if (b>y) {
            answer[pos+1] = 'B';
            b--;
          } else {
            answer[pos+1] = 'Y';
            y--;
          }
          pos+=2;
          rest-=2;
        }
        while (r+b+y > 0) {
          if (r>0) {
            answer[pos] = 'R';
            r--;
            pos++;
          }
          if (b>0) {
            answer[pos] = 'B';
            b--;
            pos++;
          }
          if (y>0) {
            answer[pos] = 'Y';
            y--;
            pos++;
          }
        }

      } else if (b == max(r, max(b, y))){

        int rest = n;
        int pos = 0;
        while (b>rest/3) {
          answer[pos] = 'B';
          b--;
          if (r>y) {
            answer[pos+1] = 'R';
            r--;
          } else {
            answer[pos+1] = 'Y';
            y--;
          }
          pos+=2;
          rest-=2;
        }
        while (r+b+y > 0) {
          if (b>0) {
            answer[pos] = 'B';
            b--;
            pos++;
          }
          if (r>0) {
            answer[pos] = 'R';
            r--;
            pos++;
          }
          if (y>0) {
            answer[pos] = 'Y';
            y--;
            pos++;
          }
        }

      } else {

        int rest = n;
        int pos = 0;
        while (y>rest/3) {
          answer[pos] = 'Y';
          y--;
          if (r>b) {
            answer[pos+1] = 'R';
            r--;
          } else {
            answer[pos+1] = 'B';
            b--;
          }
          pos+=2;
          rest-=2;
        }
        while (r+b+y > 0) {
          if (y>0) {
            answer[pos] = 'Y';
            y--;
            pos++;
          }
          if (b>0) {
            answer[pos] = 'B';
            b--;
            pos++;
          }
          if (r>0) {
            answer[pos] = 'R';
            r--;
            pos++;
          }
        }
      }
    }



    if (ok) {
      myfile<<"Case #"<<i<<": "<<string(answer.begin(), answer.begin() + n)<<endl;
    } else {
      myfile<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
    }
  }
  myfile.close();
  input.close();
  return 0;
}
