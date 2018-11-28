
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
const ll up = (ll)1000000000000000000;
vector < ll > S;
void gen(ll num){
    if(num>up)
	return;
    if(num){
	S.push_back(num);
    }
    if(num==0){
	for(ll i=1;i<=9;i++){
	    gen(num*10 + i);
	}
    }
    else{
	if(up/num < 10)
	    return;
	ll x = num%10;
	for(ll i=x;i<=9;i++){
	    gen(num*10+i);
	}
    }
}
bool check(ll num){
    vector < int > dig;
    while(num){
	dig.push_back(num%10);
	num/=10;
    }
    reverse(all(dig));
    for(int i =0;i<dig.size()-1;i++){
	if(dig[i]>dig[i+1])
	    return false;
    }
    return true;
}
int main(){
    gen((ll)0);
    sort(all(S));
    int t;
    cin>>t;
    for(int i = 1;i<=t;i++){
	ll num;
	cin>>num;
	auto x = lower_bound(S.begin(),S.end(),num);
	if(*x>num||x==S.end())
	    x--;
	cout<<"Case #"<<i<<": "<<*x<<endl;
    }
}
