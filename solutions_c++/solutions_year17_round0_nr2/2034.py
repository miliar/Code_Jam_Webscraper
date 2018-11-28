#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int t;
    cin>>t;
    for(int o=1;o<=t;o++)
    {
       long long n;
       cin>>n;
       long long cn=n;
       vector<int> num;
       while(n)
       {
          num.push_back(n%10);
          n/=10;
       }
       reverse(num.begin(),num.end());
       vector<int> pr(num.size());
       pr[0]=num[0];
       int pos=-1;
       for(int i=1;i<num.size();i++)
       {
          if(num[i]<num[i-1]&&pos<0)
          {
             pos=i;
          }
          pr[i]=max(pr[i-1],num[i]);
       }
       if(pos<0)
       {
          cout<<"Case #"<<o<<": "<<cn<<'\n';
          continue;
       }
       int st=0;
       int d=-1;
       for(int i=pos-1;i>=0;i--)
       {
          if(i==0||num[i]>num[i-1])
          {
             d=i;
             num[i]--;
             break;
          }
       }
       for(int i=d+1;i<num.size();i++)
       {
          num[i]=9;
       }
       if(num[0]==0)
       {
         st=1;
       }
       cout<<"Case #"<<o<<": ";
       for(int i=st;i<num.size();i++)
       {
          cout<<num[i];
       }
       cout<<'\n';
    }
    return 0;
}
