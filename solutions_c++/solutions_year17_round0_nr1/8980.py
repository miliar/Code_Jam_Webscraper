#include<bits/stdc++.h>
using namespace std;
int main()
{
    ofstream outfile;
    ifstream infile;
    infile.open ("C:\\Users\\ABHISHEK TIWARI\\Desktop\\atom\\code jam\\A-large.in");
    outfile.open ("C:\\Users\\ABHISHEK TIWARI\\Desktop\\atom\\code jam\\outputlong.txt");
    int t;
    infile>>t;
    for(int z=1;z<=t;z++)
    {
        string s;
        int k;
        infile>>s>>k;
        int flips=0,flag=0;
        int i=0;
        while(i<s.length())
        {
            if(s[i]=='-')
            {
                if(i+k-1<s.length())
                {
                    flips++;
                    for(int j=0;j<k;j++)
                    {
                        if(s[i+j]=='+')
                            s[i+j]='-';
                        else
                            s[i+j]='+';
                    }
                }
                else
                {
                    outfile<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<endl;
                    flag=1;
                    break;
                }
            }
            i++;
        }
        //cout<<s<<endl;
        if(flag==0)
        {
            outfile<<"Case #"<<z<<": "<<flips<<endl;
        }
    }
    infile.close();
    outfile.close();
    return 0;
}

