#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define ull unsigned long long int
#define pb push_back
#define vi vector<int>
#define vll vector<ll>
#define vs vector<string>
#define vull vector<ull>
#define all(v) v.begin(),v.end()
#define mp make_pair
#define bitcount(x) __builtin_popcountll(x)
//min_arr(v) min_element(v,v+n);
#define dulo 1000000007
#define charcount(s,c) count(s.begin(), s.end(), c)
#define each(a,b) memset(a,b,sizeof a) //for b=0/-1, all pos,s for multidim arr too;
#define tofsi(s,c,t) memset(s,c,t) // for char s[n],first t;
#define tofs(s,pos,c,t) fill_n(s.begin()+pos, t, c);
long double pi = acos(-1.0);
ll power(ll x, ll y){
    ll temp;
    if( y == 0)
       return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return (temp*temp);
    else
    {
        if(y > 0)
            return (((x*temp))*temp);
        else
            return (temp*temp)/x;
    }
}

long long int mul_inv(long long int n,long long int p,long long int m){
	if(p==1){
		return n%m;
	}
	else if(p%2==0){
		long long int t= mul_inv(n,p/2,m);
		return ((t)*(t))%m;
	}
	else{
		long long int t= mul_inv(n,p/2,m);
		return ((((n%m)*t)%m)*t)%m;
	}
}

bool isprime(ll n){
	if(n==2){
		return true;
	}
	if(n%2==0){
		return false;
	}
	for(ll i=3;i<=sqrt(n);i+=2){
		if(n%i==0){
			return false;
		}
	}
	return true;
}
/*
struct compare {
    bool operator() (point&a,point&b) const{
        int o=orientation(p0,a,b);
        if(o==0){
        	return (distsq(p0,b) >= distsq(p0,a))? -1 : 1;
		}
		return (o==2)?-1:1;
    }
};*/


/*
---------------------Priority Queue Compare Operator------------------------

priority_queue<int, std::vector<int>, compare> pq;

*/

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
	/*freopen("fbh.in","r",stdin);
    freopen("B-large.out","w",stdout);*/
	/*float ans;
	std::cout << std::fixed;
    std::cout << std::setprecision(9);
    std::cout << ans;
	*/
	int t;
    cin>>t;
    for(int ii=0;ii<t;ii++){
        string s;
        int k;
		cin>>s>>k;
		int flag1=1,flag2=1,c1=0,c2=0;
        string temp=s;
        vi v;
		int n;
		cin>>n;
		for(int i=0;i<n;i++){
			int a;
			cin>>a;
			v.pb(a);
		}
		heapsort(v);
		for(int i=0;i<n;i++){
			cout<<v[i]<<" ";
		}
        vi v;
		int n;
		cin>>n;
		for(int i=0;i<n;i++){
			int a;
			cin>>a;
			v.pb(a);
		}
		heapsort(v);
		for(int i=0;i<n;i++){
			cout<<v[i]<<" ";
		}vi v;
		int n;
		cin>>n;
		for(int i=0;i<n;i++){
			int a;
			cin>>a;
			v.pb(a);
		}
		heapsort(v);
		for(int i=0;i<n;i++){
			cout<<v[i]<<" ";
		}
        for(int i=0;i<s.length();i++) if(temp[i]=='-'){
        	f2=0;
		}
        if(flag1==0 && flag2==0) cout<<"Case #"<<T-t<<": "<<"IMPOSSIBLE"<<endl;
        else if(flag1==1 && flag2==1) cout<<"Case #"<<T-t<<": "<<min(c1,c2)<<endl;
        else if(flag1==1) cout<<"Case #"<<T-t<<": "<<c1<<endl;
        else cout<<"Case #"<<T-t<<": "<<c2<<endl;
    }
	return 0;
}
