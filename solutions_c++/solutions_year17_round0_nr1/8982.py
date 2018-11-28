#include<bits/stdc++.h>
using namespace std;
int main()
{
    ofstream outfile;
    ifstream infile;
    infile.open ("C:\\CODE_JAM\\A-large.in");
    outfile.open ("C:\\CODE_JAM\\output_large.txt");
    int testcase;
    infile>>testcase;
    for(int var=1;var<=testcase;var++)
    {
        int i=0;
        int temp=0;
        string str;
        int len;
        infile>>str>>len;
        int cake_flip=0;
        while(i<str.length())
        {
            if(str[i]=='-')
            {
                if(i+len-1<str.length())
                {
                    cake_flip++;
                    for(int l=0;l<len;l++)
                    {
                        if(str[i+l]=='+')
                            str[i+l]='-';
                        else
                            str[i+l]='+';
                    }
                }
                else
                {
                    temp=1;
                    outfile<<"Case #"<<var<<": "<<"IMPOSSIBLE"<<endl;
                    break;
                }
            }
            i++;
        }
        if(temp==0)
        {
            outfile<<"Case #"<<var<<": "<<cake_flip<<endl;
        }
    }
    infile.close();
    outfile.close();
    return 0;
}


