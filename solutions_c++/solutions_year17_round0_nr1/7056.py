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
        int k;
        cin>>k;
        int n=s.length(),ans=0;
        for(int i=0;i<n-k+1;++i)
        {
            if(s[i]=='-')
            {
                for(int j=i;j<i+k;++j)
                {
                    if(s[j]=='-')
                    s[j]='+';
                    else s[j]='-';
                }
                ans++;
            }
        }
        int f=0;
        for(int i=n-k;i<n;++i)
        if(s[i]=='-')
        f=1;
        if(f)
        file <<"Case #"<<z<<": IMPOSSIBLE\n";
        else file<<"Case #"<<z<<": "<<ans<<"\n";
    }
    file.close();
    return 0;
}
