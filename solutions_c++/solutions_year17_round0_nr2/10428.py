typedef unsigned long long ll;
#include <iostream>
#include <string>

using namespace std;

int num[18], s;

int ch(char c){
  return c - '0';
}

string rCh(string str, int i){
  if(i==0 && ch(str[0]) == 1){
    str = "";
    for(int j = 0; j < s - 1; j++){
      str += '0' + 9;
    }
    return str;
  }
  int x = ch(str[i]) - 1;
  str[i] = '0' + x;
  for(int j = i + 1; j < s; j++){
    str[j] = '0' + 9;
  }
  return str;
}

int main(){
  string n;
  int t, count = 1;
  cin >> t;
  while(t--){
    int x = 0;
    bool f = true, chain = true;
    cin >> n;
    s = n.size();
    for(int i = 0; i < s-1; i++){
      if(ch(n[i])==ch(n[i+1])){
	if(f){
	  x = i;
	  f = false;
	}
	chain = true;
      }
      if(ch(n[i])>ch(n[i+1])){
	if (chain) n = rCh(n, x);
	else n = rCh(n,i);
	break;
      }
      if(ch(n[i])<ch(n[i+1]))chain = false;
    }
    cout << "Case #" << count << ": " << n << endl;
    count++;
  }
  return 0;
}
