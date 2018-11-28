#include <algorithm>
#include <array>
#include <bitset>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
typedef long long ll;

using namespace std;

const string kInputFilename = "input.txt";
const string kOutputFilename = "output.txt";

ifstream in("input.txt");
ofstream out("output.txt");
//ifstream in("A-small-attempt0.in");
//ofstream out("A-small-attempt0.out");
//ifstream in("A-small-attempt1.in");
//ofstream out("A-small-attempt1.out");
//ifstream in("A-small-attempt2.in");
//ofstream out("A-small-attempt2.out");
//ifstream in("A-small-attempt3.in");
//ofstream out("A-small-attempt3.out");
//ifstream in("A-small-attempt4.in");
//ofstream out("A-small-attempt4.out");
//ifstream in("A-small-attempt5.in");
//ofstream out("A-small-attempt5.out");
//ifstream in("A-large.in");
//ofstream out("A-large.out");
int main() {
  int T;
  in >> T;
  for (int ti=0;ti<T;ti++){
    int R,C;
    in>>R>>C;
    string S[R];
    for (int ri=0;ri<R;ri++){
        in>>S[ri];
    }
     for (int ri=0;ri<R;ri++){
        bool kid=false;
        char t='?';
        string s=S[ri];
        for (int i=0;i<C;i++){
            if (kid==false){
                if (s[i]!='?'){
                    kid=true;
                    t=s[i];
                    for (int j=0;j<=i;j++){
                        s[j]=t;
                    }
                }
            }
            else{
                if (s[i]!='?'){
                    t=s[i];
                }
                s[i]=t;
            }
        }
        S[ri]=s;
    }

    bool line=false;
    string temp;
    for (int ri=0;ri<R;ri++){
        string s=S[ri];
        if (line==false){
            if (s[0]!='?'){
                temp=S[ri];
                line=true;
                for (int j=0;j<ri;j++){
                    S[j]=temp;
                }
            }
        }
        else{
            if (s[0]!='?'){
                temp=s;
            }
            S[ri]=temp;
        }
    }

    out<<"Case #"<<ti+1<<": "<<endl;
    for (int ri=0;ri<R;ri++){
        out<<S[ri]<<endl;
    }

  }
  out.close();
  return(0);
}
