#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

int main()
{
  int t=0;
  cin>>t;
  for(int io=0;io<t;io++)
  {
    int r,c;
    cin>>r>>c;
    vector<string> rows(r,"");
    for(int i=0;i<r;i++)
    {
      cin>>rows[i];
    }
    unordered_set<char> found;
    for(int i=0;i<r;i++)
    {
      for(int j=0;j<c;j++)
      {
        auto f = found.find(rows[i][j]);
        if(rows[i][j] != '?' && f==found.end())
        {
          char temp = rows[i][j];
          int k1 = i,k2 = j;
          int lhs,rhs;
          while(k2>0 && rows[k1][k2-1]=='?')
          {
            rows[k1][--k2] = temp;
          }
          lhs = k2;
          k2 = j;
          while(k2<c-1 && rows[k1][k2+1]=='?')
          {
            rows[k1][++k2] = temp;
          }
          rhs = k2;
          k2 = j;
          bool perfect = 1;
          int z1=k1-1,z2=k2,ul,ll;
          while(z1>=0)
          {
            perfect = 1;
            for(int k=lhs;k<=rhs;k++)
            {
              if(rows[z1][k] != '?')
              {
                perfect = 0;
                break;
              }
            }
            if(!perfect)
              break;
            else
            {
              for(int k=lhs;k<=rhs;k++)
              {
                rows[z1][k] = temp;
              }
            }
            z1--;
          }
          //cout<<endl<<lhs<<rhs<<endl;
          z1 = i+1;
          while(z1<r)
          {
            perfect = 1;
            for(int k=lhs;k<=rhs;k++)
            {
              if(rows[z1][k] != '?')
              {
                perfect = 0;
                break;
              }
            }
            //if(rows[i][j] == 'F')
            //cout<<endl<<i<<j<<z1<<perfect;
            if(!perfect)
              break;
            else
            {
              for(int k=lhs;k<=rhs;k++)
              {
                rows[z1][k] = temp;
              }
            }
            z1++;
          }
          found.insert(temp);
          //i = z1-1;
          //j = rhs;
        }

      }
    }
    cout<<"case "<<"#"<<io+1<<": \n";
    for(int i=0;i<r;i++)
    {
      for(int j=0;j<c;j++)
      {
        cout<<rows[i][j];
      }
      cout<<endl;
    }
  }
  return 0;
}
