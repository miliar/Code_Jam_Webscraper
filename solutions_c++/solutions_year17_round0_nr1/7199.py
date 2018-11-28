#include <bits/stdc++.h>
using namespace std;
int main()
{
    int T,i,j,k,K;
    string s;
    cin >>T;
    ofstream fout;
    fout.open("Code.txt");
    int c=1;
    while(T--)
    {
        cin >>s>>K;
        int len=s.length();

        int ans=0;
        bool flag=1;
        for(i=0;i<len;i++)
        {
            if(s[i]=='-')
            {
                for(j=i;j<i+K && j<len;j++)
                {
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
                ans++;
                if(i+K>len)
                    flag=0;
            }
        }
        fout <<"Case #"<<c<<": ";
        if(flag==0)fout <<"IMPOSSIBLE\n";
        else fout <<ans<<endl;
        c++;

    }

    return 0;

}
