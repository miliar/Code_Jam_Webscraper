#include <iostream>
#include <string>

using namespace std;
int main(){
  int t,k,c;
  bool possible;
  string s;
  string::iterator it;  

  int cm;
  cin >> t;
  for(int i = 1; i <=t; ++i){
    cin.ignore();
    getline(cin,s,' ');
    cin >> k;

    it = s.end()-1;
    c = 0;
    for(it; it >= s.begin()+(k-1);--it){
      if(*it == '-'){
        //flip
        c++;
        for(int j = 0; j < k; j++){
          if(*(it-j) == '-')
            *(it-j) = '+';
          else *(it-j) = '-';
        }
        /* PRINT
        for(it = s.begin(); it!=s.end();++it){
          cout << *it;
        }
        cout << '\n';
        */
      }
    }

    possible = true;
    for(it = s.begin(); it!=s.end();++it){
      if(*it == '-'){
        cout << "Case #" << i << ": " << "IMPOSSIBLE" << '\n';
        possible = false;
        break;
      }
    }

    if(possible)
      cout << "Case #" << i << ": " << c << '\n';
  }
  return 0;
}
