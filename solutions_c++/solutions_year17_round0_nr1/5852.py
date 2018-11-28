#include<bits/stdc++.h>
using namespace std;

int main()
{
    ofstream fout ("output.txt");
    ifstream fin ("A-large.in");
    int tc,caseno=0;
    fin>>tc;

    while (tc--)
    {
        string s;
        fin>>s;
        int k ;
        fin>>k;
        int l=s.length();
        int cnt=0;
        for (int i=0;i<l-k+1;i++)
        {
            if (s[i]=='+') continue;
            cnt++;
            for (int j=i;j<i+k;j++)
            {
                if (s[j]=='+') s[j]='-';
                else s[j]='+';
            }
        }
        bool f=true;
        for (int i=l-k;i<l;i++)
            if (s[i]=='-')
            {
                f=false;
                fout<<"Case #"<<++caseno<<": IMPOSSIBLE\n";
                break;
            }
        if (f) fout<<"Case #"<<++caseno<<": "<<cnt<<"\n";
    }
    return 0;
}
