#include <iostream>

using namespace std;

int main()
{
  int t, r, c, flag =0, j;
  char s;
  char cake[25][25];
  cin>>t;
  for(int a0= 1; a0<=t;a0++)
  {
    cin>>r>>c;
    for(int i = 0;i <r;i++)
    {
      for(int j = 0; j<c;j++)
      {
        cin>>cake[i][j];
      }
    }
    // cout<<r<<" "<<c<<endl;
    // for(int i = 0;i <r;i++)
    // {
    //   for(int j = 0; j<c;j++)
    //   {
    //     cout<<cake[i][j]<<" ";
    //   }
    //   cout<<endl;
    // }
    for(int i = 0; i<r;i++)
    {
      flag = 0;
      for(int j = 0; j< c;j++)
      {
        if(cake[i][j]!='?')
        {
          flag = 1;
          //cout<<"here "<<flag<<" "<<i<<" "<<j<<endl;
          s = cake[i][j];
          int k = j+1;
          while(cake[i][k] =='?' && k<c)
          {
            cake[i][k] = s;
            k++;
          }
          int k1 = j-1;
          while(cake[i][k1] =='?' && k1>=0)
          {
            cake[i][k1] = s;
            k1--;
          }
        }
      }
      if(flag == 0)
      {
        int f =0;
        //cout<<"i = "<<i<<endl;
        if(i == 0)
        {
          for(int k2 = i+1; k2<r;k2++)
          {
            for(int k3 = 0; k3<c;k3++)
            {
              if(cake[k2][k3]!='?')
              {
                f = 1;
                for(int j = 0;j<c;j++)
                {
                  cake[i][j] = cake[k2][j];
                }
                i--;
                break;

              }
              if(f) break;
            }
            if(f)break;
          }
        }
        else
        {
          for(int j = 0;j<c;j++)
          {
            cake[i][j] = cake[i-1][j];
          }
        }
      }
    }

    cout<<"Case #"<<a0<<":\n";
    for(int i = 0; i<r;i++)
    {
      for(int j = 0; j< c;j++)
      {
        cout<<cake[i][j];
      }
      cout<<endl;
    }

  }
}
