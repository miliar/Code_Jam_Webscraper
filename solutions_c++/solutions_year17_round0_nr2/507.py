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
  cin >> s;
  for (int i = s.size() - 1; i> 0; --i) {
    for (int j = i-1; j>=0; --j) {
      if (s[j] > s[i]) {
        for (int k=i; k < s.size(); ++k ) {
          s[k] = '9';
        }
        s[i-1]--;
      }
    }
  }
  bool print = false;
  for (int i=0; i< s.size(); ++i) {
    if (s[i] != '0') {
      print = true;
    }
    if (print) cout<<s[i];
  }
  cout<<endl;

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
