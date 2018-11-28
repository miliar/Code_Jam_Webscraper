#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.txt","w",stdout);

    int T,Case=1;
    cin>>T;
    while(T--)
    {
        cout<< "Case #" << Case++ << ": ";

        string S;
        int K;
        cin>>S>>K;

        int ans=0,f=0;

        for(int i=0;i<S.size();i++)
        {
            if(S[i]=='-')
            {
                if(i+K>S.size()) { f=1; break; }
                ans++;

                for(int j=0;j<K;j++) S[i+j]='+'+'-'-S[i+j];
            }
        }

        if(f) cout<<"IMPOSSIBLE"<<endl;
        else cout<<ans<<endl;
    }

    return 0;
}

