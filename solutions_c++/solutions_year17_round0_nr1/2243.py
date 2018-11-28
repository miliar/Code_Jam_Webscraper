#include <bits/stdc++.h>
#define mx 100011
#define mp make_pair
#define pb push_back
#define ppb pop_back
#define mod 1000000009
#define ff first
#define ss second
#define ll long long
#define PII pair<int,int>
#define inf 1000000000000000
#define RIGHT 131072
#define SIZE 262144
using namespace std;
int solve(string s,int n){
    int ans=0;
    for(int i=0;i<=s.length()-n;i++){
        if(s[i]=='-'){
            for(int j=i;j<i+n;j++){
                s[j] = (s[j]=='-')?'+':'-';
            }
            ans++;
        }
    }
    for(int i=0;i<s.length();i++){
        if(s[i]=='-'){
            return -1;
        }
    }
    return ans;
}
int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int caseno=0;
    while(t--){
        string s;
        int n;
        cin>>s>>n;
        cout<<"Case #"<<++caseno<<": ";
        int p =solve(s,n);
        if(p==-1){
            cout<<"IMPOSSIBLE"<<endl;
        }
        else{
            cout<<p<<endl;
        }
    }
    return 0;
}
