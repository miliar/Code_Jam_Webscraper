#include<iostream>
#include<string>
using namespace std;

int main(){
  int c = 0, t;
  string n, s;
  bool f;

  cin >> t;
  for(int i = 0; i < t; i++){
    cin >> n;
    f = 1;
    while(f){
      f = 0;
      for(int j = 0; j < n.size() - 1; j++){
        if(n[j] > n[j + 1]){
	  if(j == 0)
	    for(int k = 1; k < n.size(); k++)
	      n[k] = '9';
	  else
      	    n[j + 1] = '9';
	  n[j]--;
	  f = 1;
	}
      }
    }
    c++;
    cout << "Case #" << c << ": ";
    for(int j = 0; j < n.size(); j++){
      if(n[j] != '0')
        f = 1;
      if(f)
        cout << n[j];
    }
    cout << endl;
  }
  return 0;
}
