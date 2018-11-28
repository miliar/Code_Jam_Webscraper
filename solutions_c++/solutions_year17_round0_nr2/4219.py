#include <bits/stdc++.h>

using namespace std;

bool perfect(string a){
  for(int i=0; i<a.length()-1; i++)
    if(a[i] > a[i+1]) return false;
  return true;
}

string make_tidy(string a){
  if(perfect(a)) return a;
  int n = a.length();
  for(int i=0; i<n-1; i++){
    if(a[i] <= a[i+1]){
      continue;
    }else{
      a[i] -= 1;
      for(int j=i+1; j<n; j++)
        a[j] = '9';
      break;
    }
  }
  return make_tidy(a);
}

string trim(string a){
  if(a[0] != '0') return a;
  return trim(a.substr(1));
}

int main(void){
  int t, game = 1;
  cin >> t;
  string a;
  while(t--){
    cin >> a;
    cout << "Case #" << game++ << ": " << trim(make_tidy(a)) << endl;
  }
}
