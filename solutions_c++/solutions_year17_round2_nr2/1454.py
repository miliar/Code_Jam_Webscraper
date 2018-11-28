#include<bits/stdc++.h>

#define INF 9223372036854775807
#define mod 1000000007
#define ll  long long int
#define ld double
#define endl '\n'
#define sz 300005
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

using namespace std;
stack <char> st1,st2,st3;

ll n,r,o,y,g,b,v;

void init(){
    while(!st1.empty()){
        st1.pop();
    }
    while(!st2.empty()){
        st2.pop();
    }
    while(!st3.empty()){
        st3.pop();
    }
}

int main(){
    //fast();
    ll t,i,j;
    cin>>t;
    for(j = 1; j <= t;j++){
        cin>>n>>r>>o>>y>>g>>b>>v;
        ll flag =0;
        init();
        if(r >= y && r >= b){
            for(i = 0; i < r; i++)
                st1.push('R');
            for(i = 0; i < b; i++)
                st2.push('B');
            for(i = 0; i < y; i++)
                st3.push('Y');
        }
        else if(y >= r && y >= b){
            for(i = 0; i < r; i++)
                st2.push('R');
            for(i = 0; i < b; i++)
                st3.push('B');
            for(i = 0; i < y; i++)
                st1.push('Y');
        }
        else if(b >= r && b >= y){
            for(i = 0; i < r; i++)
                st3.push('R');
            for(i = 0; i < b; i++)
                st1.push('B');
            for(i = 0; i < y; i++)
                st2.push('Y');
        }
        //cout<<st1.size()<<' '<<st2.size()<<' '<<st3.size()<<endl;
        cout<<"Case #"<<j<<": ";
        if(st1.size() > st2.size() + st3.size()){
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }

        while(true){
            if(flag%2 == 0){
                cout<<st1.top();
                st1.pop();
                if(st1.empty())
                    break;
            }
            else{
                if(st2.size() > st3.size()){
                    cout<<st2.top();
                    st2.pop();
                }

                else {
                    cout << st3.top();
                    st3.pop();
                }
            }
            flag++;
            //cout<<"first"<<endl;
        }
        flag = 0;
        while(st2.size() > 0 || st3.size() >  0){
            if(flag%2 == 0 && st2.size() > 0){
                cout<<st2.top();
                st2.pop();
            }
            else if(flag%2 == 1 && st3.size() > 0){
                cout<<st3.top();
                st3.pop();
            }
            flag++;
            //cout<<"second";
        }
        cout<<endl;
    }
    return 0;
}
