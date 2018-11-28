#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <tuple>
#include <cmath>
using namespace std;

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        int N,R,O,Y,G,B,V;
        cin>>N>>R>>O>>Y>>G>>B>>V;
        string ans;
        if(O+B==N){
            if(O==B){
                for(int i=0;i<O;i++) ans+="OB";
            }else{
                ans="IMPOSSIBLE";
            }
        }else if(G+R==N){
            if(G==R){
                for(int i=0;i<G;i++) ans+="GR";
            }else{
                ans="IMPOSSIBLE";
            }
        }else if(V+Y==N){
            if(V==Y){
                for(int i=0;i<V;i++) ans+="VY";
            }else{
                ans="IMPOSSIBLE";
            }
        }else{
            if((O&&O>=B)||(G&&G>=R)||(V&&V>=Y)){
                ans="IMPOSSIBLE";
            }else{
                vector<string> RR,YY,BB;
                if(O){
                    string s="B";
                    for(int i=0;i<O;i++){
                        s+="OB";
                        O--;B--;
                    }
                    BB.push_back(s);
                    B--;
                }
                if(G){
                    string s="R";
                    for(int i=0;i<G;i++){
                        s+="GR";
                        O--;R--;
                    }
                    RR.push_back(s);
                    R--;
                }
                if(V){
                    string s="Y";
                    for(int i=0;i<V;i++){
                        s+="VY";
                        O--;Y--;
                    }
                    YY.push_back(s);
                    Y--;
                }
                for(int i=0;i<B;i++) BB.push_back("B");
                for(int i=0;i<R;i++) RR.push_back("R");
                for(int i=0;i<Y;i++) YY.push_back("Y");
                B=BB.size(); R=RR.size(); Y=YY.size();
                if(B>R+Y||R>B+Y||Y>B+R){
                    ans="IMPOSSIBLE";
                }else{
                    if(B==max({B,R,Y})){
                        ans+=BB.back();
                        BB.pop_back();
                        BB.push_back("B");
                    }else if(R==max({B,R,Y})){
                        ans+=RR.back();
                        RR.pop_back();
                        RR.push_back("R");
                    }else{
                        ans+=YY.back();
                        YY.pop_back();
                        YY.push_back("Y");
                    }
                    while(B||R||Y){
                        if(ans.back()=='B'){
                            if(R>Y){
                                ans+=RR.back();
                                RR.pop_back();
                                R--;
                            }else{
                                ans+=YY.back();
                                YY.pop_back();
                                Y--;
                            }
                        }else if(ans.back()=='R'){
                            if(Y>B){
                                ans+=YY.back();
                                YY.pop_back();
                                Y--;
                            }else{
                                ans+=BB.back();
                                BB.pop_back();
                                B--;
                            }
                        }else{
                            if(B>R){
                                ans+=BB.back();
                                BB.pop_back();
                                B--;
                            }else{
                                ans+=RR.back();
                                RR.pop_back();
                                R--;
                            }
                        }
                    }
                    ans.pop_back();
                }
            }
        }
        if(ans!="IMPOSSIBLE"){
            for(auto c:ans){
                B+=c=='B';
                R+=c=='R';
                Y+=c=='Y';
            }
        }
        // cout<<N<<' '<<R<<' '<<O<<' '<<Y<<' '<<G<<' '<<B<<' '<<V<<endl;
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }

    return 0;
}