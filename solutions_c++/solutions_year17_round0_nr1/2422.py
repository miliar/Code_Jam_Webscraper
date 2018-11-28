#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;


int t,k;
string s;


int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("out.txt","wt",stdout);

    cin>>t;
    for(int c=1; c<=t; c++){
        cin>>s>>k;

        int ans=0;
        for(int j=0; j<s.size()-k+1; j++){
            if(s[j]=='-'){
                    ans++;
            for(int d=0; d<k; d++)
                if(s[d+j]=='-'){
                    s[d+j]='+';
                }else {
                s[d+j]='-';
                }
            }
        }
        bool imp=0;
        for(int j=s.size()-k; j<s.size(); j++)
            if(s[j]=='-')imp=1;

        cout<<"Case #"<<c<<": ";
        if(imp)
        cout<<"IMPOSSIBLE\n";
        else cout<<ans<<endl;

    }

    return 0;
}
