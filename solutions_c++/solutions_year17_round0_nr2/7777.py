#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;

int main(){
    freopen("small2.in", "r", stdin);
    freopen("outS2.txt", "w", stdout);
    int t, ca=1, f;
    string g;
    cin>>t;
    while(ca<=t){
        f=0;
        cin>>g;
        cout<<"Case #"<<ca<<": ";
        ca++;
        for(int i=1;i<g.length();++i)
            if(g[i]<g[i-1]){
                f = 1;
                break;
            }
        if(!f || g.length()==1)
            cout<<g<<endl;
        else{
            for(int i=0;i<g.length();++i){
                if(g[i]>=g[i+1]){
                    g[i] = g[i]-1;
                    for(int j=i+1;j<g.length();++j)
                        g[j] = '9';
                    break;
                }
            }
            int i=0;
            while(g[i]=='0')
                i++;
            if(i>0)
                g.erase(0, i);
            cout<<g<<endl;
        }
    }
    return 0;
}