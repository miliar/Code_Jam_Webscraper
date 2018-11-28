
#include "bits/stdc++.h"
//#include "prettyprint.hpp"

using namespace std;

#define endl '\n'

#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)

#define all(x) x.begin(),x.end()
#define mp make_pair

#define ll long long
#define ld long double
#define pb push_back

#define MOD 1000000007

#define pi 2*acos(0)

#define fr first
#define se second

#define vi vector < int >
#define pii pair < int , int >
#define pll pair < ll , ll >

#define fast_io ios_base::sync_with_stdio(0);cin.tie(NULL)

#define LSB(x) x&-x
#define nb(x) __builtin_popcount(x)
int cntr = 0;
void solve(){
    cntr++;
    string s;
    cin>>s;
    int k;
    cin>>k;
    int moves = 0;
    for(int i=0;i<s.length()-k+1;i++){
	if(s[i]=='+') continue;
	int j = k,i2=i;
	while(j--){
	    if(s[i2]=='+')
		s[i2] = '-';
	    else s[i2] = '+';
	    i2++;
	}
	moves++;
    }
    for(int i=0;i<s.length();i++){
	if(s[i]=='-'){
	    cout<<"Case #"<<cntr<<": IMPOSSIBLE"<<endl;
	    return;
	}
    }
    cout<<"Case #"<<cntr<<": "<<moves<<endl;

}
int main(){
    int t;
    cin>>t;
    while(t--){
	solve();
    }
    return 0;
}
