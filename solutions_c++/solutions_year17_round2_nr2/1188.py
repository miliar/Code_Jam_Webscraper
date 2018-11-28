#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;
int n,r,o,y,g,b,v;
void imp(){
    cout<<"IMPOSSIBLE"<<endl;
}
void wri(char a,char b,int x){
    int i;
    for(i=1;i<=x;i++)
        cout<<b<<a;
}
void solve(){
    if(y==v && y+v==n){
        wri('Y','V',y);
        return;
    }
    if(r==g && r+g==n){
        wri('R','G',r);
        return;
    }
    if(b==o && b+o==n){
        wri('B','O',y);
        return;
    }
    if((v>=y && v) || (g>=r && g) || (o>=b && o)){
        imp();
        return;
    }
    int n1,n2,n3;
    char c1,c2,c3;
    n1=r-g;
    c1='R';
    n2=y-v;
    c2='Y';
    n3=b-o;
    c3='B';
    if(n2>n1){
        swap(n1,n2);
        swap(c1,c2);
    }
    if(n3>n2){
        swap(n2,n3);
        swap(c2,c3);
    }
    if(n2>n1){
        swap(n1,n2);
        swap(c1,c2);
    }
    string st="";
    for(int i=1;i<=n1;i++){
        if(i<=n2){
            st+=c2;
        }
        if(n1-i+1<=n3){
            st+=c3;
        }
        if(st[st.size()-1]==c1){
            imp();
            return;
        }
        st+=c1;
    }
    if(st[0]==st[st.size()-1]){
        imp();
        return;
    }
    int fy=1,fr=1,fb=1;
    for(int i=0;i<st.size();i++){
        cout<<st[i];
        if(st[i]=='Y' && fy){
            wri('Y','V',v);
            fy=0;
        }
        if(st[i]=='R' && fr){
            wri('R','G',g);
            fr=0;
        }
        if(st[i]=='B' && fb){
            wri('B','O',o);
            fb=0;
        }
    }
    cout<<endl;
}
int main(){
    int t;
    freopen("Bs.in","r",stdin);
    freopen("Bs.out","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>n>>r>>o>>y>>g>>b>>v;
        cout<<"Case #"<<i<<": ";
        solve();
    }
}
