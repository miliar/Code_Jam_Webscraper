#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
using namespace std;
typedef long long ll;
int T,P,x,N,nr[10];
int best[101][101][101];
vector<vector<int> > v;

int main() {
  cin.sync_with_stdio(false);
  cin>>T;
  for(int t=1;t<=T;++t) {
    cin>>N>>P;
    for(int i=0;i<P;++i) {
      nr[i] = 0;
    }
    for(int i=1;i<=N;++i) {
      cin>>x;
      ++nr[x%P];
    }
    if(P == 2) {
      cout<<"Case #"<<t<<": "<<nr[0] + (nr[1]+1)/2<<"\n";
      continue;
    }
    if(P == 3) {
      if(nr[1] > nr[2]) swap(nr[1],nr[2]);
      cout<<"Case #"<<t<<": "<<nr[0] + nr[1] + (nr[2] - nr[1] + 2) / 3 <<"\n";
      continue;
    }
    int ret = nr[0];
    for(int i=0;i<=nr[1];++i) {
      for(int j=0;j<=nr[2];++j) {
        for(int k=0;k<=nr[3];++k) {
          best[i][j][k] = 0; 
        }
      }
    }
    for(int i=0;i<=nr[1];++i) {
      for(int j=0;j<=nr[2];++j) {
        for(int k=0;k<=nr[3];++k) {
          if(i > 0) {
            int ok = ( ( i-1 + 2*j + 3*k )%4 == 0);
            best[i][j][k] = max(best[i][j][k], best[i-1][j][k] + ok);
          }
          if(j > 0) {
            int ok = ( ( i + 2*(j-1) + 3*k )%4 == 0);
            best[i][j][k] = max(best[i][j][k], best[i][j-1][k] + ok);
          }
          if(k > 0) {
            int ok = ( ( i + 2*j + 3*(k-1) )%4 == 0);
            best[i][j][k] = max(best[i][j][k], best[i][j][k-1] + ok);
          }
        }
      }
    }
    
    cout<<"Case #"<<t<<": "<<ret + best[nr[1]][nr[2]][nr[3]]<<"\n";
    
  }
  return 0;
}
