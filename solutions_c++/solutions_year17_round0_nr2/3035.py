
#include <iostream>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  for(int a = 1; a <= t; a++){
    string n;
    cin >> n;
    for(int i = n.length() - 1; i >= 0; i--){
      bool tidy = true;
      for(int j = i + 1; j < n.length(); j++){
        if(n[j] < n[i])
          tidy = false;
      }
      if(!tidy){
        n[i]--;
        for(int j = i + 1; j < n.length(); j++)
          n[j] = '9';
      }
    }

    while(n.length() > 1 && n[0] == '0')
      n.erase(0, 1);

    cout << "Case #" << a << ": " << n << endl;
  }

  return 0;
}
