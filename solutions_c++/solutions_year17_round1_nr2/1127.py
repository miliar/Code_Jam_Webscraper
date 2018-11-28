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
#include<utility>
#include<vector>

#define NN 50

using LL = long long int;
using namespace std;

int cas, ca;
int N, P;

LL R[NN];
vector<LL> servs[NN][NN];
vector<int> edges[NN];
bool used[NN];
int matches[NN];

bool hasinter(vector<LL>& a, vector<LL>& b) {
  for (int aa : a)  {
    for (int j= 0; j<b.size(); ++j) {

      int bb = b[j];
      if (aa == bb) return true;
    }
  }
  return false;
}


bool mat(int cur) {
  if (used[cur]) return false;
  used[cur] = true;
  for (int e : edges[cur]) {
    if (matches[e] == -1 || (matches[e] != cur && mat(matches[e]))) {
      matches[e] = cur;
      return true;
    }
  }
  return false;
}

void main2() {
  cin>>N>>P;
  memset(matches, -1, sizeof(matches));
  for (int i=0 ;i<N; ++i ){
    cin>>R[i];
    for (int j=0; j<P; ++j) {

      edges[j].clear();
      servs[i][j].clear();
    }
  }
  int ctn = 0;
  for (int i=0; i<N; ++i ) {
    for (int j=0; j<P; ++j) {
      LL x;
      cin>>x;
      for (LL ser = 1; true; ++ser) {
        if ((ser * R[i] * 9 <=  10 * x) && (10*x <= ser * R[i] * 11)) {
          servs[i][j].push_back(ser);
        } else if (10 * x < R[i] * ser * 9) {
          break;
        }
      }

      if (servs[i][j].size()) ctn++;

      if ( i >0) {
        for(int k=0; k<P; ++k) {
          if (hasinter(servs[i-1][k], servs[i][j])) {
            edges[k].push_back(j);
          }
        }
      }
    }
  }

  if (N == 2) {
    ctn =0;
    for (int i=0; i<P; ++i) {
      memset(used, 0, sizeof(used));
      if(mat(i)){
        ctn++;
      }
    }
    /*
    for (int i=0 ;i<P; ++i) {
      cout<<matches[i]<<" "<<i<<endl;

    }
    */
  }

  cout << ctn <<endl;


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
