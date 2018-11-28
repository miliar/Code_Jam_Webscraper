#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        string s;
        cin>>s;
        int k;
        cin>>k;
        int l=int(s.size());
        int x=0;
        for(int i=0;i<l;i++)
        {
            if(s[i]=='+')
            {
                int y=l-1-i;
                x=x^(1<<y);
            }
        }
        int d=((1<<l)-1);
        int level[1000000];
        for(int i=0;i<1000000;i++)level[i]=-1;
        level[x]=0;
        queue<int>q;
        q.push(x);
        while(!q.empty())
        {
            int u=q.front();
            q.pop();
            if(u==d)break;
            for(int i=0;i<=(l-k);i++)
            {
                int z=u;
                for(int j=i;j<(i+k);j++)
                z=z^(1<<j);
                if(level[z]==-1)
                {
                    level[z]=level[u]+1;
                    q.push(z);
                }
            }
        }
        if(level[d]==-1)cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
        else
        cout<<"Case #"<<t<<": "<<level[d]<<endl;
    }
    return 0;
}