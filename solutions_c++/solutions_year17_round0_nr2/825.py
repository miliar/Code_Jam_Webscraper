#include<bits/stdc++.h>
using namespace std;
string s,t;
int main(){
    ios_base::sync_with_stdio(0);
    int i,tc,cc=0;
    cin>>tc;
    while(cc<tc){
        cin>>s;
        t=s;
        i=s.length()-1;
        while(!is_sorted(t.begin(),t.end())){
            t[i]='9';
            --i;
            while(t[i]=='0'){
                t[i]='9';
                --i;
            }
            --t[i];
            if(t[0]=='0')t.erase(t.begin());
        }
        cout<<"Case #"<<++cc<<": "<<t<<'\n';
    }
    return 0;
}
