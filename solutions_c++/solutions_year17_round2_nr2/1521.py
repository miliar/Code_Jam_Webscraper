#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
string s[3]={"GR","VY","OB"};
char c[3]={'R','Y','B'};
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    int T,t;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        int i,n,R, O, Y, G, B, V;
        cin>>n>>R>>O>>Y>>G>>B>>V;
        vector<int>v;v.clear();
        v.push_back(R);
        v.push_back(Y);
        v.push_back(B);
        sort(v.begin(),v.end());
        int m=v[2],h,hh;
        v[0]=R;v[1]=Y;v[2]=B;
        string ans="";
        int f=1;
        for(hh=0;hh<3;hh++)
        {
            h=hh;
            for(i=0;i<n;i++)
            {
                v[h]--;
                if(v[h]<0)break;
                ans+=c[h];
                if(v[(h+1)%3]>v[(h+2)%3]||(v[(h+1)%3]==v[(h+2)%3]&&(h+1)%3==hh))h=(h+1)%3;
                else h=(h+2)%3;
            }
            if(v[h]<0||(ans[0]==ans[ans.length()-1]&&ans.length()>1))continue;
            else {cout<<ans<<endl;f=0;break;}
        }
        if(f)cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
