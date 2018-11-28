#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;

int main(){
    freopen("large1.in", "r", stdin);
    freopen("outL1.txt", "w", stdout);
    int t, k, ca=1;
    string g;
    cin>>t;
    while(ca<=t){
        cin>>g>>k;
        int a = 0;
        cout<<"Case #"<<ca<<": ";
        ca++;
        for(int i=0;i<g.length();i++){
            if(g[i]=='-'){
                if(i+k-1>=g.length()){
                    a=-1;
                    cout<<"IMPOSSIBLE"<<endl;
                    break;
                }
                a++;
                for(int j=1;j<k;j++)
                    g[i+j] = (g[i+j]=='-' ? '+' : '-');
            }
        }
        if(a!=-1)
            cout<<a<<endl;
    }
    return 0;
}