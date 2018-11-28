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
	//std::cout << std::fixed;
    //std::cout << std::setprecision(7);
    ifstream fin;
    fin.open("ip1.txt");
    ofstream fout;
    fout.open("op1.txt");
    int t;
    fin>>t;
    rep(p,1,t+1){
    	string s;
    	fin>>s;
    	int k;
    	fin>>k;
    	int l=s.length()-k;
    		int i=0,c=0;
			while(i<=l){
    		if(s[i]=='-'){
    			if(i<=l){
    				c++;
    				rep(m,i,i+k){
    					if(s[m]=='-')
    					s[m]='+';
    					else
    					s[m]='-';
					}
				}
			}
			i++;	
			}
			rep(i,0,s.length()){
				if(s[i]=='-'){
					c=-1;break;
				}
			}
		//	cout<<s<<endl;
			if(c==-1)
			fout<<"Case #"<<p<<": IMPOSSIBLE"<<endl;
			else
			fout<<"Case #"<<p<<": "<<c<<endl;
	}
}
