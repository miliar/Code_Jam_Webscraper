#include <bits/stdc++.h>
using namespace std;
int main(){
    int g,t,k,i,j,f,v;
    cin>>t;
    for(int z=1;z<=t;z+=1)
    {
        string s;
        cin>>s>>k;
        f=0;
        v=s.size();
        for(i=0;i<=(v-k);i+=1)
            {
            if(s[i]=='-')
                {
                for(j=i;j<=(i+k)-1;j++)
                    {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                    }
                f+=1;
                }
            }
        g=0;
        for(i=0;i<=v-1;i+=1)
            if(s[i]!='+'){g=1;break;}
        if(g==0)
            cout<<"Case #"<<z<<": "<<f<<"\n";
        else
            cout<<"Case #"<<z<< ": "<<"IMPOSSIBLE"<<"\n";
    }
    return 0;
}
