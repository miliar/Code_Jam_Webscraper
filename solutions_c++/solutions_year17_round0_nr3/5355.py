#include<bits/stdc++.h>
#define rep(i,a,b) for(int i=a;i<b;i++)
#define ll long long int
#define pii pair<int,int>
#define pll pair<ll,ll>
#define all(c) (c).begin(),(c).end()
#define pb push_back
#define vi vector <int>  
#define vii vector <vector <int> >
#define vl vector<ll>
#define vpi vector<pii>
#define vpl vector<pll>
#define rall(c) (c).rbegin(),(c).rend() 
#define mp make_pair
#define itr iterator
#define tr(it,c) for(it=(c).begin();it!=(c).end();it++)
#define ins insert
#define priq priority_queue
#define mset(a,val) memset(a,val,sizeof(a))
#define ff first
#define ss second
#define sz(x) (int)x.size()
#define infll 9999999999
#define inf   99999999
using namespace std;
ll n;
ll fast_exp(ll a,ll b)
{
    ll res = 1;
    while(b>0)
    {
        res=res*2;
		if(res>=n)
		break; 
    }
    return res;
}
int gcd(int a,int b)
{
    if(b==0)
        return a;
    else return gcd(b,a%b);
    
}
vector<int> prime_factorize(int n) {
    vector<int> res;
    for (int i = 2; i * i <= n; ++i) {
        while (n % i == 0) {
            res.push_back(i);
            n /= i;
        }
    }
    if (n != 1) {
        res.push_back(n);
    }
    return res;
}
int lg2(ll x){
	int c=0;
	while(x)
	{
	x=x>>1;c++;}
	return c-1;
}
int main(){
	std::ios_base::sync_with_stdio(false);
	//std::cout << std::fixed;
    //std::cout << std::setprecision(7);
    ifstream fin;
    fin.open("ip3.txt");
    ofstream fout;
    fout.open("op4.txt");
    int t;
    fin>>t;
    rep(p,1,t+1){
    ll k;
	fin>>n>>k;
	priq<ll> pq;
	pq.push(n);
	while(k>1){
		ll x=pq.top();
		pq.pop();
		k--;
		if(x==1)
		break;
		pq.push(x/2);
		pq.push(max(x-1-x/2,0ll));
	}
	while(k>1)
	{
		pq.pop();k--;
	}
	ll x=pq.top();pq.pop();
	ll x1=x/2;
	ll x2=max(x-1-x/2,0ll);
	fout<<"Case #"<<p<<": "<<x1<<" "<<x2<<endl;	
	}
}
