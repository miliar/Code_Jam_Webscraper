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
int q,n,t;
int arr[N];
int brr[N];
int main()
{
  freopen("A-large.in", "r", stdin);
    freopen("Output31.out", "w", stdout);


cin>>t;
for(int y=0;y<t;y++)
        {
        	cin >> a;
        	for(int i = 0;i<10000;i++)arr[i] = 0;
        	cin >> n;
        	for(int i = 0;i<a.size();i++)if(a[i] != '+')arr[i] = 1;
        	int mi = 0;
        	for(int i = 0;i<a.size() - n + 1;i++){
        		if(arr[i] == 1){
        				mi++;
        				int j = i;
        				for(int k = 0;k<n;k++)arr[i+k] = 1 - arr[i+k];
        		}
        	}
        	bool p = false;
        	for(int i = 0 ;i<a.size();i++)if(arr[i] != 0){ cout<<"Case #"<<y+1<<": "<<"IMPOSSIBLE"<<"\n";
        		p = true;
        		break;
        }

        if(!p)
        	 cout<<"Case #"<<y+1<<": "<<mi<<"\n";



}




return 0;}

