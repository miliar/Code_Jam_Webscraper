/*input
*/

#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007
#define pb push_back
#define ll long long

ll num[20];ll len;

void adjust(ll l){
	if(l==len-2)
		return;
	ll i,j,prev;
	i=len-1;
	prev=num[i];
	i--;
	while(num[i]>=prev&&i>l){
		prev=num[i];
		i--;
	}
	if(i==l)
		return;
	j=i+1;
	while(i>l){
		num[i]=9;
		i--;
	}
	num[j]--; //Borrow
	j--;
	adjust(j);
	return;
}

int main(){
	ios_base::sync_with_stdio(false);cin.tie(0);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ll t,n,i,j,k,prev,ans;
	cin>>t;
	for(k=1;k<=t;k++){
		cin>>n;
		memset(num,0,sizeof(num));i=0;
		while(n){
			num[i++]=n%10;
			n/=10;
		}
		len=i;
		adjust(-1); //adjusts the array b/w the limits (-1,len-1];
		ans=0;i=19;
		while(num[i]==0)
			i--;
		while(i>=0){
			ans=ans*10+num[i];
			i--;
		}
		cout<<"Case #"<<k<<": "<<ans<<"\n";
	}
	return 0;
}
