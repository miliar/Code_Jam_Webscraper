#include <iostream>
#include <vector>
using namespace std;

string ch = "ROYGBV";
int main () {
  int T;
  cin >> T;
  for(int tc=1; tc<=T; tc++) {
    int N;
    vector<int> a(6,0);
    cin >> N >> a[0] >> a[1] >> a[2] >> a[3] >> a[4] >> a[5];
    bool flag = false;
    if(a[1] == a[4] && a[2] == 0 && a[3] == 0 && a[5] ==0 && a[0] == 0) {
      string ss= "";
      cout << "Case #" << tc << ": ";
      for(int i=0; i<a[4]; i++){
        cout << ch[4] << ch[1];
      }
      cout << endl;
      continue;
    }
    if(a[2] == a[5] && a[0] == 0 && a[1] == 0 && a[3] ==0 && a[4] == 0) {
      string ss= "";
      cout << "Case #" << tc << ": ";
      for(int i=0; i<a[2]; i++){
        cout << ch[2] << ch[5];
      }
      cout << endl;
      continue;
    }
    if(a[0] == a[3] && a[1] == 0 && a[2] == 0 && a[4] ==0 && a[5] == 0) {
      string ss= "";
      cout << "Case #" << tc << ": ";
      for(int i=0; i<a[0]; i++){
        cout << ch[0] << ch[3];
      }
      cout << endl;
      continue;
    }
    if((a[1] >0 && (a[1]+1 > a[4])) || (a[3] >0 && (a[3]+1 > a[0])) || (a[5] >0 && (a[5] +1 > a[2]))) {
      cout << "Case #" << tc << ": " << "IMPOSSIBLE" << endl;
      continue;
    }
    vector<int> fl(6, 0);
    vector<string> str(6, "");
    string& RG = str[0];
    for(int i=0; i<a[3]; i++) {
      RG = RG + 'R' + 'G';
    }
    RG += 'R';
    a[0] -= a[3];
    if(a[3] > 0) fl[0] = 1;
    string& YV = str[2];
    for(int i=0; i<a[5]; i++) {
      YV = YV + 'Y' + 'V';
    }
    YV += 'Y';
    a[2] -= a[5];
    if(a[5] >0 ) fl[2] = 1;
    string& BO = str[4];
    for(int i=0; i<a[1]; i++) {
      BO = BO + 'B' + 'O';
    }
    BO += 'B';
    a[4] -= a[1];
    if(a[1] >0) fl[4] = 1;
    int largest = 0;
    if(a[0] >= a[2]) {
      if(a[0]<a[4]) {
        largest = 4;
      }
    }else {
      if(a[2]>=a[4]){
        largest = 2;
      }else {
        largest = 4;
      }
    }
    vector<string> b(a[largest]);
    int sl=0,tl=0;
    if(largest == 0) {
      if(a[2]+a[4] <a[0]){
        flag = true;
      }else{
        sl=2;
        tl=4;
        if(a[4] > a[2]) {
          tl=2;
          sl=4;
        }
      }
    }else if(largest == 2) {
      if(a[0]+a[4] < a[2]) {
        flag = true;
      }else{
        sl=0;
        tl=4;
        if(a[4] > a[0]){
          tl=0;
          sl=4;
        }
      }
    }else {
      if(a[0]+a[2] < a[4]) {
        flag = true;
      }else {
        sl=0;
        tl=2;
        if(a[2] >a[0]) {
          sl=2;
          tl=0;
        }
      }
    }
    for(int i=0; i<a[sl]; i++) {
      b[i] = ch[largest];
      if(fl[largest]) {
        b[i] = str[largest];
        fl[largest]=0;
      }
      if(fl[sl]) {
        b[i] += str[sl];
        fl[sl]=0;
      }else{
        b[i] += ch[sl];
      }
    }
    for(int i=a[sl]; i<a[largest]; i++) {
      if(fl[largest]) {
        b[i] = str[largest];
        fl[largest] = 0;
      }else
        b[i] = ch[largest];
    }
    for(int i=a[largest]-1; i>=a[largest]-a[tl]; i--) {
      if(fl[tl]) {
        b[i] += str[tl];
        fl[tl]=0;
      }else
        b[i] += ch[tl];
    }
    string pos;
    for(int i=0; i<a[largest]; i++) {
      pos+=b[i];
    }
    string imp = "IMPOSSIBLE";
    cout << "Case #" << tc << ": " << (flag? imp : pos) << endl;
  }
}
