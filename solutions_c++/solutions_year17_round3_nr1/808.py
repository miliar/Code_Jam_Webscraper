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
int q,n,t,k;
#define pi 3.14159265358
double arr[1003][1003];
vector < pair<double , double > > brr;
int main()
{
  freopen("A-large (1).in", "r", stdin);
    freopen("Output3.out", "w", stdout);


cin>>t;
for(int y=0;y<t;y++)
        {
        	cin >> n  >> k;
        	brr.clear();
        	for(int i = 0;i<=n+1;i++)
        		for(int j = 0;j<=n+1;j++)arr[i][j] = 0.00;
        	for(int i = 0;i<n;i++){
        		double ao,ap;
        		cin >> ao >> ap;
        		brr.pb(   mp(ao,ap) );
        	}
        	sort(all(brr));
        	reverse(all(brr));
        	double ma[1005];
        	for(int i =0;i<1002;i++)ma[i] = 0.00;
        	for(int j = 0;j<n;j++){
        		//cout << brr[j].F << " *";
        		for(int i =1;i<=min(k,j+1);i++){
        			
        			if(i == 1){
        				arr[j][i] = 1.00*pi*brr[j].F*brr[j].F + 2.00*pi*brr[j].F*brr[j].S;
        				//cerr<< arr[j][i] << "*";
        				continue;

        			}

        			
        			arr[j][i] = max(arr[j][i] , ma[i-1] + 2.00*pi*brr[j].F*brr[j].S );}
        			for(int l = 0;l<=k;l++)ma[l] = max(ma[l] , arr[j][l]);

        	}
        	
        	double ans = arr[n-1][k];
        for(int i = k-1;i<n;i++) ans = max(ans,arr[i][k]);



        cout<<"Case #"<<y+1<<fixed << setprecision(12) <<": "<<ans<<"\n";



}




return 0;}

