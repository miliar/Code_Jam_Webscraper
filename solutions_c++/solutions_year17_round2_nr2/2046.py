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

string rtn[NN];
string pr[NN];
int indi[7];
int curindi[6];

string temp[6] = {"R", "O", "Y", "G", "B", "V"};
unordered_map<string, vector<string>> ed;
unordered_map<string, int> geti;

int N;
int upto;
void pre() {
  for (int i=0; i<6; ++i) {
    geti[temp[i]] = i;
  }
  ed["R"].push_back("B");
  ed["R"].push_back("Y");
  ed["R"].push_back("G");

  ed["Y"].push_back("B");
  ed["Y"].push_back("R");
  ed["Y"].push_back("V");

  ed["B"].push_back("R");
  ed["B"].push_back("Y");
  ed["B"].push_back("O");

  ed["O"].push_back("B");
  ed["V"].push_back("Y");
  ed["G"].push_back("R");
}

bool good(int cur) {
  int ii = geti[pr[cur]];
  rtn[upto] = pr[cur];
  upto++;
  curindi[ii]++;
  if (upto == N) {
    for (string& nc : ed[pr[cur]]) {
      if (nc == pr[0]) {
        return true;
      }
    }
    curindi[ii]--;
    upto--;
    return false;
  }

  for (string& nc : ed[pr[cur]]) {
    int ni = geti[nc];
    if (curindi[ni] < indi[ni+1]) {
      if (good(curindi[ni])) {
        return true;
      }
    }
  }

  curindi[ii]--;
  upto--;
  return false;
}




char tmp[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};
map<char, int> orig;
map<char, int> nums;
void main2() {

  cin>>N;
  int x;
  upto = 0;
  indi[0] = 0;
  curindi[0] = 0;
  indi[6] = N;
  for (int i=0; i<6; ++i) {
    cin >>x;
    nums[tmp[i]] = x;
    orig[tmp[i]] = x;
  }
  char pps[3][2] = {{'O', 'B'},{'G', 'R'},{'V', 'Y'}};

  for (int i=0 ;i<3; ++i) {
    char c1 = pps[i][0];
    char c2 = pps[i][1];
    if (nums[c1] > 0) {
      nums[c2] -= nums[c1];
      if (nums[c2]<0 || (nums[c2] == 0  && N > nums[c1] * 2)) {
        cout<<"IMPOSSIBLE"<<endl;
        return;
      }
    }
  }
  char rems[3] = {'R', 'Y', 'B'};
  char minc = ' ';
  int maxn = 0;
  int minn = 0;
  char maxc = ' ';
  for (int i=0; i<3; ++i) {
    if (minc == ' ' || nums[minc] > nums[rems[i]]) {
      minc = rems[i];
      minn = nums[minc];
    }
  }
  for (int i=2; i>=0; --i) {
    if (maxc==' ' || nums[maxc] < nums[rems[i]]) {
      maxc = rems[i];
      maxn = nums[maxc];
    }
  }
  char midc = 'l';
  int midn = 0;
  for (int i=0; i<3; ++i) {
    if (rems[i] != maxc && rems[i] != minc) {
      midc = rems[i];
      midn = nums[midc];
    }
  }
//  cout<<minc<<" "<<midc<<" "<<maxc<<endl;
//  cout<<minn<<" "<<midn<<" "<<maxn<<endl;
  int su = nums['R']+ nums['Y'] + nums['B'];
  if (su - maxn < maxn) {
    cout<<"IMPOSSIBLE"<<endl;
    return;
  }
  stringstream ss;

  int fl = midn+ minn-maxn;
  for (int i=0;i < midn+minn-maxn; ++i) {
    ss << maxc<<midc<<minc;
  }

  midn-=fl;
  minn -= fl;
  for(int i=0 ;i<midn; ++i) {
    ss<<maxc<<midc;
  }

  for (int i=0; i<minn; ++i) {
    ss<<maxc<<minc;
  }
  cout<<ss.str()<<endl;
}

int main(int argc, char *argv[]) {
	cin>>cas;
  bool showtime = argc > 1;
  time_t starttime = 0;
  if (showtime) {
    time(&starttime);
  }
  pre();
	for(ca = 1; ca<=cas; ++ca) {
    if (showtime) {
      cerr<<ca<<"/"<<cas<<" "<<time(NULL) - starttime<<endl;
    }
		cout<<"Case #"<<ca<<": ";
    main2();
	}
}
