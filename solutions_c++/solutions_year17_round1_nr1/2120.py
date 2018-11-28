#include <bits/stdc++.h>
using namespace std ;
/*
An_Tea_Love.
Never_Give_Up.
*/
#define ft first
#define sd second
#define pb push_back
#define ll long long int
#define mp make_pair
#define loop(i, a, b) for(i=a; i<b; i++)
#define run	ios_base::sync_with_stdio(0)
const int mod = 1e9 + 7;
const ll INF = 1e17;
int main(){
    run;
    ll t,r,c,i,j,k,l,p=0;
    cin>>t;
    while(t--){
        p++;
        ll a[26]={0};
        cin>>r>>c;
        string s[r];
        loop(i,0,r){
            cin>>s[i];
        }
        k=0;
        ll row=0;
        loop(i,0,r){
            l=0;
            loop(j,0,s[i].length()){
                if(s[i][j]=='?'){
                    l++;
                }
            }
            if(l!=s[i].length()){
                row=i;
                break;
            }
        }
        char d;
        loop(i,0,s[row].length()){
            if(s[row][i]!='?'){
                d=s[row][i];
                break;
            }
        }
        loop(i,0,s[row].length()){
            if(s[row][i]=='?'){
                s[row][i]=d;
            }
            else{
                d=s[row][i];
            }
        }

        for(i=row-1;i>=0;i--){
            l=0;
            loop(j,0,s[i].length()){
                if(s[i][j]=='?'){
                    l++;
                }
            }
            if(l==s[i].length()){
                loop(j,0,s[i].length()){
                    s[i][j]=s[i+1][j];
                }
            }
            else{
                char g;
                loop(j,0,s[i].length()){
                    if(s[i][j]!='?'){
                        g=s[i][j];
                        break;
                    }
                }
                loop(i,0,s[i].length()){
                    if(s[i][j]=='?'){
                        s[i][j]=g;
                    }
                    else{
                        g=s[i][j];
                    }
                }
            }
        }
        for(i=row+1;i<r;i++){
            l=0;
            loop(j,0,s[i].length()){
                if(s[i][j]=='?'){
                    l++;
                }
            }
            if(l==s[i].length()){
                loop(j,0,s[i].length()){
                    s[i][j]=s[i-1][j];
                }
            }
            else{
                char g;
                loop(j,0,s[i].length()){
                    if(s[i][j]!='?'){
                        g=s[i][j];
                        break;
                    }
                }
                loop(j,0,s[i].length()){
                    if(s[i][j]=='?'){
                        s[i][j]=g;
                    }
                    else{
                        g=s[i][j];
                    }
                }
            }
        }
        cout<<"Case #"<<p<<":"<<endl;
        loop(i,0,r){
            loop(j,0,s[i].length()){
                cout<<s[i][j];
            }
            cout<<endl;
        }
        cout<<endl;
    }
return 0;

}



