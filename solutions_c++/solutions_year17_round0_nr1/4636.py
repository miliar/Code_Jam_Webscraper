#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

char s[1001];

void flip(char& c)
{
   if(c == '-')
      c = '+';
   else
      c = '-';
}

int main()
{
   int T;
   scanf("%d", &T);
   for(int _i=1; _i<=T; _i++)
   {
      int k;
      scanf("%s%d", s, &k);
      int n = strlen(s);
      int r = 0;
      for(int i=0; i<=n-k; i++)
         if(s[i] == '-') {
            r++;
            for(int j=i+1; j<i+k; j++)
               flip(s[j]);
         }
      bool b = true;
      for(int i=n-k+1; i<n; i++)
         if(s[i] == '-')
            b = false;
      if(!b)
         printf("Case #%d: IMPOSSIBLE\n",_i);
      else
         printf("Case #%d: %d\n",_i, r);
   }
   return 0;
}
