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
        int r,c;
        cin>>r>>c;
        string s[r];
        for(int i=0;i<r;++i)
        {
            cin>>s[i];
        }
        for(int i=0;i<r;++i)
        {
            for(int j=1;j<c;++j)
            if(s[i][j]=='?')
            s[i][j]=s[i][j-1];
        }
        for(int i=0;i<r;++i)
        {
            for(int j=c-2;j>=0;--j)
            if(s[i][j]=='?')
            s[i][j]=s[i][j+1];
        }
        for(int j=0;j<c;++j)
        for(int i=1;i<r;++i)
        {
            if(s[i][j]=='?')
            s[i][j]=s[i-1][j];
        }
        for(int j=0;j<c;++j)
        for(int i=r-2;i>=0;--i)
        {
            if(s[i][j]=='?')
            s[i][j]=s[i+1][j];
        }
        if(s[0][0]=='?')
        {
            for(int i=0;i<r;++i)
            for(int j=0;j<c;++j)
            s[i][j]='A';
        }
        file << "Case #" << z <<":\n" ;
        for(int i=0;i<r;++i)
        file << s[i] << "\n";
    }
    file.close();
    return 0;
}
