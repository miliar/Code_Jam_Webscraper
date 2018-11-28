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
		long long n,i,j,k,x,y,z;
		cin>>n;
		
		if(n%10==0)
		n--;
		
		vector<long long> v;
		while(n){
			v.pb(n%10);
			n=n/10;
		}
		
		reverse(v.begin(),v.end());
		
		k=v.size();
		for(i=0;i<k-1;i++){
			z=0;
			for(j=0;j<k-1;j++){
				if(v[j]>v[j+1]){
					z=1;
					break;
				}
			}
			
			if(z){
				v[j]--;
				for(j=j+1;j<k;j++){
					v[j]=9;
				}
			}else{
				break;
			}
		}
		
		n=0;
		for(i=0;i<k;i++){
			n=n*10+v[i];
		}
		
		cout<<"Case #"<<u<<": "<<n<<endl;
	}
}
