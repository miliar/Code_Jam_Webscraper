#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("aa2.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        string n;
        int k;
        cin>>n>>k;
        int f=0;
        for(int j=0;j<n.length()-k+1;j++){
            if(n[j]=='+')continue;
            f++;
            for(int l=j;l<j+k;l++)
                n[l]=(n[l]=='-')?'+':'-';
        }
        bool imp=false;
        for(int j=0;j<n.length();j++){
            if(n[j]=='-'){
                imp=true;
                break;
            }
        }
        cout<<"Case #"<<i+1<<": ";
        if(!imp)cout<<f;
        else cout<<"IMPOSSIBLE";
        cout<<endl;
    }
    return 0;
}
