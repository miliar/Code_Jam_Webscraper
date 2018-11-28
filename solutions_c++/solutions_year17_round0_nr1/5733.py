#include <bits/stdc++.h>
#include<string.h>

using namespace std;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int tt,i,T,K,c,l;
  char S[1001];
  cin >> T;
  for (int tt = 1; tt <= T; tt++)
  {
       cin >> S >> K;



       l=strlen(S);
       c=0;
       for(i=0;i<=l-K;i++)
       {
           if(S[i]=='-')
           {
               for(int i1=i;i1<i+K;i1++)
               {
                   if(S[i1]=='-')
                   S[i1]='+';
                   else
                   S[i1]='-';
               }
               c++;
           }
       }
       printf("Case #%d: ", tt);

        int flag=1;
       for(int i1=i;i1<=l-1;i1++)
       {
           if(S[i1]=='-')
           {
               flag=0;
               break;
           }
       }
        if(flag==1)
        cout << c << endl;
        else
        puts("IMPOSSIBLE");

  }

  return 0;
}


