#include <bits/stdc++.h>
using namespace std;

typedef long long int   Int;
#define pii             pair<int,int> 
#define vi              vector<int>
#define pb              push_back
#define mp              make_pair
#define ff              first
#define ss              second
#define MOD             1000000007
#define bug(x)          cout<<">"<<#x<<" = "<<x<<endl

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef ONLINE_JUDGE
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    int T;
    cin>>T;
    for(int tc=1;tc<=T;tc++){
        string ss;
        int K;
        cin>>ss>>K;
        int ff=1;
        for(auto c: ss){
            if(c=='-'){
                ff=0;
                break;
            }
        }
        if(ff==1){
            cout<<"Case #"<<tc<<": 0"<<endl;
            continue;
        }
        bool done=false,cant=false;
        int ans=0;
        int len = ss.length();
        for(int i=0;i<len; i++){
            int j = ss.find('-');
            int rr = j+K;
            if(j==-1){
                done=true;break;
            } 
            else{
                if(len-j<K){
                    cant=true;break;
                }
                else{
                    ans++;
                    for(;j<rr;j++){
                        if(ss[j]=='+'){
                            ss[j]='-';
                        }
                        else{
                            ss[j]='+';
                        }
                    }
                }
            }
        }
        if(cant==true){
            cout<<"Case #"<<tc<<": IMPOSSIBLE"<<endl;
            continue;
        }
        cout<<"Case #"<<tc<<": "<<ans<<endl;
        
    }
    return 0;
}