#include <bits/stdc++.h>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.sol");
int main()
{
    int t;
    string s,ans;
    fin>>t;
    for(int i=0;i<t;i++)
    {
        fin>>s;
        ans=("");
        for(int j=0;j<s.size()-1;j++)
        {
            if(s[j+1]<s[j])
            {
                int k=j;
                while(k>0&&s[k]==s[k-1])k--;
                if(k==0&&s[0]=='1')for(int l=0;l<s.size()-1;l++)ans+="9";
                else
                {
                    for(int l=0;l<k;l++)ans+=s[l];
                    ans+=s[k]-1;
                    for(int l=k+1;l<s.size();l++)ans+="9";
                }
                break;
            }
        }
        fout<<"Case #"<<i+1<<": ";
        if(ans=="")ans=s;
        fout<<ans<<endl;
    }
}
