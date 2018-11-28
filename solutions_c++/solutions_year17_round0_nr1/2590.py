/* 
    Har Har Mahadev
*/

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define pii pair<int,int>
#define pll pair<long long,long long>
#define vi vector<int>
#define vll vector<long long>
#define vpii vector<pair<int,int> >
#define vpll vector<pair<long long,long long> >
#define pb(x) push_back(x)
#define mk(x,y) make_pair(x,y)
#define fir first
#define sec second
#define all(x) x.begin(),x.end()
#define frp(i,x,y) for(i=x;i<=y;i++)
#define frn(i,x,y) for(i=x;i>=y;i--)
#define mod 1000000007ll
#define FILE freopen("input.in", "rt", stdin),freopen("output.txt", "wt", stdout);


template <class T>
T expo(T x,T n) { T result=1; while(n>0){ if(n%2==1) result=(result*x)%mod; x=(x*x)%mod; n=n/2; } return result; }

// ------------------------------------------- Potha Ends Here------------------------------------------------ //

int main(){
	FILE
	int t,u=0;
	cin>>t;
	while(t--){
		u++;
		string s;
		int n,i,j,k,ans=0;
		cin>>s>>k;
		n=s.size();
		
		for(i=0;i<=n-k;i++){
			if(s[i]=='-'){
				ans++;
				for(j=i;j<i+k;j++){
					if(s[j]=='+')
					s[j]='-';
					else
					s[j]='+';
				}
			}
		}
		
		k=0;
		for(i=0;i<n;i++){
			if(s[i]=='-'){
				k++;
			}
		}
		
		cout<<"Case #"<<u<<": ";
		if(k){
			cout<<"IMPOSSIBLE\n";
		}else{
			cout<<ans<<endl;
		}
	}
}
