#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("first.in");
ofstream fout("first.out");

#define cin fin
#define cout fout

int n , k , res = 0;
string s;

void change(int x){
  for(int i = 0 ; i < k ; i++)
    s[i+x] = (s[i+x] == '-' ? '+' : '-');
}

void solve(){
  for(int i = 0 ; i < s.size() - k + 1 ; i++)
    if(s[i] == '-'){
      res++;
      change(i);
    }
}

bool check(){
  for(int i = 0 ; i < s.size() ; i++)
    if(s[i] == '-')
      return false;
  return true;
}

void input(){
  cin >> n;
  for(int i = 1 ; i <= n ; i++){
    cin >> s >> k;
    solve();
    cout << "Case #" << i << ": ";
    if(check())
      cout << res << endl;
    else
      cout << "IMPOSSIBLE" << endl;
    res = 0;
  }
}

int main(){
  input();
  return 0;
}
