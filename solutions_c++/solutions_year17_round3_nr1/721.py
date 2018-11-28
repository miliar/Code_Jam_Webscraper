
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <climits>
#include <iomanip> 

#define ll long long
 
using namespace std;

int main(){
	int t;
	cin>>t;
	int a=0;
	while (t--){
		a++;
		cout<<"Case #"<<a<<": ";
		int n,k;
		cin>>n>>k;
		vector<pair<ll,ll> > dim(n);
		for (int i=0;i<n;i++){
			int r,h;
			cin>>r>>h;
			dim[i]=make_pair(r,h);
		}
		
		long long maxar=0;
		for (int i=0;i<n;i++){
			vector<ll> temp;
			long long base=dim[i].first*dim[i].first+2*dim[i].first*dim[i].second;
			
			for (int j=0;j<n;j++){
				if (i==j){
					continue;
				}
				ll tempar=2*dim[j].first*dim[j].second;
				temp.push_back(tempar);

			}
			sort(temp.begin(),temp.end());
			ll ans=0;
			for (int j=n-2;j>=n-2-k+2;j--){
				ans+=temp[j];
			}
			ans+=base;
			if (ans>maxar){
				maxar=ans;
			}
			
		}
		

		double final=maxar*3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481;
		std::cout << std::fixed;
  		std::cout << std::setprecision(8) << final<<endl;



		// My code

		

	}
	
	return 0;
}
