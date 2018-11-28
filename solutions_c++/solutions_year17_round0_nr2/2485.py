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
  string s;
  cin >> t;
  rep(z,t){
    cin >> s;
    int i=0;
    int l=-1;
    bool flag=false,en=false;
    while(s[++i]!='\0'){
      if(s[i-1]<s[i]){l=i;flag=false;}
      else if(s[i-1]>s[i]){en=true;break;}
      else if(s[i-1]==s[i]){if(!flag) l=i-1; flag=true;}
    }
    cout << "Case #" << z+1 <<": ";
    if(s.length()==1 || !en) cout << s;
    else if(!flag){
      if(s[i-1]=='1')
	{while(s[i++] != '\0') cout << "9";}
      else{
      s[i-1]=s[i-1]-1;
      while(s[i] != '\0') s[i++]='9';
      cout << s;
      }
    }
    else if(flag){
      if(s[l]=='1')
	{while(s[++l] != '\0') cout << "9";}
      else{
	s[l]=s[l]-1;
	while(s[++l] != '\0') s[l]='9';
	cout << s;
      }
    }
    cout << endl; 
  }

  return 0;
}
