#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int nmax = 1010; const LL mod = 1000000007;

int N,K;

struct el{
 int st,dr;
 bool operator <(const el& A) const
 {
    if(min(st,dr) == min(A.st,A.dr)){
      if(max(st,dr) == max(A.st,A.dr))
         return (st > A.st);
      return (max(st,dr) < max(A.st,A.dr));
    }
    return (min(st,dr) < min(A.st,A.dr));
 }
};

priority_queue<el>Q;

inline void Solve(int caz){
   int i,j,nr=0;
   cin >> N >> K;
   el w,r;
      w.st = w.dr = N/2;
      if(N%2 == 0)
         w.st--;
   Q.push(w);

         cout << "Case #"<<caz<<": ";
     --K;
     while(K--){
         w = Q.top();
         Q.pop();
         r.st = r.dr = (w.st)/2;
         if(w.st%2 == 0)
            r.st--;
         Q.push(r);
         r.st = r.dr = (w.dr)/2;
         if(w.dr%2 == 0)
            r.st--;
         Q.push(r);
     }
     w = Q.top();
     cout << max(w.st,w.dr) << ' ' << min(w.st,w.dr) << '\n';
}

inline void Reset(){
   while(!Q.empty())Q.pop();
}

int main(void){
   int tests=1,i=1;
//   freopen("txt.in","r",stdin);
//   freopen("txt.out","w",stdout);
   ios::sync_with_stdio(false);
   cin >> tests;
  while(tests--){
      Solve(i);
      Reset();
      ++i;
  }
    return 0;
}
