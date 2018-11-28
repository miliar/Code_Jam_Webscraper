#include<iostream>
#include<string>

using namespace std;

int solve(string &S, int K);
void flip(char &c);

int main() {
  int T; cin>>T; cerr<<"Total case: "<<T<<endl;
  for(int i=0;i<T;++i) {
    string S; int K;
    cin>>S>>K;
    cerr << "Case #" << i+1 << ": S:"<< S << " K:" << K << endl;
    int ans = solve(S,K);
    if(ans<0) cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
    else cout << "Case #" << i+1 << ": " << ans << endl;
  }
  return 0;
}

int solve(string &S, const int K) {
  int fp=0;
  int end = S.size();
  int ans=0;
  while(fp+K-1<end) {
    cerr << "fp:" << fp << endl;
    if(S[fp]=='+') { fp++; continue; }
    for(int i=fp;i<fp+K;++i) flip(S[i]);
    ans++;
    cerr << S << endl;
    fp++;
  }
  for(int i=fp;i<end;++i) if(S[i]=='-') return -1;
  return ans;
}

void flip(char &c) {
  if(c=='-') c='+';
  else if(c=='+') c='-';
}

