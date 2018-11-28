#include <bits/stdc++.h>

using namespace std;


void flip(string& str, int i ,int k)
{
    for(int j=i; j<i+k; j++)
    {
        if(str[j] == '-')
        {
            str[j] = '+';
        }
        else
        {
            str[j] = '-';
        }
    }
}

int main()
{
    int t,k=0,x=0;
    int count = 0;
    string str;
    fstream fin,fout;

    fin.open("A-large.in",ios::in);
    fout.open("Output.txt",ios::out);

    fin>>t;

    for(int x=1; x<=t; x++)
    {
        count = 0;

        fin>>str;
        fin>>k;

        for(int i=0; i<str.length(); i++)
        {
            if(str[i] == '-' && i+k <= str.length())
            {
                flip(str,i,k);
                count++;
            }
           else if(i+k > str.length() && str[i] == '-')
            {
                count = -1;
                break;
            }
        }

        if(count!=-1)
            fout<<"Case #"<<x<<": "<<count<<"\n";
        else
            fout<<"Case #"<<x<<": IMPOSSIBLE\n";
    }

    fout.close();
    fin.close();
    return 0;
}

