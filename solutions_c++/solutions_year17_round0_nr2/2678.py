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
void func(int ie ){
	bool f = true;

	for(int i = 0;i<a.size();i++){
		if(arr[i] == arr[ie] && f){
			f = false;
			arr[i]-=1;
		}
		else if(!f)arr[i] = 9;
	}
}
void prin(){
	bool p = true;
	for(int i = 0;i<a.size();i++)
		if(arr[i] == 0 && p)continue;
		else {cout<<arr[i];p= false;}
}
int main()
{
  freopen("B-large.in", "r", stdin);
    freopen("Output32.out", "w", stdout);


cin>>t;
for(int y=0;y<t;y++)
        {

        	cin >> a;
        	for(int i = 0;i<a.size();i++)
        		arr[i] = a[i] - '0';
        	for(int i = 0;i<a.size()-1;i++)
        		if(arr[i] > arr[i+1])
        		{
        			func(i);
        			break;
        		}



        cout<<"Case #"<<y+1<<": ";
        prin();
        cout<<"\n";



}




return 0;}

