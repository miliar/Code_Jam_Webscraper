
/*Aman Singh's competitive coding template
  aman_singh[at]students[dot]iitmandi[dot]ac[dot]in  */

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);
  int test, k, i, j, count, m;
  string s;
  bool flag;
  cin >> test;
  m = 0;
  while(test--){
    m++;
    flag = false;
    count = 0;
    cin >> s;
    cin >> k;
    for (i = 0; i<s.length() - k + 1; i++) {
      if(s[i] == '-'){
	// 	cout << " 324" << endl;
	count++;
	for (j = 0; j < k && (j + i)<s.length(); j++) {
	  s[j + i] = (s[j + i] == '+') ? '-' : '+';
	}
      }
      // cout << s << endl;
    }
    for (i = 0; i<s.length(); i++) {
      if(s[i] == '-'){
	flag = true;
	break;
      }
    }
    if(!flag)
      cout <<" Case #" << m << ": "<< count << endl;
    else
      cout  <<" Case #" << m << ": "<< "IMPOSSIBLE" << endl;
  }
  return 0;
}
