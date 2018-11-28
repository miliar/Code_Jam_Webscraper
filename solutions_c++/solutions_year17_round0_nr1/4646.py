//Author: Andres-Felipe Ortega-Montoya
//A.cpp
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ll TC;
  cin >> TC;
  for(int t=1; t <= TC;++t){
    string str;
    int k;
    cin >> str >> k;
    int n = 0;
    for(int i = 0; i <= str.size()-k; ++i){
      if(str[i] == '-'){
	++n;
	for(int j = i; j < i+k; ++j){
	  if(str[j] == '+'){
	    str[j] = '-';
	  }else{
	    str[j] = '+';
	  }
	}
      }
      //cout << str << "\n";
    }
    bool bad = false;
    for(int i = str.size()-k; i < str.size(); ++i){
      if(str[i] == '-'){
	bad = true;
	break;
      }
    }
    cout << "Case #" << t << ": ";
    if(bad){
      cout << "IMPOSSIBLE\n";
    }else{
      cout << n << "\n";
    }
  }
}
