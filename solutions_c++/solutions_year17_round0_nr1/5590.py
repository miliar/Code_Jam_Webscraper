#include <iostream>
#define endl '\n' 

using namespace std;

void flip(string& s, int i, int k){
  for(int j=i; j<i+k; j++){
    if(s[j]=='-') s[j] = '+';
    else s[j] = '-';
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  string s;
  int k, n, count;
  bool possible;
  for(int ind=0; ind<T; ind++){
    cin >> s;
    cin >> k;
    n = s.length();
    count=0;
    for(int i=0; i<n-k+1; i++){
      if(s[i]=='-'){
        flip(s,i,k);
        count++;
      }
    }
    possible = true;
    for(int i=n-k+1; i<n; i++)
      if(s[i]=='-'){
        possible=false;
        break;
      }
    cout << "Case #" << (ind+1) << ": ";
    if(possible)
      cout << count << endl;
    else
      cout << "IMPOSSIBLE" << endl;
  }
  return 0;
}