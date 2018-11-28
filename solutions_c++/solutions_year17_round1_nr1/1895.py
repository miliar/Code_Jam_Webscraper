#include <iostream>

using namespace std;

int main()
{
  int t;
  cin>>t;
  for (int a=0;a<t;a++)
  {
    int r,c;
    cin>>r>>c;
    char z[30][30];
    
    for (int i=0;i<30;i++)
      for (int j=0;j<30;j++)
        z[i][j]='?';
    for (int b=0;b<r;b++)
      for (int j=0;j<c;j++)
        cin>>z[b][j];
    int s=0;
    for (int i=0;i<r;i++)
      for (int j=0;j<c;j++)
        if (z[i][j]=='?')
          s++;
    
    while (s)
    {
      s=0;
      for (int j=0;j<=c;j++)
      {
        int v=0;
        char p;
        for (int i=0;i<r;i++)
          if (z[i][j]!='?')
          {
            v=1;
            p=z[i][j];
            int m=i-1;
            while (m>=0 &&z[m][j]=='?')
            {
              z[m][j]=p;
              m--;
            }
          }
        if (v==0)
        {
          int g=0,h=0;
          if (j>0)
            for (int i=0;i<r;i++)
              if (z[i][j-1]!='?')
                g=1;
          if (j<c)
            for (int i=0;i<r;i++)
              if (z[i][j+1]!='?')
                h=1;
          if (g)
            for (int i=0;i<r;i++)
            z[i][j]=z[i][j-1];
          else if (h)
            for (int i=0;i<r;i++)
            z[i][j]=z[i][j+1];
        }
        /*  && j==0)
          continue;
        if (v==0)
          for (int i=0;i<r;i++)
            z[i][j]=z[i][j-1];*/
        else
        {
          int m=r-1;
          while (m>=0 &&z[m][j]=='?')
            {
              z[m][j]=p;
              m--;
            }
        }
      }
      
      
    for (int i=0;i<r;i++)
      for (int j=0;j<c;j++)
        if (z[i][j]=='?')
          s++;
    }
    
    cout<<"Case #"<<a+1<<": \n";
    
    for (int i=0;i<r;i++)
    {
      for (int j=0;j<c;j++)
        cout<<z[i][j];
      cout<<endl;
  }
  }
  return 0;
}