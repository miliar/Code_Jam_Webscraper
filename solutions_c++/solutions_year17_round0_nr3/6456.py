#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	ll;
typedef unsigned long long int ULL;

#define loop(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
//Works for forward as well as backward iteration


FILE *fin = freopen("A-large.in","r",stdin);
FILE *fout = freopen("A-large-out.txt","w",stdout);
//const int N = int(1e5)+10;
const int LOGN = 20;
const int INF = int(1e9);

ll mn,mx;

void f(ll n,ll k){

	if(k==1){
		mx = n/2;
		mn = (n-1)/2;
		return;
	}
	k--;

	if(k%2){
		f(n/2,(k+1)/2);
	}
	else{
		f((n-1)/2,k/2);
	}
}

void solve(){

	ll n,k;
	cin>>n>>k;
	f(n,k);
	cout<<mx<<" "<<mn<<endl;
}

int main()
{
	int t;
	cin>>t;
	loop(i,1,t+1){
		cout<<"Case #"<<i<<": ";
		solve();
	}

    return 0;
}
