#include <bits/stdc++.h>
#include<fstream>
using namespace std;

void flip(string &s,int st,int end)
{
    int i;
    for(i=st;i<end;i++)
    {
        if(s[i]=='+')
            s[i]='-';
        else
            s[i]='+';
    }
}

int func(string s,int k)
{
    int i,ans=0;

    for(i=0;i<=s.length()-k;i++)
    {
        if(s[i]=='-')
        {
            flip(s,i,i+k);
            ans++;
        }
    }
    if(find(s.begin(),s.end(),'+')!=s.end() && find(s.begin(),s.end(),'-')!=s.end())
        return -1;
    return ans;
}

int main()
{
    ofstream myfile ("example.txt");
    ifstream ip ("A-large.txt");
    if (ip.is_open())
    {
      int i=1;
      int t;
      ip>>t;
      if (myfile.is_open())
      {
        while(t--)
        {
            string s;
            ip>>s;
            int k;
            ip>>k;
            int ans=func(s,k);
            myfile<<"Case #"<<i<<": ";
            //cout<<s<<" ";
            if(ans==-1)
            {
                myfile<<"IMPOSSIBLE"<<endl;
                //cout<<"IMPOSSIBLE"<<endl;
            }
            else{
                myfile<<ans<<endl;
                //cout<<ans<<endl;
            }
            i++;
        }
      }
    }
    return 0;
}
