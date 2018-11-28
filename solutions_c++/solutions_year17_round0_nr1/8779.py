#include <bits/stdc++.h>
using namespace std;
#define lli long long int
#define mp(x,y) make_pair(x,y)

bool shi(string s){
    for(int i=0;i<s.length();i++)
        if(s[i]=='-') 
            return false;
    return true;
}
int main(){
    lli t,val=1;
    string s,tmpstr;
    lli k;
    cin>>t;
    while(t--){
        bool yo=false;
        cin>>s>>k;
        lli n=s.length();
        set<string> st;
        st.clear();
        queue<pair<string,lli> > q;
        q.push(mp(s,0));
        st.insert(s);
        cout<<"Case #"<<val<<": ";
        while(!q.empty()){
        pair<string,lli> temp=q.front();
        q.pop();
        if(shi(temp.first)){
        cout<<temp.second<<"\n";
        yo=true;
        break;
        }
            for(int i=0;i<=n-k;i++){
            tmpstr=temp.first;
                for(int j=i;j<=i+k-1;j++){
                if(tmpstr[j]=='+')
                    tmpstr[j]='-';
                    else
                    tmpstr[j]='+';
                }
                if(st.find(tmpstr)==st.end()){
                q.push(mp(tmpstr,temp.second+1));
            st.insert(tmpstr);
                }
            }
        }
        if(!yo)            cout<<"IMPOSSIBLE\n";
       val++;
    }
    return 0;
}