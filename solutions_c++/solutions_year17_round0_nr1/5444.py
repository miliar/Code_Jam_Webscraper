#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int nmax = 1010; const LL mod = 1000000007;

int N,T,K,ans,c[nmax];
bool a[nmax];
char ch[nmax];

inline void Solve(int caz){
   int i,j,nr,q,rest,dr;
   cin >> ch >> K;
   N = strlen(ch);
   for(i = 0; i < N; ++i)
      if(ch[i] == '+') a[i+1] = true;
      else a[i+1] = false;
   a[N+1] = true;

   for(i = 1; i <= N && ans >= 0; ++i)
      if(!a[i] && a[i+1]){
         nr = 1 , j = i-1;
         while(j >= 1 && !a[j])++nr,--j;
         ans+=(nr/K);
         rest = nr%K;
         ++j , nr = (nr/K)*K;
         while(nr>0)a[j] = true,--nr,++j;

         if(rest){
            rest = K-rest;
            c[0] = 0;
            dr = i+rest;
            for(j = i+1; j <= dr; ++j)
               if((a[j]^1) == a[j-1])c[++c[0]] = j+K-1,++ans;

            for(j = 1; j <= c[0]; ++j)
               if(c[j] > N)ans = -1;
            for(j = i+1; j <= dr; ++j)
               a[j] = false;
            q = c[0];
            for(j = c[q],nr=0; j > dr; --j){
               if(q>0&&j == c[q])++nr,--q;
               if(nr%2)a[j]^=1;
            }
         }
      }
      if(ans < 0)
         cout << "Case #"<<caz<<": IMPOSSIBLE\n";
      else
         cout << "Case #"<<caz<<": "<<ans<<'\n';;
//   for(i = 1; i <= N; ++i)
//      cout << a[i]<<' ';
//   cout << '\n';
}

inline void Reset(){
   ans = 0;
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
