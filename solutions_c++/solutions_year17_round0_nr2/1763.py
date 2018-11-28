#include<bits/stdc++.h>

using namespace std;

int main(void)
{
    freopen("C:\\Users\\user\\Desktop\\input.in","r",stdin);
freopen("C:\\Users\\user\\Desktop\\output.txt","w",stdout);
    int t;
    cin>>t;

    for(int i=1;i<=t;i++)
    {
        int ok=1;
        string s;
        cin>>s;
        //cout<<s<<endl;
        string ans="";
        int len=s.length();
        int same=0;;
        for(int i=0;i<len-1;i++)
        {

            if(s[i]>s[i+1])
            {
                for(int j=0;j<same;j++)
                ans=ans+s[j];
                char c=s[same]-1;
                if(same!=0||c!='0')
                ans=ans+c;
                for(int j=same+1;j<len;j++)
                ans=ans+'9';
                ok=0;
                break;
            }
        if(s[i]!=s[i+1])
            same=i+1;

        }
        if(ok)
            ans=s;
        cout<<"case #"<<i<<": "<<ans<<endl;
    }
}
