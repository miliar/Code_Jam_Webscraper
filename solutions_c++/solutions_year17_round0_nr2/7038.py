#include<bits/stdc++.h>
using namespace std;
int main()
{
    ofstream file;
    file.open("/home/sanban/Downloads/filename.txt");
    int tc;
    cin>>tc;
    for(int z=1;z<=tc;++z)
    {
        string s;
        cin>>s;
        int n=s.length();
        for(int i=n-1;i>=1;--i)
        {
            if((s[i]-'0')<(s[i-1]-'0'))
            {
                for(int j=i;j<n;++j)
                s[j]='9';
                s[i-1]=(int)(s[i-1]-'0'-1)+'0';
            }
        }
        file <<"Case #"<<z<<": ";
        int i;
        for(i=0;i<n;++i)
        if(s[i]!='0')
        break;
        for(int j=i;j<n;++j)
        file <<s[j];
        file <<"\n";
    }
    file.close();
    return 0;
}
