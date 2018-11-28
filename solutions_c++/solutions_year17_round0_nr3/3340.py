#include <bits/stdc++.h>
using namespace std ;

pair<long long ,long long >  rep (long long int n,long long int p){
	if (p==1){
				if (n%2==1)
				{
					return make_pair(n/2,n/2);
				}
				else
					return make_pair (n/2,n/2-1);
	}
	if (n%2==0 && (p%2==1)){
		return rep (n/2-1,p/2);
	}
	else
		return rep(n/2,p/2);
}

int main (){
        freopen ("C-large.in","r",stdin);
        freopen ("out","w",stdout);
		long long int h;
		cin>>h;
		int cnt(1);
		while (h--){
		long long n ,k ;

				cin>>n>>k;
				pair<long long ,long long > chta7;
				chta7 =rep(n,k);
				  cout<<"Case #"<<cnt<<": ";
				  cout<<chta7.first<<" "<<chta7.second<<endl;
                    cnt++;


		}



}
