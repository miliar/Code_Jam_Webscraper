/* In The Name Of God */
#include <bits/stdc++.h>

# define xx first
# define yy second
# define pb push_back
# define pp pop_back
# define eps 1e-9

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vint;
bool can(ll num , ll rem , ll x , ll digit){
	while(rem--){
		num = num*10 + digit;
	}
	return (num <= x);
}
ll go(ll num , ll rem, ll x){
	if(rem==0)
		return num;
	int tmp = num%10;
	for(int i=9 ; i>=max(1,tmp) ; i--)
		if(can(num,rem,x,i))
			return go(num*10+i , rem-1 , x);
}
int main(){
	ios_base::sync_with_stdio (0);
	freopen("input.in","r",stdin);
	freopen("input.out","w",stdout);
	int T;cin>>T;
	for(int Case = 1 ; Case <= T ; Case++){
		cout<<"Case #"<<Case<<": ";
		ll x;cin>>x;
		ll tmp = 0;
		for(int i=1 ; i<=(int)log10(x)+1 ; i++)
			tmp = tmp*10 + 1;
		if(tmp > x)
			cout<<(ll)pow(10,(int)log10(x))-1<<endl;
		else{
			cout<<go(0ll,(ll)log10(x)+1,x)<<endl;
		}
	}
	return 0;
}

