#include<iostream>
#include<string>
using namespace std;

int main()
{
    int t;
    cin>>t;

    for(int T=1; T<=t; T++)
    {
      string a;
      cin>>a;
      int k,n;
      cin>>k;
      n=a.size();
      int flips=0;
      for(int i=0; i<=n-k; i++)
      {  if(a[i]=='-')
        {
          for(int j=i; j<i+k; j++)
          {
             if(a[j]=='+') a[j]='-';
             else a[j]='+';
          } ++flips;
        }
      }
      bool possible=1;
      for(int i=n-1; i>=n-k; i--)
      {
          if(a[i]=='-') {possible=0; break;}
      }

      if(possible==0) cout<<"Case #"<<T<<": "<<"IMPOSSIBLE"<<endl;
        else  cout<<"Case #"<<T<<": "<<flips<<endl;
    }

    return 0;
}

