#include<bits/stdc++.h>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("out114.txt");
int main()
{
    int t;
    fin>>t;
    for(int x=1;x<=t;x++)
    {
        string s;
        int k;
        fin>>s;
        fin>>k;
        int f=0,cnt=0;
        int l=s.length();
        for(int i=0;i<l;i++)
        {
            if(s[i]=='-')
            {
                if((i+k)>l)
                {
                    f=1;
                    break;
                }
                else{
                        cnt++;
                    for(int j=i;j<i+k;j++)
                    {
                        if(s[j]=='+')
                            s[j]='-';
                        else
                            s[j]='+';
                    }
                }
            }
        }
        fout<<"Case #"<<x<<": ";
        if(f)
            fout<<"IMPOSSIBLE"<<endl;
        else
            fout<<cnt<<endl;


    }
    return 0;
}
