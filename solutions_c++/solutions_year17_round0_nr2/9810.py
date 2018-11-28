#include <iostream>
#include <string>

using namespace std;

int main(){
  int t;
  cin >> t;
  for(int i = 0; i < t; ++i){
    string n;
    cin >> n;
    if(n.length() == 1){
      cout << "case #" << (i+1) << ": " << n << endl;
      continue;
    }
    int min = 0;
    int pos = 0;
    for(int j = 0; j < n.length(); ++j){
      int tmp = n[j] - '0';
      if(tmp == min){
	continue;
      } else if(tmp > min){
	min = tmp;
	pos = j;
	} else{
	n[pos] -= 1;
	for(int k = pos+1; k < n.length(); ++k){
	  n[k] = '9';
	}
	  break;
      }
    }
    for(int j = 0; j < n.length(); ++j){
      if(n[j] != '0')break;
      n = n.substr(j+1);
    }
    cout << "case #" << (i+1) << ": " << n << endl; 
  }
  
  return 0;
}
