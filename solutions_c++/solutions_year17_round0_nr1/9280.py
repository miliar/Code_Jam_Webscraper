#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        string s;
        int k;
        cin>>s>>k;
        int n;
        bool flag=false;
        int ans=0;
        n=s.length();
        string res="";

        for(int i=0;i<n;i++)
            res+="+";

        if(res==s)
            flag=true;
        else
        {
            for(int i=0;i<n;i++)
        {
            string temp="";
            temp+=s[i];
            if(temp=="-" && (i+k-1) < n)
            {
                for(int j=i;j<k+i;j++)
                {
                   string temp1="";
                   temp1+=s[j];
                   if(temp1=="-")
                    s.replace(j,1,1,'+');
                    else
                        s.replace(j,1,1,'-');
                }
                //cout<<s<<endl;
                ans++;
                //cout<<ans;
                if(s==res)
                {
                    flag=true;
                    break;
                }
            }
        }
    }

            if(flag==true)
              cout<<"Case #"<<z<<":"<<" "<<ans<<endl;
          else
            cout<<"Case #"<<z<<":"<<" "<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}