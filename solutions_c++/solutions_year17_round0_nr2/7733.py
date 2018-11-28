#include<bits/stdc++.h>

using namespace std;

const int Maxn=25;

string s,dp[Maxn][16][2];


int main()
{
    int t;
    cin>>t;
    for(int o=0;o<t;o++)
    {
        cin>>s;
        //cerr<<s<<endl;
        //cerr<<endl;
        for(int i=0;i<s.length();i++)
            for(int j=0;j<10;j++)
                dp[i][j][0]=dp[i][j][1]="0";
        for(int i=0;i<s[0]-'0';i++)
            dp[0][i][0]=char(i+'0');
        dp[0][s[0]-'0'][1]=s[0];
        //cerr<<"******"<<s<<" "<<s[0]<<" "<<s[0]-'0'<<" "<<dp[0][s[0]-'0'][1]<<endl;
        for(int i=0;i<10;i++)
        {
            if(dp[0][i][0].length()==0)
                dp[0][i][0]="0";
            if(dp[0][i][1].length()==0)
                dp[0][i][1]="0";
        }
       // cerr<<s<<endl;
        for(int i=1;i<s.length();i++)
        {
            //cerr<<s[i];
            for(int j=0;j<10;j++)
            {
                for(int k=0;k<=j;k++)
                    if(dp[i-1][k][0]!="0"&&dp[i-1][j][0]!="")
                    {
                        string q=dp[i-1][k][0];
                        q+=char(j+'0');
                        dp[i][j][0]=max(dp[i][j][0],q);
                    }
                if(j<s[i]-'0'&&j>=s[i-1]-'0'&&dp[i-1][s[i-1]-'0'][1]!="0"&&dp[i-1][s[i-1]-'0'][1]!="")
                {
                    string q=dp[i-1][s[i-1]-'0'][1];
                    q+=char(j+'0');
                    dp[i][j][0]=max(dp[i][j][0],q);
                }
            }
            if(s[i]>=s[i-1])
                dp[i][s[i]-'0'][1]=dp[i-1][s[i-1]-'0'][1]+s[i];
        }
        string ans="";
        for(int i=0;i<10;i++)
        {
       //     cerr<<"!!!"<<dp[s.length()-1][i][0]<<" "<<dp[s.length()-1][i][1]<<" "<<max(dp[s.length()-1][i][0],dp[s.length()-1][i][1])<<" "<<max(ans,max(dp[s.length()-1][i][0],dp[s.length()-1][i][1]))
//<<endl;
            ans=max(ans,max(dp[s.length()-1][i][0],dp[s.length()-1][i][1]));
        }
        for(int i=0;i<s.length();cerr<<endl,i++)
        {
            for(int j=0;j<10;j++)
                cerr<<dp[i][j][0]<<" ";
             cerr<<endl;
             for(int j=0;j<10;j++)
                cerr<<dp[i][j][1]<<" ";
        }
        bool flag=0;
        string q=ans;
        ans="";
        for(int i=0;i<q.length();i++)
            if(q[i]!='0'||(q[i]=='0'&&flag))
            {
                ans+=q[i];
                flag=1;
            }
        if(ans.size()<s.length())
        {
            ans="";
            for(int i=0;i<s.length()-1;i++)
                ans+="9";
        
        }
        cout<<"Case #"<<o+1<<": "<<ans<<endl;
    }

}
