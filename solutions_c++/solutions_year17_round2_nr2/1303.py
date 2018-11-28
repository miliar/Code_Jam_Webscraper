#include<bits/stdc++.h>
using namespace std;


//long long int a[100001];
double pos[10001],sp[10001];
int main(){
      freopen("C:\\Users\\Chandan\\Desktop\\input.txt", "r", stdin);
freopen("C:\\Users\\Chandan\\Desktop\\gcj.txt", "w", stdout);
long long N;
double D,x,y;
int t;
cin>>t;
int lc=1;
while(t--){
        cout<<"Case #"<<lc<<": ";
        lc++;
    int a,b,c,d,e,f,i;
        cin>>N>>a>>b>>c>>d>>e>>f;
        b=c;
        c=e;
string ans="";
    if(a>=b && a>=c){
    if(a>(b+c)){
    cout<<"IMPOSSIBLE"<<endl;
    continue;
    }
   int  y=(c+b)-a;

    for(int i=0;i<a;i++){
    ans+='R';
    if(b>0){
    ans+='Y';
b--;
    if(y>0){
        ans+='B';
        y--;
    }
    continue;
    }
    else {
    ans+='B';
    c--;
    }
    }

       cout<<ans<<endl;
continue;
    }



    if(b>=a && b>=c){
    if(b>(a+c)){
    cout<<"IMPOSSIBLE"<<endl;
    continue;
    }
   int  y=(c+a)-b;

    for(int i=0;i<b;i++){
    ans+='Y';
    if(a>0){
    ans+='R';
a--;
    if(y>0){
        ans+='B';
        y--;
    }
    continue;
    }
    else {
    ans+='B';
    c--;
    }
    }

       cout<<ans<<endl;
continue;
    }




   if(c>=a && b<=c){
    if(c>(a+b)){
    cout<<"IMPOSSIBLE"<<endl;
    continue;
    }
   int  y=(a+b)-c;

    for(int i=0;i<c;i++){
    ans+='B';
    if(a>0){
    ans+='R';
a--;
    if(y>0){
        ans+='Y';
        y--;
    }
    continue;
    }
    else {
    ans+='Y';
    b--;
    }
    }

       cout<<ans<<endl;
continue;
    }

}
return 0;
}
