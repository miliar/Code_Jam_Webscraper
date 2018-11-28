#include<bits/stdc++.h>

using namespace std;

int main()
{
    int T, k, ctr, t=1;
    string str;

    ifstream fin;
    ofstream fout;
    fin.open("A-large.in",ios::in);
    fout.open("A-large.txt",ios::out);
    fin>>T;

    while(T--)
    {
        ctr=0;
        bool flag = false;
        fin>>str>>k;
        int l = str.length();

        for(int i=0;i<=l-k;i++)
        {
            if(str[i]=='-')
            {
                ctr++;
                for(int j=0;j<k;j++)
                {
                    if(str[i+j]=='-')
                        str[i+j] = '+';
                    else
                        str[i+j] = '-';
                }
            }
        }
        for(int i=l-k-1;i<l;i++)
        {
            if(str[i]=='-')
                flag=true;
        }
        fout<<"Case #"<<t++<<": ";
        if(flag)
            fout<<"IMPOSSIBLE";
        else
            fout<<ctr;
        fout<<endl;
    }
    return 0;
}
