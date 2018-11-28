#include<bits/stdc++.h>

using namespace std;
string s;
int k;
int mini = 1e9;

void tryall (int i ,string si,int cnt){
    if(i==s.size()-(k-1)){
            //cout<<i<<si<<endl;
            bool ok =true;
        for(int j=0;j<si.size();j++){
            if(si[j]=='-')ok = false;
        }
        if(ok)mini = min(mini,cnt);
        return;
    }
    tryall(i+1,si,cnt);
    for(int j=i;j<i+k;j++){
        if(si[j]=='+')si[j]='-';
        else if(si[j]=='-')si[j]='+';
    }
    tryall(i+1,si,cnt+1);
}


int main(){
   // freopen("A-small-attempt2.in","r",stdin);
    //freopen("pan1.txt","w",stdout);
    int T;
    cin>>T;
    for(int O=0;O<T;O++){
            mini= 1e9;
        cin>>s;
        cin>>k;
        tryall(0,s,0);
        if(mini==1e9)cout<<"Case #"<<O+1<<": IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<O+1<<": "<<mini<<endl;
    }
}
