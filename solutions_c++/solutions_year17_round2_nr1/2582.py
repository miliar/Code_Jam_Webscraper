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
#define MOD 1000000007
#define infll 9999999999
#define inf   99999999
using namespace std;
ll fast_exp(ll a,ll b)
{
    ll res = 1;
    res%=MOD;
    while(b>0)
    {
        if(b & 1)
        {
            res = (res*a)%MOD;
        }
        b = b>>1;
        a = (a*a)%MOD;   
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

     ofstream fout;
    ifstream fin;
    fin.open("ip.txt");
    fout.open("prog1.txt");
    	fout << std::fixed;
    fout << std::setprecision(7);
    int t;
    fin>>t;
    rep(i,1,t+1){	
	double d;int n;
	fin>>d>>n;
	double k[n],s[n];
	rep(p,0,n)
	{
		fin>>k[p]>>s[p];
	}
	
	double ma=9999999999;
	double ans=0;
	rep(p,0,n){
		double x=(d-k[p])/s[p];
		//cout<<x<<endl;
		if(x>ans){
		ans=x;	
		}
	}
	ma=d/ans;
	
	fout<<"Case #"<<i<<": "<<ma<<endl;
	}
}
