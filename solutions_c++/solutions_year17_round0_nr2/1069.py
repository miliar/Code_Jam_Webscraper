#include <bits/stdc++.h>
using namespace std;
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define forex(i,j) for(int i=0;i<(j);i++) // 0 .. N-1
#define forin(i,j) for(int i=0;i<=(j);i++) // 0 .. N
#define printv(v) {for(int i=0;i<v.size();i++) cout<<v[i]<<" ";cout<<"\n";}
#define printa(a,len) {for(int i=0;i<len;i++) cout<<a[i]<<" ";cout << "\n";}

typedef long long ll;
typedef pair<int,int> pii;

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<ll> vll;
typedef vector<pii> vpii;

#define mp make_pair
#define pb push_back
#define uset unordered_set
#define umap unordered_map
#define mset multiset
#define mmap multimap
#define umset unordered_multiset
#define ummap unordered_multimap
#define all(v) (v).begin(),(v).end()

bool isok(string n){
    if(n.size()==1)return true;
    int flag=1;
    for(int i=1;i<n.size();i++)if(n[i]<n[i-1])flag=0;
    return flag;
}

int f(int n){
    while(n--){
        string ss=to_string(n+1);
        if(isok(ss))return (n+1);
    }
}

//int xx[]={0,1,0,-1,-1,-1,1,1,-1};int yy[]={1,0,-1,0,1,1,-1,-1}; //E S W N NE SE SW NW
int main() {
_
int T;cin>>T;

for(int XX=1;XX<=T;XX++){
    string s;ll n;
    cin>>n;
    s=to_string(n);
    if(n==0)
    cout<<"Case #"<<XX<<": "<<"0"<<"\n";
    else{
        while(!isok(s)){
            int ii=1;
            for(;ii<s.size();ii++){
                if(s[ii]<s[ii-1])break;
            }
            s[ii-1]=s[ii-1]-1;
            for(int j=ii;j<s.size();j++)s[j]='9';
        }
        string fans="";
        int i=0;
        for(i=0;i<s.size();i++)if(s[i]!='0')break;
        for(;i<s.size();i++)fans+=s[i];
        cout<<"Case #"<<XX<<": "<<fans<<"\n";
    }
}
return 0;
}
