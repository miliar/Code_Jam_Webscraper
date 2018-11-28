#include<bits/stdc++.h>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("out114.txt");
int main()
{
    int t;
    fin>>t;
    for(int x=1;x<=t;x++)
    {
        string s;
        fin>>s;
        int l=s.length();
        int idx=-1;
        for(int i=0;i<l-1;i++)
        {
            if(s[i]>s[i+1])
            {
                idx=i;
                break;
            }
        }
        fout<<"Case #"<<x<<": ";
        if(idx==-1)
            fout<<s<<endl;
        else{
                int j=idx;
            while(j>0)
            {
                if(s[j]==s[j-1])
                {
                    j--;
                }
                else
                    break;
            }
            string ans="",ans1="";
            int f=0;
            for(int i=0;i<l;i++)
            {
                if(i==j)
                {
                    int c=s[i]-1;
                    ans=ans+(char)c;
                    f=1;
                }
                else if(f==1)
                {
                    ans=ans+'9';
                }
                else
                {
                    ans=ans+s[i];
                }
            }
            int f1=0;
            for(int i=0;i<ans.length();i++)
            {
                if(ans[i]!='0')
                    f1=1;
                if(f1)
                {
                    ans1=ans1+ans[i];
                }
            }
            fout<<ans1<<endl;
        }
    }
    return 0;
}
