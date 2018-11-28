/*While alive CODE*/

                    /*War will happen and code will follow*/

#include <bits/stdc++.h>
using namespace std;
#define mem(x,y) memset(x,y,sizeof(x))
#define bitcount    __builtin_popcountll
#define mod 1000000007
#define N 1000009
#define fast ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define ss(s) cin>>s;
#define si(x)  scanf("%d",&x);
#define sl(x)  cin>>x;
#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()
#define S second
#define F first
#define ll long long 
ll power(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
string a,b,c;
int arr[N];
int brr[N];
ll t,n,k;
ll mx,mn;
void solve(ll n,ll k){
	if(k == 1){
		mx = n/2;
		mn = (n-1)/2;
		return ;
	}
	k--;
	if(k%2)solve(n/2, k/2 + 1);
	else solve((n-1)/2 , k/2 );
}
int main()
{
  freopen("C-large.in", "r", stdin);
    freopen("Output331.out", "w", stdout);


cin>>t;
for(int y=0;y<t;y++)
        {
        	
        	cin >> n >>k;
        	solve(n,k);



        cout<<"Case #"<<y+1<<": "<<mx<<" "<<mn<<"\n";



}




return 0;}

