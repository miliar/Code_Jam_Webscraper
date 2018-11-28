#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define rep(i,n) for(ll i=0;i<(ll)(n);i++)
#define all(a)  (a).begin(),(a).end()
#define pb emplace_back
#define INF (1e9+1)
//#define INF (1LL<<59)

int main(){
    int T;
    cin>>T;
    rep(t,T){
        bool f=false;
        
        int n;
        vector<int> inp(6);
        cin>>n;
        rep(i,6)cin>>inp[i];
        
        int r,o,y,g,b,v;
        r = inp[0];
        o = inp[1];
        y = inp[2];
        g = inp[3];
        b = inp[4];
        v = inp[5];
        
        int m=INF;
        vector<pair<int,string>> vp;
        vector<string> vs;

        if( (o!=0&&o+1>b) || (g!=0&&g+1>r) || (v!=0&&v+1>y) ){
            int res = (o!=0&&o+1>b) + (g!=0&&g+1>r) + (v!=0&&v+1>y);
            if(b==o && y==0 && g==0 && r==0 && v==0){
                cout<<"Case #"<<t+1<<": ";
                rep(j,b){
                    cout<<"BO";
                }
                cout<<endl;
                continue;
            }else if(r==g && y==0 && b==0 && o==0 && v==0){
                cout<<"Case #"<<t+1<<": ";
                rep(j,r){
                    cout<<"RG";
                }
                cout<<endl;
                continue;
                
            }else if(v==y && b==0 && g==0 && r==0 && o==0){
                cout<<"Case #"<<t+1<<": ";
                rep(j,v){
                    cout<<"YV";
                }
                cout<<endl;
                continue;
            }
            f=true;
        }else{
            
            r-=g;
            y-=v;
            b-=o;
            
            vp.pb(make_pair(r,"R"));
            vp.pb(make_pair(y,"Y"));
            vp.pb(make_pair(b,"B"));
            
            sort(all(vp));
            
            m = vp[2].first;
            vs.resize(m,vp[2].second);
            
            for(int i=0;i<m;i++){
                if(vp[1].first>0){
                    vs[i]+=vp[1].second;
                    vp[1].first--;
                }else{
                    if(vp[0].first>0){
                        vs[i]+=vp[0].second;
                        vp[0].first--;
                    }else{
                        f=true;
                        break;
                    }
                }
            }
        }
        if(f){
            cout<<"Case #"<<t+1<<": ";
            cout<<"IMPOSSIBLE"<<endl;
        }else{
            rep(i,m){
                if(vp[0].first>0){
                    vs[i]+=vp[0].second;
                    vp[0].first--;
                }else break;
            }
            cout<<"Case #"<<t+1<<": ";
            string ans = "";
            rep(i,vs.size())ans+=vs[i];
            
            if(o>0){
                rep(i,ans.size()){
                    if(ans[i]=='B'){
                        string str="";
                        rep(j,o){
                            str+="BO";
                        }
                        str+="B";
                        ans = ans.substr(0,i) + str + ans.substr(i+1);
                        break;
                    }
                }
            }

            if(g>0){
                rep(i,ans.size()){
                    if(ans[i]=='R'){
                        string str="";
                        rep(j,g){
                            str+="RG";
                        }
                        str+="R";
                        ans = ans.substr(0,i) + str + ans.substr(i+1);
                        break;
                    }
                }
            }
            
            if(v>0){
                rep(i,ans.size()){
                    if(ans[i]=='Y'){
                        string str="";
                        rep(j,v){
                            str+="YV";
                        }
                        str+="Y";
                        ans = ans.substr(0,i) + str + ans.substr(i+1);
                        break;
                    }
                }
            }

            cout<<ans<<endl;
        }
    }
}