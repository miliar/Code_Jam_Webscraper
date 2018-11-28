#include <iostream>
#include <fstream>
#define f(i,a,b) for(int i=a; i<=b; i++)

using namespace std;

int t,k,kq,x[1005];
string st;

void Solve() {
   kq=0;
   f(i,0,st.size()-1)
     if (st[i]=='+') x[i+1]=1;
     else x[i+1]=0;

   f(i,1,st.size()-k+1) {

      if (x[i]==0) {
        f(j,i,i+k-1) x[j]=1-x[j];
        kq++;
      }
   }
   f(i,1,st.size())
     if (x[i]==0) kq=-1;
}

int main() {
   ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
   cin >> t;
   f(test,1,t) {
    cin >> st >> k;
    Solve();
    cout <<  "Case #" << test << ": ";
    if (kq==-1) cout <<"IMPOSSIBLE" << endl;
    else cout << kq << endl;
   }
}
