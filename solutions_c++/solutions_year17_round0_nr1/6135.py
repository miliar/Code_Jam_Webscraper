/* 
    -----------------------------------------------
    -----------------------------------------------
             Copyrights with magnifico
    -----------------------------------------------
    -----------------------------------------------
		CodeChef    :- magnifico
		Spoj        :- magnifico
		Codeforces  :- magnifico_mudit
		HackerRank  :- magnifico_mudit
		HackerEarth :- magnifico
		Github      :- magnifico-mudit
    -----------------------------------------------
    -----------------------------------------------
             Copyrights with magnifico
    -----------------------------------------------
    -----------------------------------------------
                                                       */


#include<bits/stdc++.h>
#define ll long long
#define st string
#define ch char
#define ife(i,j) i==j?1:0
#define vec(i) vector<i>
#define fori(i,v,l,in) for(ll i=v;i<l;i+=in)
#define ford(i,v,l,in) for(ll i=v;i>l;i-=in)
#define pb push_back
#define map(i,j) map<i,j>
#define mp make_pair
#define pr(i,j) pair<i,j>
#define fs first(
#define se second

using namespace std;


ll t,k;
st s;

ll check(st s){
    ll a=0,b=0;
    if(s.find('+')==string::npos) a=1;
    if(s.find('-')==string::npos) b=1;
    if(a+b==1&&a==1) return 1;
    else if(a+b==1&&b==1) return 0;
    else return -1;
}

ll solve(st s){
    ll p=0;
    fori(i,0,s.length()-k,1){
        if(s[i]=='-'){
            p++;
            fori(j,i,i+k,1){
                if(s[j]=='+') s[j]='-';
                else s[j]='+';
            }
        }
    }
    ll idx=s.length()-k;
    ll j=check(s.substr(idx,k));
    if(j>=0) return p+j;
    else return -1;
}

int main(){
   ios::sync_with_stdio(0);
   cin.tie(0);
   //type code here
   cin>>t;
   fori(i,1,t+1,1){
       cin>>s>>k;
       ll p=solve(s);
       if(p!=-1) cout<<"Case #"<<i<<": "<<p;
       else cout<<"Case #"<<i<<": IMPOSSIBLE";
       cout<<endl;
   }
  return 0;
}
