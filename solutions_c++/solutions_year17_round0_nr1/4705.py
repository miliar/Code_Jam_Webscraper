#include<bits/stdc++.h>
using namespace std;
#define pb push_back
typedef vector<int> vi;
typedef long long int ll;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a2.out","w",stdout);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        string S;
        int k;
        cin>>S;
        cin>>k;

        int p,n,ans=0,f=0;
        p=count(S.begin(),S.end(),'+');
        n=count(S.begin(),S.end(),'-');
        //cout<<"p:"<<p<<"\t"<<"n:"<<n;
        int size=S.size();
        if(n==0) {cout<<"Case #"<<z<<": "<<"0"<<"\n";f=1; continue    ;}
        for(int i=0;i<size;i++)
        {
            if(S[i]=='-')
            {   ans++;

                if(i+k<=size)
                {
                for(int j=i;j<i+k;j++)
                {
                    if(S[j]=='-') S[j]='+';
                    else S[j]='-';
                }
                /*p=count(S.begin(),S.end(),'+');
                n=count(S.begin(),S.end(),'-');
                cout<<"p:"<<p<<"\t"<<"n:"<<n;*/
                }
                else {cout<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<"\n"; f=1; continue;}

            }
        }
        if(f==0)
            cout<<"Case #"<<z<<": "<<ans<<"\n";
        //cout<<p<<"\n"<<n;
    }
    return 0;
}
