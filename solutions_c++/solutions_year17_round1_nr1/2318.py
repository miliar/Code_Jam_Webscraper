#include <iostream>

using namespace std;

int zero(){
  return 0;
}
int one(){
  return 1;
}
int main()
{
  int test, row, col, flag =0, j;
  char temp;
  char cake[25][25];
  cin>>test;
  zero();
  for(int a0= 1; a0<=test;a0++)
  {
    cin>>row>>col;
    for(int i = 0;i <row;i++)
    {
      for(int j = 0; j<col;j++)
      {
        cin>>cake[i][j];
      }
    }
    one();
    for(int i = 0; i<row;i++)
    {
      flag = 0;
      for(int j = 0; j< col;j++)
      {
        if(cake[i][j]!='?')
        {
          flag = 1;
          //cout<<"here "<<flag<<" "<<i<<" "<<j<<endl;
          temp = cake[i][j];
          int k = j+1;
          while(cake[i][k] =='?' && k<col)
          {
            cake[i][k] = temp;
            k++;
          }
          int k1 = j-1;
          while(cake[i][k1] =='?' && k1>=0)
          {
            cake[i][k1] = temp;
            k1--;
          }
        }
      }
      zero();
      if(flag == 0)
      {
        int f =0;
        //cout<<"i = "<<i<<endl;
        if(i == 0)
        {
          for(int k2 = i+1; k2<row;k2++)
          {
            for(int k3 = 0; k3<col;k3++)
            {
              if(cake[k2][k3]!='?')
              {
                f = 1;
                for(int j = 0;j<col;j++)
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
          for(int j = 0;j<col;j++)
          {
            cake[i][j] = cake[i-1][j];
          }
        }
        zero();
      }
    }
    one();
    cout<<"Case #"<<a0<<":\n";
    for(int i = 0; i<row;i++)
    {
      for(int j = 0; j< col;j++)
      {
        cout<<cake[i][j];
      }
      cout<<endl;
    }
    one();
  }
}
