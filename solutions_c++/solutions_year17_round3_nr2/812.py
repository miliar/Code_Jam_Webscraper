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
  freopen("B-small-attempt0 (1).in", "r", stdin);
    freopen("Output3.out", "w", stdout);


cin>>t;
for(int y=0;y<t;y++)
        {
        	int a1,a2;
        	cin >> a1 >> a2;
        	int ans;
        	for(int i =0;i<a1+a2;i++){
        		cin >> arr[i] >> brr[i];
        	}
        	if(a1 + a2 ==1)ans=2;
        	else if(a1 ==1 && a2 == 1)ans=2;
        	else{
        		if(arr[0] > arr[1]){
        			swap(arr[0],arr[1]);
        			swap(brr[0],brr[1]);
        		}
        		if(brr[1] - arr[0] > 720)ans = 4;
        		if(arr[1] - brr[0] >= 720 )ans = 2;
        		if(brr[1]-arr[0]<=720)ans = 2;

        	}


        cout<<"Case #"<<y+1<<": "<<ans<<"\n";



}




return 0;}

