#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
using namespace std;

#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)

typedef long long ll;


int main(){
  int t;
  cin >> t;
  string s;
  rep(i,t){
    int k;
    cin >> s;
    cin >> k;
    int j=0;
    int c=0;
    while(s[j]!='\0'){
      if(s[j]=='+')j++;
      else{
	if(k+j>s.length()){c=-1;break;}
	else{
	  c++;
	  rep(l,k){
	    if(s[j+l]=='+') s[j+l]='-';
	    else s[j+l]='+';
	  }
	}
      }
    }
    cout << "Case #" << i+1 << ": ";
    if(c==-1){cout << "IMPOSSIBLE" << endl;}
    else {cout << c << endl;}
  }

  return 0;
}
