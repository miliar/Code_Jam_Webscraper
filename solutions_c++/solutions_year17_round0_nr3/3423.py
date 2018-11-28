#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

struct stall {
  int L, R, m, M;
};
stall *S=nullptr;

struct stall_compare {
    bool operator() (const int& lhs, const int& rhs) const{
        if (S[lhs].m != S[rhs].m) return S[lhs].m > S[rhs].m;
        if (S[lhs].M != S[rhs].M) return S[lhs].M > S[rhs].M;
        return lhs < rhs;
    }
};

int main(int argc, char **argv) {
  _;
  int T;
  cin >> T;
  if (argc!=3) {
    cout << "Bad argc" << endl;
    return 0;
  }
  int base = stoi(argv[1]);
  int amount = stoi(argv[2]);
  int maxi=0, mini=0;

  for (int t=1; t<=T; t++) {
    int N, K;
    cin >> N >> K;
    if (t < base || t >= base+amount ) continue;
    if(S!=nullptr) {
      delete[] S;
    }
    S = new stall[N];
    set<int, stall_compare> pq;

    for (int i=0; i<N; i++) {
      stall s;
      s.L = i;
      s.R = N-i-1;
      s.m = min(s.L, s.R);
      s.M = max(s.L, s.R);
      S[i] = s;
      pq.insert(i);
    }

    for (int i=0;i<K; i++) {
      int k = *pq.begin();
      //cout << k << endl;
      maxi = S[k].M;
      mini = S[k].m;
      pq.erase(pq.begin());
      S[k].L=S[k].R=-1;

      for (int j=k+1; j<N && S[j].L!=-1; j++)
        pq.erase(j);
      for (int j=k-1; j>=0 && S[j].R!=-1; j--)
        pq.erase(j);

      for (int j=k+1; j<N && S[j].L!=-1; j++) {
        S[j].L = S[j-1].L+1;
        if (S[j].L >= S[j].R) {
          S[j].m = S[j].R;
          S[j].M = S[j].L;
        } else {
          S[j].m = S[j].L;
          S[j].M = S[j].R;
        }
      }
      for (int j=k-1; j>=0 && S[j].R!=-1; j--) {
        S[j].R = S[j+1].R+1;
        if (S[j].R >= S[j].L) {
          S[j].m = S[j].L;
          S[j].M = S[j].R;
        } else {
          S[j].m = S[j].R;
          S[j].M = S[j].L;
        }
      }

      for (int j=k+1; j<N && S[j].L!=-1; j++)
        pq.insert(j);
      for (int j=k-1; j>=0 && S[j].R!=-1; j--)
        pq.insert(j);

    }

    cout << "Case #" << t << ": " << maxi << " " << mini << endl;
  }
}