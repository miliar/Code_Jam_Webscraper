#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define ll long long
using namespace std;
ifstream fin("in.in");
ofstream fo("out.out");
int test,n,r,o,y,g,b,v;
int c[5];
string ans;
void up(int il){
    if(il==1) ans.pb('R');
    else if(il==2) ans.pb('Y');
    else ans.pb('B');
}
int ok(){
    for(int i=1;i<n;i++){
        if(ans[i]==ans[i-1]) return 0;
    }
    if(ans[n-1]==ans[0]) return 0;
    return 1;
}
int main(){
    ios_base::sync_with_stdio(0);
    fin>>test;
    for(int t=1;t<=test;t++){
        int ck=0;
        fin>>n>>r>>o>>y>>g>>b>>v;
        ans.clear();
        c[1]=r;
        c[2]=y;
        c[3]=b;
        int ml=r,id=1,sid,sml;
        fo<<"Case #"<<t<<": ";
        if(y>ml){
            ml=y;
            id=2;
        }
        if(b>ml){
            ml=b;
            id=3;
        }
        up(id);
        c[id]--;
        for(int i=1;i<n;i++){
            if(id==1){
                sid=2;
                sml=c[2];
                if(c[3]>sml){
                    sid=3;
                    sml=c[3];
                }
            }
            else if(id==2){
                sid=1;
                sml=c[1];
                if(c[3]>sml){
                    sid=3;
                    sml=c[3];
                }
            }
            else{
                sid=1;
                sml=c[1];
                if(c[2]>sml){
                    sid=2;
                    sml=c[2];
                }
            }
            if(c[sid]<=0){
                ck=1;
                break;
            }
            c[sid]--;
            up(sid);
            id=sid;
        }
        if(ck==1){
            fo<<"IMPOSSIBLE\n";
            continue;
        }
        ck=0;
        if(ans[n-1]==ans[0]){
            for(int i=1;i<n-1;i++){
                swap(ans[n-1],ans[i]);
                if(ok()==1){
                    ck=1;
                    break;
                }
                swap(ans[n-1],ans[i]);
            }
        }
        else ck=1;
        if(ck==0){
            fo<<"IMPOSSIBLE";
        }
        else{
            for(int i=0;i<n;i++){
                fo<<ans[i];
            }
        }
        fo<<endl;
    }
}
