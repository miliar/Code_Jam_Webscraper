#include<bits/stdc++.h>
using namespace std;
int main()
{
    ofstream outfile;
    ifstream infile;
    infile.open ("C:\\Users\\ABHISHEK TIWARI\\Desktop\\atom\\code jam\\B-small-attempt2.in");
    outfile.open ("C:\\Users\\ABHISHEK TIWARI\\Desktop\\atom\\code jam\\outputsmall_2.txt");
    int t;
    infile>>t;
    for(int i=1;i<=t;i++)
    {
        string s,w;
        int flag=0;
        infile>>s;
        if(s.length()==1)
        {
            outfile<<"Case #"<<i<<": "<<s<<endl;
        }
        else
        {
            int temp=0;
            int c=0;
            for(int k=0;k<s.length()-1;k++)
            {
                if(s[k]<=s[k+1])
                {
                    c++;
                }
            }
            if(c==s.length()-1)
                outfile<<"Case #"<<i<<": "<<s<<endl;
            else
            {
                for(int j=1;j<s.length();j++)
                {
                    if(s[0]=='1' && s[0]>=s[1])
                    {
                        flag=1;
                        break;
                    }
                    else if(s[j]<=s[j-1])
                    {
                        s[j-1]--;
                        for(int z=j;z<s.length();z++)
                        {
                            s[z]='9';
                        }
                        break;
                    }
                }
                if(flag==1)
                {
                    for(int k=0;k<s.length()-1;k++)
                    {
                        w+="9";
                    }
                    outfile<<"Case #"<<i<<": "<<w<<endl;
                }
                else
                    outfile<<"Case #"<<i<<": "<<s<<endl;
            }
        }
    }
    infile.close();
    outfile.close();
    return 0;
}
