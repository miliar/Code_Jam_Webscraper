#include <bits/stdc++.h>
using namespace std;

typedef long long llu;

void K(llu g, llu v, llu o,vector<string>& R_blocks,vector<string>& Y_blocks,vector<string>& B_blocks){
    if(g > v+o){
        printf("IMPOSSIBLE\n");
        return;
    }
    for(int i=0;i<g-v;i++){
        cout<< B_blocks.back()+R_blocks.back();
        B_blocks.pop_back();
        R_blocks.pop_back();
    }
    for(int i=0;i<(o-(g-v));i++){
        cout<< Y_blocks.back()+B_blocks.back()+R_blocks.back();
        Y_blocks.pop_back();
        B_blocks.pop_back();
        R_blocks.pop_back();
    }
    for(int i=0;i<(g-o);i++){
        cout << Y_blocks.back() + R_blocks.back();
        Y_blocks.pop_back();
        R_blocks.pop_back();
    }
    cout<<endl;
}

void solve(){
    vector<string> R_blocks,Y_blocks,B_blocks;
    llu N,R,O,Y,G,B,V;
    llu v,o,g;
    scanf("%lld %lld %lld %lld %lld %lld %lld\n",&N,&R,&O,&Y,&G,&B,&V);
    if(V>Y || O>B || G>R){
        printf("IMPOSSIBLE\n");
        return;
    }
    //cerr<<N<<" "<<R<<" "<<O<<" "<<Y<<" "<<G<<" "<<B<<" "<<V<<" "<<endl;
    v = Y-V;
    o = B-O;
    g = R-G;
    // YELLOW
    //cout<<"K"<<endl;
    for(int i=0;i<Y-(V+1);i++){
        Y_blocks.push_back("Y");
    }
    //cout<<"A"<<endl;
    string last_block = "Y";
    for(int i=0;i<V;i++){
        last_block += "VY";
    }
    Y_blocks.push_back(last_block);
    // BLUE
    //cout<<"A2"<<endl;
    for(int i=0;i<(B-(O+1));i++){
        B_blocks.push_back("B");
    }
    //cout<<"B"<<endl;
    last_block = "B";
    for(int i=0;i<O;i++){
        last_block += "OB";
    }
    B_blocks.push_back(last_block);
    // RED
    for(int i=0;i<R-(G+1);i++){
        R_blocks.push_back("R");
    }
    //cout<<"C"<<endl;
    last_block = "R";
    for(int i=0;i<G;i++){
        last_block += "GR";
    }
    R_blocks.push_back(last_block);

    if(v==0){
        if(V+Y == N){
            for(int i=0;i<V;i++){
                printf("VY");
            }
            printf("\n");return;
        }else if(V != 0){
            printf("IMPOSSIBLE\n");
            return;
        }
    }
    //cout<<"D"<<endl;
    if(o==0){
        if(B+O == N){
            for(int i=0;i<B;i++){
                printf("OB");
            }
            printf("\n");return;
        }else if(B !=0){
            printf("IMPOSSIBLE\n");
            return;
        }
    }
    if(g==0){
        if(R+G == N){
            for(int i=0;i<R;i++){
                printf("GR");
            }
            printf("\n");return;
        }else if(R != 0){
            printf("IMPOSSIBLE\n");
            return;
        }
    }
    //cout<<"E"<<endl;
    if(g==0){
        if(v != o){
            printf("IMPOSSIBLE\n");
            return;
        }else{
            for(int i=0;i<v;i++){
                cout<< Y_blocks.back() + B_blocks.back();
                Y_blocks.pop_back();
                B_blocks.pop_back();
            }
            printf("\n");return;
        }
    }
    if(v==0){
        if(g != o){
            printf("IMPOSSIBLE\n");
            return;
        }else{
            for(int i=0;i<g;i++){
                cout << R_blocks.back() + B_blocks.back();
                R_blocks.pop_back();
                B_blocks.pop_back();
            }
            printf("\n");return;
        }
    }
    if(o==0){
        if(g != v){
            printf("IMPOSSIBLE\n");
            return;
        }else{
            for(int i=0;i<g;i++){
                cout<< R_blocks.back() + Y_blocks.back();
                R_blocks.pop_back();
                Y_blocks.pop_back();
            }
            printf("\n");return;
        }
    }
    //cout<<"F"<<endl;

    if(g>= v && v>=o){
        K(g,v,o,R_blocks,Y_blocks,B_blocks);
    }else if(g>=o && o>=v){
        K(g,o,v,R_blocks,B_blocks,Y_blocks);
    }else if(v>=o && o>=g){
        K(v,o,g,Y_blocks,B_blocks,R_blocks);
    }else if(v>=g && g>=o){
        K(v,g,o,Y_blocks,R_blocks,B_blocks);
    }else if(o>=v && v>=g){
        K(o,v,g,B_blocks,Y_blocks,R_blocks);
    }else if(o>=g && g>=v){
        K(o,g,v,B_blocks,R_blocks,Y_blocks);
    }

}

int main() {
    int T;
    scanf("%d\n",&T);
    for(int i=1;i<=T;i++){
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}