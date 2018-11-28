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

ll stll(st mystr){
 stringstream convert(mystr);
	ll x;
	convert>>x;
	return x;
}

st llts(ll a){
	std::stringstream ss;
    ss << a;
    st result=ss.str();
    return result;

}

ll check(ll n){
    st s=llts(n);
    st p=llts(n);
    sort(s.begin(),s.end());
   // cout<<s<<" "<<p<<"  ";
    if(s.compare(p)!=0) return 0;
    return 1;
}

int main(){
   ios::sync_with_stdio(0);
   cin.tie(0);
   //type code here
   ll t;
   st n;
   cin>>t;
   fori(j,1,t+1,1){
       cin>>n;
        ford(i,n.length()-1,0,1){
            if(n[i]<n[i-1]){
                fori(k,i,n.length(),1) n[k]='9';
                n[i-1]=n[i-1]-1;
            }
        }
        ll p=stll(n);
        cout<<"Case #"<<j<<": "<<p<<endl;
   }
  return 0;
}
