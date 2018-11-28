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

//int xx[]={0,1,0,-1,-1,-1,1,1,-1};int yy[]={1,0,-1,0,1,1,-1,-1}; //E S W N NE SE SW NW
int main() {
_
int T;cin>>T;

for(int XX=1;XX<=T;XX++){
    int n;cin>>n;
    int R,O,Y,G,B,V;

        cin>>R>>O>>Y>>G>>B>>V;
        vector<pair<int,char>> v;
        v.pb({R,'R'});v.pb({Y,'Y'});v.pb({B,'B'});
        sort(all(v));
        int a=v[0].first,b=v[1].first,c=v[2].first;
        char AA=v[0].second,BB=v[1].second,CC=v[2].second;//cout<<R<<Y<<B;
        if(a+b<c)
    cout<<"Case #"<<XX<<": "<<"IMPOSSIBLE"<<"\n";
    else{
        if(a==0){
            string ab="";
            ab+=BB;ab+=CC;

            string fin="";
            for(int i=0;i<b;i++)fin+=ab;
            cout<<"Case #"<<XX<<": "<<fin<<"\n";
        }
        else{
        string hh="";hh+=AA;//cout<<hh;
        vector<string> ss(a,hh);
        //for(int i=0;i<a;i++){ss[i]+=C;c--;}
        int nbc=b/a;int nbr=b%a;
        string h="";h+=BB;h+=CC;
        string tt=h;
        int gg=nbc;
        gg--;
        while(gg--)h+=tt;
        for(int i=0;i<a;i++)ss[i]+=h;
        for(int i=0;i<nbr;i++)ss[i]+=tt;
        c-=b;
        for(int i=0;i<c;i++)ss[i].insert(1,1,CC);
        string ans="";
        for(auto aa:ss)ans+=aa;
        cout<<"Case #"<<XX<<": "<<ans<<"\n";
    }}
}
return 0;
}
