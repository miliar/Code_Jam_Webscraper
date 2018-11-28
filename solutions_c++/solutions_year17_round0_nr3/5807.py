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
	int t,st=1;
	sn(t);
	int n,k,l,r,x,y,f,mx,my,maxx,minn,pos,v1,v2;
	while(t--){
		cin>>n>>k;
		bool arr[n+5]={false};
		int a[n+5],b[n+5];
		
		v1=v2=0;
		for(int i=0;i<n;i++){
			a[i]=i;
		}
		
		for(int i=0;i<n;i++){
			b[i]=n-1-i;
		}
		
		l=0,r=n-1;f=0;
		maxx=-1;minn=-1;
		while(k--){
			//cout<<"hi";
			maxx=-1;minn=-1;f=0;
			for(int i=0;i<n;i++){
				if(arr[i]==false){
					x=a[i];
					y=b[i];
					mx=min(x,y);
					//cout<<mx<<"mx ";
					if(mx>minn){
						pos=i;
						minn=mx;
						if(f==0){
							maxx=mx;
							f=1;
						}
					}
					else if(mx==minn){
						//cout<<minn;
						//cout<<"hello";
						my=max(x,y);
						if(my>maxx){
							pos=i;
							maxx=my;
						}
					}
				}
			}
			//cout<<pos<<"pos";
			arr[pos]=true;
			a[pos]=-1;
			b[pos]=-1;
			for(int i=pos-1;i>=0;i--){
				if(arr[i]==true)
				break;
				b[i]=pos-i-1;
			}
			for(int i=pos+1;i<n;i++){
				if(arr[i]==true)
				break;
				a[i]=i-pos-1;
			}
			/*for(int i=0;i<n;i++)
			cout<<a[i];
			cout<<endl;
			for(int i=0;i<n;i++)
			cout<<b[i];
			cout<<endl;
		*/}
		//for(int i=0;i<n;i++)
		//cout<<arr[i];
		//cout<<endl;
		for(int i=pos-1;i>=0;i--){
			if(arr[i]==true)
			break;
			v1++;
		}
		for(int i=pos+1;i<n;i++){
			if(arr[i]==true)
			break;
			v2++;
		}
		cout<<"Case #"<<st<<": "<<max(v1,v2)<<" "<<min(v1,v2)<<endl;
		st++;
	}
	return 0;
}
