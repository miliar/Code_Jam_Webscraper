#include <bits/stdc++.h>
#include<string.h>

using namespace std;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int tt,len,i,j,T,K,count,qq,l;
  char S[1001];
  cin >> T;
  for (int qq = 1; qq <= T; qq++)
  {
       cin >> S >> K;
      // cout << S << " and " << K << endl;
       i=0;
       j=i+K;
       l=strlen(S);
       count=0;
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
               count++;
           }
       }
       printf("Case #%d: ", qq);
        //cout << "String is " << S << endl;
        int f=1;
       for(int i1=i;i1<=l-1;i1++)
       {
           if(S[i1]=='-')
           {
               f=0;
               break;
           }
       }
        if(f==1)
        cout << count << endl;
        else
        puts("IMPOSSIBLE");

  }

  return 0;
}


