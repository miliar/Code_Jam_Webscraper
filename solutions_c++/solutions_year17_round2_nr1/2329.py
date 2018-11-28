
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
		// My code

		int d,n;
		cin>>d>>n;
		
		double maxi=INT_MIN;
		for (int i=0;i<n;i++){
			int k,s;
			cin>>k>>s;
			maxi=max(maxi,(d-k)/(s*1.0));
		}
		std::cout << std::fixed;
		cout << std::setprecision(6) << d/maxi << endl;

	}
	
	return 0;
}
