#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("aa.out");

#define cin fin
#define cout fout

int t , R , C;
string s[30];

void solve(int x , int y){
  for(int i = x ; i >= 0 ; i--)
    if(s[i][y] != '?')
      for(int j = i + 1 ; j <= x && s[j][y] == '?' ; j++)
	s[j][y] = s[i][y];
  int ii = -1 , jj_plus = 0 , jj_minus = 0;
  for(int i = 0 ; i <= x ; i++)
    if(s[i][y] != '?'){
      ii = i;
      break;
    }
  if(ii != -1)
    for(int i = 0 ; i < ii ; i++)
      s[i][y] = s[ii][y];
  if(y < C)
    for(int i = 0 ; i <= x ; i++)
      jj_plus += (s[i][y+1] != '?' ? 1 : 0);
  if(ii == -1 && jj_plus == R)
    for(int i = 0 ; i <= x ; i++)
      s[i][y] = s[i][y+1];
  if(y > 0)
    solve(x , y-1);
  if(y > 0)
    for(int i = 0 ; i <= x ; i++)
      jj_minus += (s[i][y-1] != '?' ? 1 : 0);
  if(ii == -1 && jj_minus == R)
    for(int i = 0 ; i <= x ; i++)
      s[i][y] = s[i][y-1];
}

void input(){
  cin >> t;
  for(int i = 1 ; i <= t ; i++){
    cin >> R >> C;
    for(int j = 0 ; j < R ; j++)
      cin >> s[j];
    solve(R - 1, C - 1);
    cout << "Case #" << i << ":" << endl;
    for(int j = 0 ; j < R ; j++)
      cout << s[j] << endl;
  }
}

int main(){
  input();
  return 0;
}
