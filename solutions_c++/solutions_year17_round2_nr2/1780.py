#include<bits/stdc++.h>
using namespace std;
char cha[105][1005];
int main()
{
  int t,i,bn[1005],an[1005]={0};

  cin>>t;
  for(i=0;i<t;i++)
  {
      int n,j,a[8]={0},f=0,x;
      cin>>n;
      bn[i]=n;
      char c[1006],co[6]={'R','O','Y','G','B','V'};
      for(j=0;j<1005;j++)
      {
          c[j]='Z';
      }
      for(j=0;j<6;j++)
      {
          cin>>a[j];
          if(a[j]!=0&&f==0)
          {
              f=1;
              x=j;
          }
      }
      c[0]=co[x];
      a[x]--;
      for(j=1;j<n;j++)
      {
          if(c[j-1]=='R')
          {
             if(a[3])
             {
               a[3]--;
               c[j]=co[3];
             }
             else if(a[2]&&a[2]>=a[4])
             {
                 a[2]--;
                 c[j]=co[2];
             }
             else if(a[4])
             {
                 a[4]--;
                 c[j]=co[4];
             }
          }
          if(c[j-1]=='B')
          {
             if(a[1])
             {
               a[1]--;
               c[j]=co[1];
             }
             else if(a[0]&&a[0]>a[2])
             {
                 a[0]--;
                 c[j]=co[0];
             }
             else if(a[2])
             {
                 a[2]--;
                 c[j]=co[2];
             }
          }

          if(c[j-1]=='Y')
          {
             if(a[5])
             {
               a[5]--;
               c[j]=co[5];
             }
             else if(a[4]&&a[4]>a[0])
             {
                 a[4]--;
                 c[j]=co[4];
             }
             else if(a[0])
             {
                 a[0]--;
                 c[j]=co[0];
             }
          }

          if(c[j-1]=='O')
          {
              if(a[4])
              {
                  a[4]--;
                  c[j]=co[4];
              }
          }

          if(c[j-1]=='V')
          {
              if(a[2])
              {
                  a[2]--;
                  c[j]=co[2];
              }
          }

          if(c[j-1]=='G')
          {
              if(a[0])
              {
                  a[0]--;
                  c[j]=co[0];
              }
          }
          if(c[j]=='Z')
          {
              an[i]=1;
          }
      }
      int f1=1;
      if(c[n-1]=='R')
      {
        if(c[0]=='Y'||c[0]=='G'||c[0]=='B')
        {
            f1=0;
        }
      }
      if(c[n-1]=='B')
      {
        if(c[0]=='Y'||c[0]=='R'||c[0]=='O')
        {
            f1=0;
        }
      }
      if(c[n-1]=='Y')
      {
        if(c[0]=='B'||c[0]=='R'||c[0]=='V')
        {
            f1=0;
        }
      }
      if(c[n-1]=='O')
      {
        if(c[0]=='B')
        {
            f1=0;
        }
      }

      if(c[n-1]=='V')
      {
        if(c[0]=='Y')
        {
            f1=0;
        }
      }

      if(c[n-1]=='G')
      {
        if(c[0]=='R')
        {
            f1=0;
        }
      }
      if(f1==1)
      {
          an[i]=1;
      }
     for(j=0;j<n;j++)
     {
         cha[i][j]=c[j];
     }

  }
  for(i=0;i<t;i++)
  {
      cout<<"Case #"<<i+1<<": ";
      if(an[i]==0)
      {
          for(int m=0;m<bn[i];m++)
          {
              cout<<cha[i][m];
          }
      }
      else
      {
          cout<<"IMPOSSIBLE";
      }
      cout<<" \n";
  }
  return 0;
}
