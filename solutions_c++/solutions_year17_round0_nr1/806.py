#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define ld long double
#define vi vector<int> 
#define ii pair<int,int>
#define vii vector<ii>
#define loop(x,i,a,b) for(x i=a;i<=b;i++)
#define loopi(i,a,b) for(int i=a;i<=b;i++)
#define loop2(i,a,b) for(i=a;i<=b;i++)  
#define rloop(x,i,a,b) for(x i=a;i>=b;i--)
#define rloopi(i,a,b) for(int i=a;i>=b;i--)
#define rloop2(i,a,b) for(i=a;i>=b;i--)  
#define X first
#define Y second 
//#define fill(a,x) memset(a,x,sizeof(a))
#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()
//#define DEBUG
const long double pi = atan(1.0)*4.0;
const ll mod = 1e9+7;
const ll INF = 1e18;
#ifdef DEBUG
#define dout(x) cout<<x;
#define douttb(x) cout<<x<<" ";
#define doutln(x) cout<<x<<endl;
#else
#define dout(x)
#define douttb(x)
#define doutln(x)
#endif
#define N 100001

char flip(char ch){
	if(ch=='+') return '-';
	return '+';
}
int main()
{	
	int ans,t,k,n;
	cin>>t;
	string s;
	loop(int,T,0,t-1){
		cin>>s;
		cin>>k;
		n = s.size();
		ans = 0;
		loop(int,i,0,n-k){
			if(s[i]=='-'){
				ans ++;
				loop(int,j,0,k-1){
					s[i+j]=flip(s[i+j]);
				}
			}
		}
		loop(int,i,n-k+1,n-1){
			if(s[i]=='-')
				ans=-1;
		}
		cout<<"Case #"<<T+1<<": ";
		if(ans ==-1)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<ans<<endl;
	}
	return 0;	
}
