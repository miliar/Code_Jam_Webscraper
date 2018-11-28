#include <bits/stdc++.h>
using namespace std;
#define INF 100000000

typedef long long ll;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    string ss;
    int n;
    int t,c=1,con;
    bool ans=false;
    cin>>t;
    while(t--)
    {
        cin>>ss; cin>>n;
        con=0;
        ans=false;
        for(int i=0;i<=ss.size()-n;i++)
        {
            if(ss[i]=='-')
            {
                con++;
                for(int j=0;j<n;j++)
                    ss[i+j]=((ss[i+j]=='-')?'+':'-');
            }
                
        }
        cout<<"Case #"<<c++<<": ";
        for(int i=0;i<n;i++)
            if(ss[ss.size()-1-i]=='-')
            {
                ans=true;cout<<"IMPOSSIBLE";
                break;
            }
                
        if(!ans)
            cout<<con;
        cout<<"\n";
    }
    return 0;
}