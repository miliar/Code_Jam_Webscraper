#include <bits/stdc++.h>
using namespace std;

int main()
{
    string ss;
    int T;
    // freopen("B-large.in","r",stdin);
    // freopen("out.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        cin>>ss;
        int len=ss.length();
        while(1)
        {
            bool f=false;
            int pos=-1;
            for(int i=0;i<len-1;i++)
            {
                if(ss[i+1]<ss[i]) {pos=i;f=true;break;}
            }
            if(!f) break;
            ss[pos]-=1;
            for(int i=pos+1;i<len;i++) ss[i]='9';
        }
        // cout<<ss<<endl;
        long long ans=0;
        for(int i=0;i<len;i++) ans=ans*10+ss[i]-'0';
        cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
    return 0;
}
