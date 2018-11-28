#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("cook.in",ios::in);
    fout.open("output.txt",ios::out);

    int t;
    fin>>t;

    for(int i=1;i<=t;i++)
    {
        string s;
        int k,ans=0,j,m;

        fin>>s>>k;

        for(j=0;j<=s.length()-k;j++)
        {
            if(s.at(j)=='-')
            {
                ans++;
                for(m=j;m<j+k;m++)
                {
                    if(s.at(m)=='-')
                        s.at(m)='+';
                    else
                        s.at(m)='-';
                }
            }
        }
        bool flag=false;
        for(j=s.length()-k+1;j<s.length();j++)
        {
            if(s.at(j)=='-')
            {
                flag=true;
                break;
            }
        }
        if(flag)
            fout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        else
            fout<<"Case #"<<i<<": "<<ans<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
