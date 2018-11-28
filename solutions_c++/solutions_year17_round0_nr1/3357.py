#include <bits/stdc++.h>
using namespace std;

const int N = 1000+10;
int A[N];

int main()
{
    int T,k;
    string ss;
    // freopen("A-large.in","r",stdin);
    // freopen("out.out","w",stdout);
    cin>>T;
    int iCase=0;
    while(T--)
    {
        iCase++;
        cin>>ss>>k;
        int len=ss.length();
        for(int i=0;i<len;i++)
        {
            if(ss[i]=='+') A[i]=1;
            else A[i]=0;
        }
        int ans=0;
        for(int i=0;i<len;i++)
        {
            if(i+k>len) break;
            if(A[i]==0)
            {
                ans++;
                for(int j=i;j<i+k;j++)
                {
                    A[j]^=1;
                }
            }
        }
        bool f=true;
        for(int i=0;i<len;i++) if(A[i]==0) {f=false;break;}
        cout<<"Case #"<<iCase<<": ";
        if(f) cout<<ans<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
