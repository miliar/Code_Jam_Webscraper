#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int main()
{
   int T;
   scanf("%d", &T);
   for(int _i=1; _i<=T; _i++)
   {
      char s[19];
      scanf("%s", s);
      int n = strlen(s);

      for(int i=0; i<n-1; i++)
         if(s[i] > s[i+1]) {
            s[i]--;
            for(int j=i+1; j<n; j++)
               s[j] = '9';
            for(int j=i-1; j>=0; j--)
               if(s[j] > s[j+1]) {
                  s[j]--;
                  s[j+1] = '9';
               }
            break;
         }
      if(s[0] == '0') {
         for(int i=0; i<n-1; i++)
            s[i] = '9';
         s[n-1] = '\0';
      }

      printf("Case #%d: %s\n",_i, s);
   }
   return 0;
}
