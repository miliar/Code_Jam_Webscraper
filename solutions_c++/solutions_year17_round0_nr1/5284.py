#include <bits/stdc++.h>
using namespace std;
FILE *fi;
int jat(int g)
{
fi=fopen("ez.txt","at");
    int h;
    string s;
  cin>>s>>h;
  int ki=0,si=s.length();
  for (int i=0;i<si;i++)
  {
      if (i>si-h && s[i]=='-')
      {
          fprintf(fi,"Case #%d: IMPOSSIBLE\n",g+1);
          return 0;
      }
      if (s[i]=='-')
      {
          for (int j=i;j<i+h;j++)
          {
              if (s[j]=='-') s[j]='+';
              else s[j]='-';
          }
          ki++;
      }

  }fprintf(fi,"Case #%d: %d\n",g+1,ki);
  return 0;
}
int main()
{
fi=fopen("ez.txt","wt");
fclose(fi);
int n;
scanf("%d",&n);
for (int i=0;i<n;i++)
{
    jat(i);
}
        return 0;
}
