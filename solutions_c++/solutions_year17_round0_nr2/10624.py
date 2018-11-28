//template--------------------//
#include<bits/stdc++.h>
using namespace std;

#define gc getchar//zz_unlocked
#define pb push_back
#define mp make_pair
#define fi first
#define se second 
#define ll long long int
#define rep(i,s,e) for(i=s;i<e;i++)
#define all(c) c.begin(), c.end() 
#define revsort(v) std::sort(v.begin(), v.end(), std::greater<ll>());
#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define present(c,x) ((c).find(x) != (c).end())
#define vpresent(container, element) (find(all(container),element) != container.end())

#define inf 100005

typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vii;
typedef vector<pll> vll;

ll gcd(ll a,ll b){if(b==0)return a;return gcd(b,a%b);}
ll lcm(ll a,ll b){return((a*b)/gcd(a,b));}
//fast-IO
void scanint(int &x){register int c = gc();x = 0;int neg = 0;for(;((c<48 || c>57) && c != '-');c = gc());if(c=='-') {neg=1;c=gc();}
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}if(neg) x=-x;}


// template---------------------------//

bool istidy[1001];
void init(){
    int i,j,k;
    for(i=0;i<=9;i++)istidy[i]=true;
    
    for(i=10;i<=1000;i++){
        int t = i,flag=0;
        int r1 = t%10,r2;
        t = t/10;
        while(t!=0){
            r2 = t%10;
            t = t/10;
            if(r2 > r1){
                flag=1;break;
            }
            r1 = r2;
        }
        if(flag==1)istidy[i] = false;
        else istidy[i] = true;
    }
}

int main(){
ios_base::sync_with_stdio(false);
init();
int t;
cin>>t;
for(int cas=1;cas<=t;cas++){
    int n,i;
    cin>>n;
    //if(istidy[n]==true)cout<<"Case #"<<cas<<": "<<n<<endl;
    
    	while(istidy[n]!=true)n--;
    	cout<<"Case #"<<cas<<": "<<n<<endl;
}

	return 0;
}	


	




