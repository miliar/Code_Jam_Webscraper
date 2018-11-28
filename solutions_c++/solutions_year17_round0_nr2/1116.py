#define REP(i,n) for(int i=0; i<(int)(n); i++)

typedef long long ll;

#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

inline int getInt(){ int s; scanf("%d", &s); return s; }
inline string getStr(){ char s[32]; scanf("%s", s); return s; }

ll toLL(const string &s){
  ll ret;
  sscanf(s.c_str(), "%lld", &ret);
  return ret;
}

bool isTidy(const string &s){
  REP(i,s.size() - 1)
    if(s[i] > s[i + 1])
      return false;
  return true;
}

int main(){
  const int t = getInt();

  REP(c,t){
    const string s = getStr();

    string ans = s;
    if(!isTidy(ans)){
      for(int i = s.size() - 1; i >= 0; i--) if(s[i] != '0'){
	string ss = s;
	ss[i]--;
	for(int j = i + 1; j < (int)s.size(); j++)
	  ss[j] = '9';
	if(isTidy(ss)){
	  ans = ss;
	  break;
	}
      }
    }

    int idx = 0;
    while(ans[idx] == '0') idx++;
    printf("Case #%d: %s\n", c + 1, ans.c_str() + idx);
  }

  return 0;
}
