#include <bits/stdc++.h>
using namespace std;


#define ll long long int
#define ull unsigned long long int
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define fore(t,i,x) for(int i=t; i<x; ++i)
#define mod 1000000007
#define endl "\n"
#define output freopen("output2.out","w", stdout)
#define input freopen("input2.in","r", stdin)


int main(){

    output;
    input;
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int test;
    cin>>test;
    fore(0,tc,test){
        bool pos=true;
        ll k, tally=0;
        string s;
        cin>>s >> k;
        fore(0,i,s.length()){
            if(s[i]=='-'){
                tally++;
                if((i+k) > s.length()){
                    pos=false;
                    break;
                }
                for(int j=i; j<(i+k); j++){
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }

        }
        if(pos==true)
            cout<<"Case #"<<tc+1<<": "<<tally<<endl;
        else
            cout<<"Case #"<<tc+1<<": IMPOSSIBLE"<<endl;

    }
    return 0;
}
