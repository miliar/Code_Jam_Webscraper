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
	freopen("bb.in","r",stdin);
    freopen("output.txt","w",stdout);
    ll t;
    cin>>t;
    for(int ii=0;ii<t;ii++){
    	ll n,k;
        cin>>n>>k;
        K=k;
        priority_queue<pair<int,int>,vector<pair<int,int>>,cmp> q;
        int n=s.length();
	for(int i=0;i<n;i++){
		rnk[0][i]=s[i]-'a';
		// Sorted rank of the i'th suffix after matching only 1st character.
	}
	vector<pair<pair<int,int>,int>>tup(n);
	for(pos=1,r=1;pos<n;pos*=2,r++){
		for(int i=0;i<n;i++){
			// Information for the ith tuple. Stores Info for ith suffix.
			tup[i].second=i;
			// We have compared first alpha chars. now compare next alpha chars so that 2*alpha chars are matched. at i+alpha we have a string that has already been compared. So use that information..
			tup[i].first.second=(i+pos<n)?rnk[r-1][i+pos]:-1;
			// First value of tuple has same rank as that at last step;
			tup[i].first.first=rnk[r-1][i];
		}
		radix_sort(tup);
		//sort(all(tup),cmp);
		for(int i=0;i<n;i++){
			rnk[r][tup[i].second]=(i>0&&tup[i].first.first==tup[i-1].first.first&&tup[i].first.second==tup[i-1].first.second)?rnk[r][tup[i-1].second]:i;
		}
	} 
	    for(int i = 0; i < size; ++i)
	        print(find_circles(points[i*2], points[i*2 + 1], radius[i]));
        cout<<"Case #"<<ans<<": "<<ans<<" "<<ans1<<endl;
    }
	return 0;
}
