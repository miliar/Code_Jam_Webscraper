#include<iostream>
#include<cstring>
#include<string>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<unordered_map>
#include<list>
#include<utility>
#include<algorithm>

#define NN 1000

using LL = long long int;
using namespace std;

int cas, ca;

void main2() {
  string s;
  int k, rtn = 0;
  cin >> s >> k;

  for (int i=0; i<s.size(); ++i ){
    if (s[i] == '+') continue;
    if (i+k-1 >= s.length()) {
      cout<<"IMPOSSIBLE"<<endl;
      return;
    }
    rtn++;
    for (int j=0 ;j<k; ++j) {
      s[i+j] = s[i+j] == '-' ? '+' : '-';
    }
  }
  cout<< rtn<<endl;
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
