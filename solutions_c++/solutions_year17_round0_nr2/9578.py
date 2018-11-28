#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t;
    cin>>t;
    for (int  T = 0; T < t; T++) {
      std::vector<int> v;
      long long int n;
      cin>>n;
      long long temp=n;
      while(n>0)
      {
        v.push_back(n%10);
        n=n/10;
      }
      reverse(v.begin(),v.end());
      int a[10][18];
      long long int b[10][18];
      for(int i=0;i<v.size();i++)
      {
        for(int j=0;j<10;j++)
        {
          if(j==0)
          {
            a[j][i]=v[i];

          }
          else
          {
            if (a[j-1][i]==0) {
              a[j][i]=9;
            }
            else
          {
            a[j][i]=a[j-1][i]-1;
          }
          }
          b[j][i]=a[j][i]*pow(10,v.size()-1-i);
        }
      }
      for(int i=1;i<v.size();i++)
      {
        for(int j=0;j<10;j++)
        {
          long long min=b[0][i-1];
          for(int k=0;k<=j;k++)
          {
            if(min>b[k][i-1]&&((v[i]>=j&&k<=v[i])))
            {min=b[k][i-1];}
            else if(min>b[k][i-1]-pow(10,v.size()-i)&&(v[i]<j)&&b[k][i-1]-pow(10,v.size()-i)>=0)
            {
              min=b[k][i-1]-pow(10,v.size()-i);
            }
          }
          b[j][i]=b[j][i]+min;
        }
      }
      long long min=b[0][v.size()-1];
      for(int i=0;i<10;i++)
      {
        //cout<<b[i][v.size()-1]<<",";
        if(min>b[i][v.size()-1])
        {
          min=b[i][v.size()-1];
        }

      }

      cout<<"Case #"<<T+1<<": "<<temp-min<<endl;

      v.clear();
    }
}
