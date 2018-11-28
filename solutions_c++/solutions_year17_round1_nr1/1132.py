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

#define NN 25

using LL = long long int;
using namespace std;

int cas, ca;

int R,C;
string board[NN];
vector<int> emps;
bool embool[NN];
char chs[NN];
void print() {
  for (int i=0 ;i<R; ++i ){
    cout << board[i]<<endl;
  }
}
void main2() {
  cin>>R>>C;

  memset(embool, 0, sizeof(embool));
  emps.clear();
  for (int i=0 ;i <R; ++i) {
    cin>>board[i];
    bool emp = true;
    int ctn = 0;
    for (int j=0; j<C; ++j) {
      if (board[i][j] != '?') {
        emp = false;
        chs[ctn++] = board[i][j];
      }
    }
    if (emp) {
      emps.push_back(i);
      embool[i] = true;
    } else {
      int it = 0;
      for (int j=0; j<C; ++j) {
        if (board[i][j] == '?') {
          board[i][j] = chs[it];
        } else if (it < ctn-1) {
          it++;
        }
      }
    }
  }
  for (int ei : emps) {
    int mod = ei -1;
    if (ei == 0) {
      for (mod = ei +1; embool[mod] ; mod++);
    }
    board[ei] = board[mod];
  }
  print();

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
		cout<<"Case #"<<ca<<":"<<endl;
    main2();
	}
}
