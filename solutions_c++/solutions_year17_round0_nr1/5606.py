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
	int st,t,k,cnt;
	sn(t);
	st=1;
	string str;
	while(t--){
		cin>>str;
		sn(k);
		//cin>>str>>k;
		cnt=0;
		for(int i=0;i<str.length()-k+1;i++){
			if(str[i]=='-'){
				for(int j=i;j<i+k;j++){
					if(str[j]=='+')
					str[j]='-';
					else
					str[j]='+';
				}
				cnt++;
			}
		}
		int flag=0;
		//cout<<str;
		for(int i=0;i<str.length();i++){
			if(str[i]=='-')
			flag=1;
		}
		if(flag==1){
			cout<<"Case #"<<st<<": IMPOSSIBLE"<<endl;
		}
		else{
			cout<<"Case #"<<st<<": "<<cnt<<endl;
		}
		st++;
	}
	return 0;
}
