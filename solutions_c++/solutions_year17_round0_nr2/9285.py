#include<bits/stdc++.h>
using namespace std;
int main()
{
    ofstream outfile;
    ifstream infile;
    infile.open ("C:\\CODE_JAM\\B-small-attempt0.in");
    outfile.open ("C:\\CODE_JAM\\outputsm.txt");
    int testcase;
    infile>>testcase;
    for(int i=1;i<=testcase;i++)
    {
        int temp=0;
        string str,temporary;
        infile>>str;
        if(str.length()==1)
        {
            outfile<<"Case #"<<i<<": "<<str<<endl;
        }
        else
        {
            int count1=0;
            for(int l=0;l<str.length()-1;l++)
            {
                if(str[l]<=str[l+1])
                {
                    count1++;
                }
            }
            if(count1==str.length()-1)
                outfile<<"Case #"<<i<<": "<<str<<endl;
            else
            {
                for(int j=1;j<str.length();j++)
                {
                    if(str[0]=='1' && str[0]>=str[1])
                    {
                        temp=1;
                        break;
                    }
                    else if(str[j]<=str[j-1])
                    {
                        str[j-1]--;
                        for(int z=j;z<str.length();z++)
                        {
                            str[z]='9';
                        }
                        break;
                    }
                }
                if(temp==1)
                {
                    for(int l=0;l<str.length()-1;l++)
                    {
                        temporary+="9";
                    }
                    outfile<<"Case #"<<i<<": "<<temporary<<endl;
                }
                else
                    outfile<<"Case #"<<i<<": "<<str<<endl;
            }
        }
    }
    infile.close();
    outfile.close();
    return 0;
}
