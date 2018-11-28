#include <bits/stdc++.h>
using namespace std;

vector< pair<int,char> > v;
int main() 
{
    int r,o,y,g,b,V,t,k=1,n,i,j;
    cin>>t;
    while(t>0)
    {
        cout<<"Case #"<<k<<": ";
        ++k;
        cin>>n>>r>>o>>y>>g>>b>>V;
        vector<char>ans;
        if(r>(n)/2 || y>(n)/2 || b>(n)/2)
        cout<<"IMPOSSIBLE"<<endl;
        else
        {
            v.clear();
            v.push_back({r,'R'});
            v.push_back({y,'Y'});
            v.push_back({b,'B'});
            for(i=0;i<n;i=i+2)
            {
            sort(v.begin(),v.end());
            ans.push_back(v[2].second);
            ans.push_back(v[1].second);
            v[2].first--;
            v[1].first--;
            }
            sort(v.begin(),v.end());
            if(v[2].first!=0)
            ans.push_back(v[2].second);
            if(ans[n-1]==ans[0])
            {
                ch=ans[n-1];
                ans[n-1]=ans[n-2];
                ans[n-2]=ch;
            }
            
            for(i=0;i<n;++i)
            cout<<ans[i];
            cout<<endl;
        }
        
        
        --t;
    }
	return 0;
}

