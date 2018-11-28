#include<bits/stdc++.h>
#define N 1005
#define M 1000000007
#define vi vector<int>
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define rep(i,s,e) for(int i=s;i<e;i++)
#define drep(i,s,e) for(int i=e-1;i>=s;i--)
#define all(x) (x).begin(),(x).end()
using namespace std;
typedef long long ll;
int index(string &s){
    for(int i=0;i<s.size();i++){
        if(s[i]=='r')
            return i;
    }
    return s.size();
}
int n;
void palce(string &s,int r,int b,int y,char a,char b1,char c){
     int i=0;
        while(r--){
            s[i]=a; i+=2;
            if(i>n-1)
                i= index(s);
        } while(b--){

            s[i]=b1;
            i+=2;
            if(i>n-1)
                i= index(s);
        }
        while(y--){
            s[i]=c;
            i+=2;
            if(i>n-1)
                i = index(s);
        }
}

int main(){
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++){
        int r,b,g,y,o,v;
        cin>>n;
        cin>>r>>o>>y>>g>>b>>v;
        string s(n,'r');
        cout<<"Case #"<<ii<<": ";

        if(r>n/2|| b>n/2|| y>n/2){
            cout<<"IMPOSSIBLE"<<endl;
            continue;
            
         }/*
        palce(s,r,b,y,'R','B','Y');
        cout<<s<<endl;
        continue;*/
        if(r>=b&&r>=y){
            if(b>y){
                palce(s,r,b,y,'R','B','Y');
            }
            else
                palce(s,r,y,b,'R','Y','B');
        }
        else if(b>=r&&b>=y){
            if(r>y){
                palce(s,b,r,y,'B','R','Y');
            }
            else
                palce(s,b,y,r,'B','Y','R');
        }
        else  if(y>=b&&y>=r){
            if(b>r){
                palce(s,y,b,r,'Y','B','R');
            }
            else
                palce(s,y,r,b,'Y','R','B');
        }
        cout<<s<<endl;
    }
    return 0;
}
