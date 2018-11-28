#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;
int T;
string S;
int K;
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>S>>K;
        int nr=0,sgn=1;
        queue<int> op;
        for(int i=0;i<=S.size()-K;i++)
        {
            while(!op.empty()&&op.front()<=i-K) {op.pop();sgn*=-1;}
            if((sgn==1&&S[i]=='-')||(sgn==-1&&S[i]=='+'))
            {
                sgn*=-1;
                nr++;
                op.push(i);
            }
        }
        bool ok=0;
        for(int i=S.size()-K+1;i<S.size();i++)
        {
            while(!op.empty()&&op.front()<=i-K) {op.pop();sgn*=-1;}
            if((sgn==1&&S[i]=='-')||(sgn==-1&&S[i]=='+'))
            {
                ok=1;
            }
        }
        cout<<"Case #"<<t<<": ";
        if(ok) cout<<"IMPOSSIBLE";
        else cout<<nr;
        cout<<"\n";
    }
    return 0;
}
