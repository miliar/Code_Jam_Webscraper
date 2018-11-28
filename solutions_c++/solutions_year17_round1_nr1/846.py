#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
string s[30];
int main()
{
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   int T;
   cin >> T;

   for (int cas  = 1 ;  cas <= T ;cas++)
   {
       int N,C;
       cin >> N >> C;
       for (int i =  1; i<=N; i++)
            cin >> s[i];
       for (int i = 1; i<=N; i++)
       {
           for (int j = 0; j<C ; j++)
            {
                if (s[i][j]=='?'){
                int b = j;
                while (b<C&&s[i][b]=='?')b++;
                if (b<C&&s[i][b]!='?') s[i][j] = s[i][b];
                b = j;
                while (b>=0&&s[i][b]=='?') b--;
                if (b>=0&&s[i][b]!='?') s[i][j] = s[i][b];
                }
            }
       }
       for (int j = 0; j<C;j++)
        for (int i = 0; i<=N; i++)
       {
                if (s[i][j]=='?'){
                int b = i;
                while (b<=N&&s[b][j]=='?')b++;
                if (b<=N&&s[b][j]!='?') s[i][j] = s[b][j];
                b = i;
                while (b>=1&&s[b][j]=='?') b--;
                if (b>=1&&s[b][j]!='?') s[i][j] = s[b][j];
                }
       }
       printf("Case #%d:\n",cas);
       for (int i = 1; i<=N; i++)
        cout << s[i]<<endl;
   }
}
