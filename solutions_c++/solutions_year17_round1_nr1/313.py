#include <bits/stdc++.h>

using namespace std;
bool test(vector<vector<char> > & v)
{
   for(int i=0;i<v.size();i++)
   {
      for(int j=0;j<v[0].size();j++)
      {
         if(v[i][j]=='?')
         {
            return 1;
         }
      }
   }
   return 0;
}
int main()
{
    ios_base::sync_with_stdio(0);
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int t;
    cin>>t;
    for(int o=1;o<=t;o++)
    {
       int n,m;
       cin>>n>>m;
       vector<vector<char> > v(n,vector<char> (m));
       for(int i=0;i<n;i++)
       {
          for(int j=0;j<m;j++)
          {
             cin>>v[i][j];
          }
       }
          for(int i=0;i<n;i++)
          {
             for(int j=0;j<m;j++)
             {
                if(v[i][j]>='A'&&v[i][j]<='Z')
                {
                   for(int k=i-1;k>=0;k--)
                   {
                      if(v[k][j]=='?')
                      {
                         v[k][j]=v[i][j];
                      }
                      else
                      {
                         break;
                      }
                   }
                   for(int k=i+1;k<n;k++)
                   {
                      if(v[k][j]=='?')
                      {
                         v[k][j]=v[i][j];
                      }
                      else
                      {
                         break;
                      }
                   }
                }
             }
          }
          for(int i=0;i<n;i++)
          {
             for(int j=0;j<m;j++)
             {
                if(v[i][j]>='A'&&v[i][j]<='Z')
                {
                   for(int k=j-1;k>=0;k--)
                   {
                      if(v[i][k]=='?')
                      {
                         v[i][k]=v[i][j];
                      }
                      else
                      {
                         break;
                      }
                   }
                   for(int k=j+1;k<m;k++)
                   {
                      if(v[i][k]=='?')
                      {
                         v[i][k]=v[i][j];
                      }
                      else
                      {
                         break;
                      }
                   }
                }
             }
          }
          cout<<"Case #"<<o<<":\n";
          for(int i=0;i<n;i++)
          {
             for(int j=0;j<m;j++)
             {
                cout<<v[i][j];
             }
             cout<<'\n';
          }
    }
    return 0;
}
