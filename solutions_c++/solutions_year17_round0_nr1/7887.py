#include <bits/stdc++.h>

using namespace std;
#define F first
#define S second
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin>>t;
    for(int z=1 ; z<=t ; z++){
        string kelma;int k,ans=0;
        cin>>kelma>>k;
        for(int i=0 ; i<kelma.size()-k+1 ; i++){
            if(kelma[i]=='+')continue;
            ans++;
            for(int j=i; j<i+k ; j++)
                kelma[j]=(kelma[j]=='-'?'+':'-');
        }
        int flag=0;
        for(int i=0 ; i<kelma.size() ; i++)
            if(kelma[i]=='-')flag=1;
        flag?cout<<"Case #"<<z<<": IMPOSSIBLE"<<endl:
        cout<<"Case #"<<z<<": "<<ans<<endl;
    }

    return 0;

}
