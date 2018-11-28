#include <bits/stdc++.h>

using namespace std;
int n,a[7];
int ans[1002+1];

int getMax(){
  int idx=0,curr=0;
  for(int i=0;i<6;i++) {
    if (a[i] > curr){
      curr = a[i];
      idx =i;
    }
  }
  return idx;
}

bool isSafe(int idx, int i) {
  if(ans[(i-1+n)%n] == idx){
    return false;
  }
  if (ans[(i+1+n)%n] == idx) {
    return false;
  }
  return true;
}

int main() {
  // freopen("inb.in","r",stdin);
  // freopen("outb.txt","w",stdout);
  int t;cin>>t;
  map <int, char> co;
  co[0]='R';
  co[1]='O';
  co[2]='Y';
  co[3]='G';
  co[4]='B';
  co[5]='V';
  for(int test=1;test<=t;test++) {

    cin>>n;
    for(int i=0;i<7;i++){
      a[i] = 0;
    }

    for(int i=0;i<6;i++){
      cin>>a[i];
    }

    memset(ans, -1, sizeof(ans));

    bool flag = false;

    for(int i=0;i<n;i++) {
      int idx = getMax();
      cout<<idx<<" "<<a[idx]<<endl;
      if(a[idx] == 0) {
        break;
      }

      a[idx]--;
      bool placed = false;
      for(int j=0;j<n;j++){
        if(ans[j]==-1 && isSafe(idx, j)){
          ans[j] = idx;
          placed = true;
          break;
        }
      }

      if (!placed) {
        cout<<"b"<<idx;
        flag = true;
        break;
      }
    }
    cout<<"Case #"<<test<<": ";
    if(flag){
      cout<<"IMPOSSIBLE"<<endl;
    }else {
    for(int i=0;i<n;i++){
      cout<<co[ans[i]];
    }
    cout<<endl;
  }
  }
  return 0;
}
