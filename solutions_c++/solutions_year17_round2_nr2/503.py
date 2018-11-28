#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define ll long long
#define F first
#define S second
#define pp pair<int,int>
using namespace std;
int n;
pair<int,char> a,b,c,ab,bc,ac;

void solve(){
    a.F-=bc.F;
    b.F-=ac.F;
    c.F-=ab.F;
    if(a.F<0 || b.F<0 || c.F<0){
        cout<<"IMPOSSIBLE"<<endl;
        return;
    }

    if(b.F>a.F)swap(a,b); // a>=b
    if(c.F>a.F)swap(a,c);
    if(c.F>b.F)swap(b,c);

    if(a.F>b.F+c.F){
        cout<<"IMPOSSIBLE"<<endl;
        return;
    }

    string s;
    for(int i=0;i<a.F;i++){
        int k=1;
        if(i+1==a.F)k=b.F+c.F;
        s+=a.S;
        for(int j=0;j<k;j++)
            if(b.F>c.F){
                s+=b.S;
                b.F--;
            }
            else{
                s+=c.S;
                c.F--;
            }
    }

    for(int i=0;i<ac.F;i++){
        for(int j=0;j<s.size();j++)
        if(s[j]=='Y'){
            s.insert(j+1,"VY");
            break;
        }
    }
    for(int i=0;i<bc.F;i++){
        for(int j=0;j<s.size();j++)
        if(s[j]=='R'){
            s.insert(j+1,"GR");
            break;
        }
    }
    for(int i=0;i<ab.F;i++){
        for(int j=0;j<s.size();j++)
        if(s[j]=='B'){
            s.insert(j+1,"OB");
            break;
        }
    }

    if(s=="" && ac.F+bc.F+ab.F>0){
        for(int i=0;i<ac.F;i++)
            s+="VY";
        for(int i=0;i<bc.F;i++)
            s+="GR";
        for(int i=0;i<ab.F;i++)
            s+="OB";
    }
    cout<<s<<endl;
}

int main(){
    freopen("B-small-attempt0.in","r",stdin); freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        //ry = o
        //yb = g
        //rb = v
        cin>>n>> a.F >> ab.F >> b.F >> bc.F >> c.F >> ac.F;
        a.S='R';
        b.S='Y';
        c.S='B';
        ab.S='O';
        bc.S='G';
        ac.S='V';


        cout<<"Case #"<<t<<": ";
        solve();
    }
    return 0;
}
