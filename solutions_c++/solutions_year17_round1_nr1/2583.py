#include<bits/stdc++.h>
using namespace std;
#define PI 3.14159265358979323846
#define ull unsigned long long
#define ll long long
#define MOD 1000000007
#define sn(t) scanf("%d",&t);
#define snl(t) scanf("%lld",&t);
#define snc(t) scanf("%c",&t);
#define sns(t) scanf("%s",&t);
#define swap(a,b,t) (t=a,a=b,b=t)

ll power(ll a,ll b){
	ll res=1;
	while(b){
		if(b%2==1)
		res=(res*a)%MOD;
		a=(a*a)%MOD;
		b/=2;
	}
	return res%MOD;
}
ll power(ll a,ll b,ll mod){
	if(b==0)
	return 1;
	if(b==1)
	return (a%mod);
	else{
		if(b%2==0){
			ll temp=power(a,b/2,mod);
			return (temp*temp)%mod;
		}
		else{
			ll temp=power(a,b/2,mod);
			temp=(temp*temp)%mod;
			return (temp*a)%mod;
		}
	}
}
ll gcd(ll a,ll b){
	if(b==0)
	return a;
	return gcd(b,a%b);
}
ll lcm(ll a,ll b){
	return (a*b)/gcd(a,b);
}
ll moduloinverse(ll a,ll mod){
	return power(a,mod-2,mod);
}
ll min(ll a,ll b){
	return a>b?b:a;
}
ll max(ll a,ll b){
	return a>b?a:b;
}

ll binarysearch(ll *a,ll n,ll k){
	ll low=0,high=n-1,mid;
	while(low<=high){
		mid=low+(high-low)/2;
		if(a[mid]<k){
			low=mid+1;
		}
		else if(a[mid]>k){
			high=mid-1;
		}
		else{
			return mid;
		}
	}
	return -1;
}
string tostring(long long n)
{
   string s;
   while(n!=0)
  {
      s+=(n%10)+'0';
      n/=10;
   }
    reverse(s.begin(), s.end());
    return s;
}
int main(){
	#ifndef ONLINE_JUDGE
		freopen("inp.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	int st,t,k,cnt,r,c,x,y;
	sn(t);
	st=1;
	char str[30][30],ch;
	while(t--){
		cin>>r>>c;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cin>>str[i][j];
			}
		}
		
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(str[i][j]!='?'){
					ch=str[i][j];
					for(int k=i-1;k>=0;k--){
						if(str[k][j]=='?'){
							str[k][j]=ch;
							x=k;
						}
						else
						break;
					}
					for(int k=i+1;k<r;k++){
						if(str[k][j]=='?'){
							str[k][j]=ch;
							x=k;
						}
						else
						break;
					}
				}
			}
		}
		
		if(str[0][0]=='?'){
			for(int j=0;j<c;j++){
				if(str[0][j]!='?'){
					for(int l=j-1;l>=0;l--){
						for(int i=0;i<r;i++){
							str[i][l]=str[i][l+1];
						}
					}
					x=j;
					break;
				}
			}
			for(int j=x+1;j<c;j++){
				if(str[0][j]=='?'){
					for(int l=0;l<r;l++){
						str[l][j]=str[l][j-1];
					}
				}
			}
		}
		
		for(int j=0;j<c;j++){
			if(str[0][j]=='?'){
				for(int l=0;l<r;l++){
					str[l][j]=str[l][j-1];
				}
			}
		}
		
		cout<<"Case #"<<st<<":"<<endl;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout<<str[i][j];
			}
			cout<<endl;
		}
		st++;
	}
	return 0;
}
