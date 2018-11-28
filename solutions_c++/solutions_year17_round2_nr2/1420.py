#include <bits/stdc++.h>
using namespace std;


struct nodey{
    double dist;
    double speed;
};

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int pp=1;pp<=t;pp++){
        int n;
        int r,o,y,g,b,v;
        cin >> n;
        cin >> r >> o >> y >> g >> b >> v;
        string ans="";
        if(o==0 && g==0 && v==0){
            int maxx=0;
            maxx=max(r,max(y,b));
            if(maxx==r){
                if(y+b<r){
                    ans="IMPOSSIBLE";
                }
                else{
                    int cnt=y+b-r;
                    y=y-cnt;
                    b=b-cnt;
                    for(int i=0;i<r;i++){
                        ans+='R';
                        if(cnt>0){
                            ans+='Y';
                            ans+='B';
                            cnt--;
                        }
                        else if(y>0){
                            ans+='Y';
                            y--;
                        }
                        else{
                            ans+='B';
                        }
                    }
                }
            }
            else if(maxx==y){
                if(r+b<y){
                    ans="IMPOSSIBLE";
                }
                else{
                    int cnt=r+b-y;
                    r=r-cnt;
                    b=b-cnt;
                    for(int i=0;i<y;i++){
                        ans+='Y';
                        if(cnt>0){
                            ans+='R';
                            ans+='B';
                            cnt--;
                        }
                        else if(r>0){
                            ans+='R';
                            r--;
                        }
                        else{
                            ans+='B';
                        }
                    }
                }
            }
            else{
                if(y+r<b){
                    ans="IMPOSSIBLE";
                }
                else{
                    int cnt=y+r-b;
                    y=y-cnt;
                    r=r-cnt;
                    for(int i=0;i<b;i++){
                        ans+='B';
                        if(cnt>0){
                            ans+='Y';
                            ans+='R';
                            cnt--;
                        }
                        else if(y>0){
                            ans+='Y';
                            y--;
                        }
                        else{
                            ans+='R';
                        }
                    }
                }
            }
        }
        cout << "Case #" << pp << ": " << ans << endl;
        
    }
    // your code goes here
    return 0;
}
