#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("b_large.in");
ofstream fout("b_large.out");

#define cin fin
#define cout fout

int n;
string f;

string solve(string k){
  string res = "" , s = "";
  int i = 1;
  while(i < k.size() && k[i] - '0' >= k[i-1] - '0'){
    i++;
  }
  if(i == k.size())
    return k;
  for(int j = 0 ; j < i-1 ; j++)
    res += k[j];
  res += ((k[i-1] - '0' - 1) + '0');
  res = solve(res);
  for(; i < k.size() ; i++)
    res += "9";
  s = res;
  res = "";
  i = (s[0] == '0') ? 1 : 0;
  for(; i < s.size() ; i++)
    res += s[i];
  return res;
}

void input(){
  cin >> n;
  for(int i = 1 ; i <= n ; i++){
    cin >> f;
    cout << "Case #" << i << ": " << solve(f) << endl;
  }
}

int main(){
  input();
  return 0;
}
