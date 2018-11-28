#include <bits/stdc++.h>
#define ll long long
#define mp make_pair
#define pp pair<int,int>
#define ppi pair <int,int >

using namespace std ;

pp result (long long int n,long long k){
	if (k==1){
				if (n & 1)
				{
					return mp(n/2,n/2);
				}
				else
					return mp (n/2,n/2-1);
	}
	if (!(n&1) && (k & 1)){
		return result (n/2-1,k/2);
	}
	else
		return result (n/2,k/2);




}

int main (){
	freopen ("in","r",stdin);
	freopen ("out","w",stdout);

		int t;
		cin>>t;
		long long n ,k ;
		int rep(0);
		while (t--){
		rep++;
				cin>>n>>k;
				pp x;
				x=result (n,k);
				  cout<<"Case #"<<rep<<": ";
				  cout<<x.first<<" "<<x.second<<endl;



		}



}
