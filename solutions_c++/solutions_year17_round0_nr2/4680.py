#include<bits/stdc++.h>
using namespace std;
#define pb push_back
typedef vector<int> vi;
typedef long long int ll;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b2.out","w",stdout);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        string S; int f=0;
        cin>>S;
        ll size=S.size();
        //cout<<size;
        for(int i=size-1;i>0;i--)
        {
            if(S[i]<S[i-1])
            {
                for(int j=i;j<size;j++)
                    S[j]='9';
                if(S[i-1]=='1'){f=1; S[i-1]='0';}
                else {S[i-1]-=1; }
            }
        }
       // cout<<"f : "<<f<<"\n";
        if(f==0) cout<<"Case #"<<z<<": "<<S<<"\n";
        else {  S.erase(0, min(S.find_first_not_of('0'), S.size()-1));
            cout<<"Case #"<<z<<": "<<S<<"\n";
        };
    }
    return 0;
}
