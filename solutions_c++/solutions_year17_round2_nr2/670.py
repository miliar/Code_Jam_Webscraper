#include<bits/stdc++.h>
using namespace std;

const int maxm = 1111;
int T;
int R,O,Y,G,B,V;
int m;
struct node
{
  string str;
  int num;
}g[3];

int cmp(node a,node b)
{
  return a.num>b.num;
}


int main()
{
  freopen("B-small-attempt0.in","r",stdin);
  freopen("B-small-attempt0.out","w",stdout);
  cin>>T;
  for(int it=1;it<=T;it++)
  {
    cin>>m;
    cin>>g[0].num>>O>>g[1].num>>G>>g[2].num>>V;
    g[0].str="R";g[1].str="Y";g[2].str="B";
    sort(g,g+3,cmp);    

//    for(int i=0;i<3;i++)cout<<g[i].num<<" "<<g[i].str<<endl;
  
    if(g[0].num>g[1].num+g[2].num)
    {
      printf("Case #%d: IMPOSSIBLE\n",it);
      continue;
    }
    else
    {
      printf("Case #%d: ",it);
      int len0 = g[0].num;
      int len1 = g[1].num;
      int len2 = g[2].num;
      int out = len1+len2-len0;
      for(int i=1;i<=len0;i++)
      {
        if(out)
        {
          out--;
          cout<<g[2].str;
        }
        if(len1)
        {
          cout<<g[1].str;
          len1--;
        
          if(out)
          {
            out--;
            cout<<g[2].str;
          }
          cout<<g[0].str;
        }
        else
        {
          cout<<g[2].str;
          cout<<g[0].str;
        }
      }
      cout<<endl;
    }
  }
  return 0;
}
