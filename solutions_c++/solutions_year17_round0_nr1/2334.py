#include <bits/stdc++.h>
#define ll long long int
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define itr vector <int> :: iterator
#define vi vector <int> 
#define lb lower_bound
#define fast ios::sync_with_stdio(0);cin.tie(0);
#define tt int t; cin>>t; while(t--)
#define ff first
#define ss second
#define fora(i,a,b) for(i=a;i<b;i++)
#define reva(i,a,b) for(i=a;i>=b;i--)
using namespace std;



void F(){
    string a;
    int i,j,k,m,n,sum=0;
    cin>>a>>k;
    n=a.size();
    int st[n+1]={0};
    fora(i,0,n){
        if(a[i]=='+')
            sum++;
    }
    if(sum==n){
        cout<<"0\n";
        return;
    }
    int ct=0;
    while(1){
        int flag=0;
        fora(i,0,n){
            if(a[i]=='-'){
                if(i+k<=n){
                    if(st[i]==2){
                        if(sum==n){
                            cout<<ct<<endl;
                        }
                        else{
                            cout<<"IMPOSSIBLE\n";
                        }
                        return;
                    }
                    st[i]++;
                    fora(j,i,i+k){
                        if(a[j]=='-'){
                            sum++;
                            a[j]='+';
                        }
                        else{
                            sum--;
                            a[j]='-';
                        }
                    }
                    ct++;
                    if(sum==n){
                        cout<<ct<<endl;
                        return;
                    }
                    flag++;
                }
            }
        }
        reva(i,n-1,0){
            if(a[i]=='-'){
                if(i+1-k>=0){
                    if(st[i]==2){
                        if(sum==n){
                            cout<<ct<<endl;
                        }
                        else{
                            cout<<"IMPOSSIBLE\n";
                        }
                        return;
                    }
                    st[i]++;
                    reva(j,i,i+1-k){
                        if(a[j]=='-'){
                            sum++;
                            a[j]='+';
                        }
                        else{
                            sum--;
                            a[j]='-';
                        }
                    }
                    ct++;
                    if(sum==n){
                        cout<<ct<<endl;
                        return;
                    }
                    flag++;
                }
            }
        }
        if(!flag){
            cout<<"IMPOSSIBLE\n";
            return;
             
        }
    }
}

int main(){
    fast
    int x=1;
    tt{
        cout<<"Case #"<<x<<": "; 
        F();
        x++;
    }

}