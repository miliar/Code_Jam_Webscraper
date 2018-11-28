#include<bits/stdc++.h>
#define ll long long 
#define pb push_back
#define mp make_pair

using namespace std;

multiset<ll,greater<ll> >st;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t,n,k,i,j,cc,x,y,z;
	cin>>t;
	for(cc=1;cc<=t;cc++){
		cout<<"Case #"<<cc<<": ";
		cin>>n>>k;
		st.clear();
		st.insert(n);
		for(i=1;i<=k-1;i++){
			z=*st.begin();
			if(z%2!=0){
				x=z/2;
				y=x;
			}
			else{
				x=z/2;
				y=x-1;
			}
			st.erase(st.begin());
			st.insert(x);
			st.insert(y);
		}		
		z=*st.begin();
		if(z%2!=0){
                	x=z/2;
                        y=x;
                }
                else{
                        x=z/2;
                        y=x-1;
                }
		cout<<x<<" "<<y<<endl;
	}


	return 0;
}
