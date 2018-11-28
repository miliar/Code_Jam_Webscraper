
#include <iostream>
#include <vector>
#include <utility>
using namespace std;
typedef long long ll;
vector< pair<ll, ll> > v;

int no_cases;
ll y, z;



int main(){
	cin>>no_cases;
	for (int caseID=1; caseID<=no_cases; caseID++){
		ll n, k;
		v.clear();
		cin>>n>>k; 
		pair<ll, ll> pr(n, 1);
		v.push_back(pr);
		ll i=0;
		while (i<k){
			ll value=v[0].first;

			ll number=v[0].second;
			
			
			if (i+number>=k){
				if (value%2==0){
					y=(value-1)/2+1;
					z=(value-1)/2;
				}
				else{
					y=(value-1)/2;
					z=(value-1)/2;
				}
				break;
			}

			if (value%2==0){

				ll l_d=(value-1)/2+1;
				ll s_d=(value-1)/2;

				if (v[v.size()-1].first==l_d){
					v[v.size()-1].second+=number;
				}
				else{
					pair<ll, ll> pr(l_d, number);
					v.push_back(pr);
				}

				if (v[v.size()-1].first==s_d){
					v[v.size()-1].second+=number;
				}
				else{
					pair<ll, ll> pr(s_d, number);
					v.push_back(pr);
				}
			}
			else{
				ll l_d=(value-1)/2;
				if (v[v.size()-1].first==l_d){
					v[v.size()-1].second+=2*number;
				}
				else{
					pair<ll, ll> pr(l_d, 2*number);
					v.push_back(pr);
				}
			}


			
			v.erase(v.begin()+0);

			i=i+number;
			//cout<<i<<endl;

		}

		cout<<"Case #"<<caseID<<": "<<y<<" "<<z<<endl;
	}
}