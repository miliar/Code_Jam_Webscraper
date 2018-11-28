#include <bits/stdc++.h>
using namespace std;

int ans,sum,t[5],n,p;

void ok(int k)
{
    t[k]--;
    sum=(sum+k)%p;
    if(sum==0) ans++;
}

int main()
{
    ifstream cin("in");
    ofstream cout("out");
    int qw;
    cin>>qw;
    for(int q=1;q<=qw;q++)
    {
        cin>>n>>p;
        ans=1;
        memset(t,0,sizeof t);
        for(int i=0;i<n;i++)
        {
            int tmp;
            cin>>tmp;
            t[tmp%p]++;
        }
        sum=0;
        if(p==2) ans=1+t[0]+t[1]/2-(t[1]%2==0);
        else
            for(int i=0;i<n-1;i++)
            {
                if(t[0]) {
                    ans++;
                    t[0]--;
                    continue;
                }
                if(t[1] && t[p-1])
                {
                    t[1]--;t[p-1]--;
                    i++;
                    if(i<n-1) ans++;
                    continue;
                }
                if(p==4 && t[2]>1)
                {
                    t[2]-=2;
                    i++;
                    if(i<n-1) ans++;
                    continue;
                }
                if(t[2]>0)
                    ok(2);
                else if(t[3]) ok(3);
                else ok(1);
            }
        cout<<"Case #"<<q<<": "<<ans<<endl;
    }
}
