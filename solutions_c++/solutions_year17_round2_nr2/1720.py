#include <bits/stdc++.h>

using namespace std;
int arr[300];
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    int cases=0;
    while(T--){
        cases++;
        int N,R,O,Y,G,B,V;
        memset(arr,0,sizeof arr);
        cin>>N>>R>>O>>Y>>G>>B>>V;
        for(int i=0;i<R;i++)
            arr['R']++;
        for(int i=0;i<O;i++){
            arr['R']++;
            arr['Y']++;
        }
        for(int i=0;i<Y;i++)
            arr['Y']++;
        for(int i=0;i<G;i++){
            arr['Y']++;
            arr['B']++;
        }
        for(int i=0;i<B;i++)
            arr['B']++;
        for(int i=0;i<V;i++){
            arr['B']++;
            arr['R']++;
        }
        string ans="IMPOSSIBLE";
        if(arr['B']>N/2||arr['R']>N/2||arr['Y']>N/2||B<O||R<G||Y<V||(B==O&&B+O!=N&&B!=0)||(R==G&&R+G!=N&&G!=0)||(Y==V&&Y+V!=N&&V!=0)){
                cout<<"Case #"<<cases<<": "<<ans<<endl;
                continue;
        }
        string ans1;
        if(O+B==N&&O){
            if(O!=B){
                cout<<"Case #"<<cases<<": "<<ans<<endl;
                continue;
            }
            cout<<"Case #"<<cases<<": ";
            for(int i=0;i<O;i++)
                cout<<"OB";
            cout<<endl;
            continue;
        }
         if(G+R==N&&G){
            if(G!=R){
                cout<<"Case #"<<cases<<": "<<ans<<endl;
                continue;
            }
            cout<<"Case #"<<cases<<": ";
            for(int i=0;i<G;i++)
                cout<<"GR";
            cout<<endl;
            continue;
        }
        if(Y+V==N&&Y){
            if(Y!=V){
                cout<<"Case #"<<cases<<": "<<ans<<endl;
                continue;
            }
            cout<<"Case #"<<cases<<": ";
            for(int i=0;i<V;i++)
                cout<<"VY";
            cout<<endl;
            continue;
        }
        if(O){
            ans1.push_back('B');
            B--;
        }
        while(O--){
            ans1.push_back('O');
            ans1.push_back('B');
            B--;
        }
        string ans2;
        if(G){
            ans2.push_back('R');
            R--;
        }
        while(G--){
            ans2.push_back('G');
            ans2.push_back('R');
            R--;
        }
        string ans3;
        if(V){
            ans3.push_back('Y');
            Y--;
        }
        while(V--){
            ans3.push_back('V');
            ans3.push_back('Y');
            Y--;
        }
        if(ans1.size())
            B++;
        if(ans2.size())
            R++;
        if(ans3.size())
            Y++;
        string pr;
        bool lR=false,lB=false,lY=false;
        if(R){
            pr.push_back('R');
            lR=true;
            R--;
        }
        else if(Y){
            pr.push_back('Y');
            lY=true;
            Y--;
        }

        while(R||Y||B){
            if(R>=Y&&R>=B&&!lR){
                pr.push_back('R');
                R--;
                lR=true;lB=false;lY=false;
            }
            else if(Y>=R&&Y>=B&&!lY){
                pr.push_back('Y');
                Y--;
                lR=false;lB=false;lY=true;
            }
            else if(B>=Y&&B>=R&&!lB){
                pr.push_back('B');
                B--;
                lR=false;lB=true;lY=false;
            }
            if(R<=max(Y,B)&&R>=min(Y,B)&&R&&!lR){
                pr.push_back('R');
                R--;
                lR=true;lB=false;lY=false;
            }
            else if(Y>=min(R,B)&&Y<=max(R,B)&&Y&&!lY){
                pr.push_back('Y');
                Y--;
                lR=false;lB=false;lY=true;
            }
            else if(B>=min(Y,R)&&B<=max(Y,R)&&B&&!lB){
                pr.push_back('B');
                B--;
                lR=false;lB=true;lY=false;
            }
        }
        cout<<"Case #"<<cases<<": ";
        for(int i=0;i<pr.size();i++){
            if(ans1.size()&&pr[i]=='B'){
                cout<<ans1;
                ans1.clear();
            }
            else if(ans2.size()&&pr[i]=='R'){
                cout<<ans2;
                ans2.clear();
            }
            else if(ans3.size()&&pr[i]=='Y'){
                cout<<ans3;
                ans3.clear();
            }
            else
                cout<<pr[i];
        }
        cout<<endl;
    }
    return 0;
}
