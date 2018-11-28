#include <iostream>
#include<cstdio>
using namespace std;

int main(){
  ios_base::sync_with_stdio(true);

  int t; cin >> t;
  for  (int id = 1; id <= t; id++) {
    string s; cin >> s; int l = s.length();
    int n[s.length()];
    for (int i = 0; i < s.length(); i++) {
      n[i] = int(s[i]) - int('0');
    }
    int min = n[l-1]; int pos = l;
    for (int i = l-2; i >=0 ; i--) {
      if (n[i] > min) {
        n[i] --; // dalej same dziewiątki
        pos = i;
      }
      min = n[i];
    }
    for (int i = pos+1; i < l; i++) n[i] = 9;
    bool start = false;
    cout << "Case #" << id << ": ";
    for (int i = 0; i < l; i++) {
      if (n[i] != 0 || start) {
        start = true;
        cout << n[i];
      }
    }
    cout << endl;
  }
}
