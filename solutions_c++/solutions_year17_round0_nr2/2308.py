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
bool prime[100010];

void F(){
    string a;
    cin>>a;
    int i,j,n,k;
    n=a.size();
    string s=a;
    for(i=a.size()-1;i>0;i--){
        if(a[i]<a[i-1]){
            fora(j,i,n){
                a[j]='9';
            }
            a[i-1]--;
        }
    }
    bool flag=0;
    fora(i,0,n){
        if(a[i]=='0' && !flag){
            continue;
        }
        else{
            flag=1;
            cout<<a[i];
        }
    }
    cout<<endl;
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