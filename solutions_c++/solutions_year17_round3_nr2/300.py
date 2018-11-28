#include<algorithm>
#include<cassert>
#include<cstring>
#include<iostream>
#include<list>
#include<map>
#include<set>
#include<sstream>
#include<string>
#include<unordered_map>
#include<unordered_set>
#include<utility>
#include<vector>

#define NN 1000

using LL = long long int;
using namespace std;

int cas, ca;
int na, nb;
bool aav[1440];
bool bav[1440];
int inf = 1<<28;
int dp[1440][720][2];
int start;
int go(int cur, int sofar, int aturn) {
  if (cur == 1440) {
    if (sofar < 720) return inf;
    return aturn == start ? 0 : 1;
  }

  if (sofar == 720) {
    for (int i = cur; i<1440; ++i) {
      if (!bav[i]) return inf;
    }
    int ch = aturn ? 1 : 0;
    int end = start == 0 ? 0 : 1;
    return ch + end;
  }
  if (720-sofar > 1440-cur) return inf;

  if(dp[cur][sofar][aturn]>=0) return dp[cur][sofar][aturn];

  int rtn = inf;


  if ((aturn && aav[cur]) || (!aturn && bav[cur])) {
    rtn = min(rtn, go(cur+1, sofar + (aturn ? 1 : 0), aturn));
  }
  if ( (aturn && bav[cur]) || (!aturn && aav[cur]) ) {
    rtn = min(rtn, 1+go(cur+1, sofar + (aturn ? 0 : 1), 1-aturn));
  }

  dp[cur][sofar][aturn] = rtn;
  return rtn;

}

void main2() {
  cin >>na>>nb;
  memset(dp, -1, sizeof(dp));
  int a,b;
  for (int i=0; i<1440; ++i ){
    aav[i] = true;
    bav[i] = true;
  }
  for (int i=0; i<na; ++i) {
    cin>>a>>b;
    for (int j=a; j<b; ++j ) {
      aav[j] = false;
    }
  }
  for (int i=0; i<nb; ++i) {
    cin>>a>>b;
    for (int j=a; j<b; ++j ) {
      bav[j] = false;
    }
  }

  start = 0;
  int rtn = go(0, 0, 0);
  memset(dp, -1, sizeof(dp));
  start = 1;
  rtn = min(rtn, go(0, 0, 1));
  cout<<rtn<<endl;
}

int main(int argc, char *argv[]) {
  cin>>cas;
  bool showtime = argc > 1;
  time_t starttime = 0;
  if (showtime) {
    time(&starttime);
  }
  for(ca = 1; ca<=cas; ++ca) {
    if (showtime) {
      cerr<<ca<<"/"<<cas<<" "<<time(NULL) - starttime<<endl;
    }
    cout<<"Case #"<<ca<<": ";
    main2();
  }
}
