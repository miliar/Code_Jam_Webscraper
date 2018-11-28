#include<iostream>
#include<string>
using namespace std;

int main(){
  string s;
  int n, k, cont, c = 0;
  bool f;

  cin >> n;
  for(int i = 0; i < n; i++){
    cin >> s >> k;
    f = 1;
    cont = 0;
    for(int j = 0; j < s.size(); j++){
      if(s[j] == '-'){
        s[j] = '+';
	cont++;
	for(int l = 1; l < k; l++){
	  if(j + l >= s.size()){
	    f = 0;
	    break;
	  }
	  if(s[j+l] == '-')
	    s[j+l] = '+';
	  else
	    s[j+l] = '-';
	}
      if(f == 0)
        break;
      }
    }
    c++;
    if(f)
      cout << "Case #" << c << ": " << cont << endl;
    else
      cout << "Case #" << c << ": IMPOSSIBLE" << endl;
  }
  return 0;
}
