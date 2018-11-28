#include <iostream>
#include <string>
using namespace std;

void reverse(string* st, int s, int c){
    for(int i=s; i<s+c; i++){
        (*st)[i] = ((*st)[i] == '+' ? '-' : '+');
    }
}

int main() {
    int T;
    cin >> T;
    for (int num = 1; num <= T; num++){
      string s;
      cin >> s;
      int S;
      cin >> S;
      int l = s.length();
      int res = 0;
      for(int i=0; i<=l-S; i++){
        if(s[i] != '+'){
          res++;
          reverse(&s, i, S);
        }
      }
      bool flag = true;
      for(int i=0; i<l; i++){
        if(s[i] != '+'){
            flag = false;
            break;
        }
      }
      if(!flag){
        cout << "Case #" << num << ": IMPOSSIBLE" << endl;
      }else {
        cout << "Case #" << num << ": " << res << endl;
      }
    }
}

