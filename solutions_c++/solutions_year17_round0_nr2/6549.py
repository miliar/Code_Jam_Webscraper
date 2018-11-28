#include<bits/stdc++.h>

using namespace std;

int main()
{
    int T,t=1;
    long long l,i,j;
    string str;

    ifstream fin;
    ofstream fout;
    fin.open("B-large.in",ios::in);
    fout.open("B-large.txt",ios::out);

    fin>>T;

    while(T--)
    {
        bool flag = false;
        fin>>str;
        l = str.length();

        for(i=1;i<l;i++)
        {
            if(flag)
                str[i]='9';
            else
            {
                if(str[i-1]>str[i])
                {
                    j=i;
                    flag = true;
                    str[i-1]--;
                    str[i]='9';
                }
            }
        }
        while(j)
        {
            j--;
            if(str[j]>str[j+1])
            {
                str[j]=str[j+1];
                str[j+1]='9';
            }
        }
        if(str[0]=='0')
        {
            str = str.substr(1);
        }
        fout<<"Case #"<<t++<<": "<<str<<endl;
    }
    return 0;
}
