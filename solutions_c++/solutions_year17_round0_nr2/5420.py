#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int nmax = 1010; const LL mod = 1000000007;

int N,c[30];
LL X,ans,aux,p;
bool ok;

inline void Solve(int caz){
   int i,j,nr=0;
   cin >> X;
   if(X < 10){
      cout << "Case #"<<caz<<": "<<X<<'\n';
      return;
   }

   aux = X;
   c[0] = 0;
   while(X){
      c[++c[0]] = X%10;
      ++nr;
      X/=10;
   }
   X = aux;
   for(i = 1,p = 9; i+1 < nr; ++i)
      p = (p*10)+9;

   for(i = 1; i <= c[0]/2; ++i)
      swap(c[i],c[c[0]-i+1]);

   for(i = 1; i < c[0]; ++i)
      if(c[i] > c[i+1]){
         j=i-1;
         while(c[j]==c[i])--j;
         i=j+1;
         c[i]--;
         for(j = i+1; j <= c[0]; ++j)
            c[j] = 9;
         for(j = i-1; j > 0; --j)
            c[j] = min(c[j],c[j+1]);

         break;
      }
//      for(i = 1; i <= c[0]; ++i)
//         cout << c[i];
//      cout << '\n';
         cout << "Case #"<<caz<<": ";
         LL qq = 0;
         j=1;
         while(j<=c[0] && !c[j])++j;
         for(i = j; i <= c[0]; ++i)
            qq=qq*10+c[i];
      cout << max(qq,p) << ' ';
//         for(i = 1; i <= X; ++i){
//   c[0] = 0;
//   aux=i;
//   while(i){
//      c[++c[0]] = i%10;
//      i/=10;
//   }
//   i=aux;
//      for(j = 1; j <= c[0]/2; ++j)
//      swap(c[j],c[c[0]-j+1]);
//
//      bool tr = false;
//         for(j = 1; j < c[0]; ++j)
//            if(c[j] > c[j+1]) tr = true;
//         if(!tr){
//               qq = 0;
//            for(j = 1; j <= c[0]; ++j)
//               qq = qq*10+c[j];
//         }
//         }
//         LL w = 0;
//         j=1;
//         while(j<=c[0] && !c[j])++j;
//
//         for(i = j; i <= c[0]; ++i)
//            w = (w*10)+c[i];
//      cout << qq <<'\n';
   cout << '\n';
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
