#include <bits/stdc++.h>
using namespace std;
FILE *fi;
void kiir(string s,int g)
{fi=fopen("ez.txt","at");

    fprintf(fi,"Case #%d: ",g+1);
    bool b=false;
    for (int i=0;i<s.length();i++)
    {
        if (s[i]!='0') b=true;
        if (b) fprintf(fi,"%c",s[i]);
    }
    fprintf(fi,"\n");
}
int jat(int g)
{

   string s;
   cin>>s;
   int si=s.length();
   for (int i=1;i<si;i++)
   {
       if (s[i]<s[i-1])
       {

           {
              s[i-1]--;
              int o;
              for ( o=i-1;o>0;o--)
              {
                  if (s[o]<s[o-1]) s[o-1]--;
                  else break;
              }
              for (int j=o+1;j<si;j++) s[j]='9';
              kiir(s,g);
              return 0;
           }


       }
   }
   kiir(s,g);
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
