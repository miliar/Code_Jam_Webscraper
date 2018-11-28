#include<bits/stdc++.h>
#define ll long long
using namespace std;
string remove_trailing_zero(string x){
  if(x.size() == 1) return x;
  int sz = 0;
  while(x[sz] == '0') ++sz;
  return x.substr(sz);
}
int valid(string x){
  int flag = -1;
  for(int i = 0 ; i + 1 < x.size() ; ++i ){
    if(x[i] > x[i + 1]){
    flag = i;
    break;
    }
  }
  return flag;
}
string solve(string x){
     int index = valid(x);
     if(index == -1) return x;
     --x[index];
       for(int i = index + 1 ; i < x.size() ; ++i )  x[i] = '9';
       return solve(x);
}
int main(){
                cin.sync_with_stdio(false);
                ifstream cin("a.txt");
                ofstream cout("b.txt");
                int T;
                cin >> T;
                for(int i = 1 ; i <= T ; ++i ){
                  string x;
                  cin >> x;
                  cout << "Case #" << i <<": " << remove_trailing_zero(solve(x)) << endl;
                }
}
