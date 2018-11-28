
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

#define ll long long
 
using namespace std;

int main(){
	int t;
	cin>>t;
	int a=0;
	while (t--){
		a++;
		cout<<"Case #"<<a<<": ";
		int n,p;
		cin>>n>>p;
		int req[60];
		for (int i=0;i<n;i++){
			cin>>req[i];
		}
		int qty[60][60];
		for (int i=0;i<n;i++){
			for (int j=0;j<p;j++){
				cin>>qty[i][j];
			}
		}
		for (int i=0;i<n;i++){
			sort(qty[i],qty[i]+p);
		}
		for (int i=0;i<n;i++){
			qty[i][p]=0;
		}
		int maxi=0,kits=0;
		int servings[60]={0};
		while (maxi!=p){
			//cout<<maxi<<endl;
			int dfs;
			//cin>>dfs;
			int mini=INT_MAX;
			int x;
			for (int i=0;i<n;i++){
				servings[i]=(qty[i][qty[i][p]]/0.9)/req[i];
				if (mini>servings[i]){
					mini=servings[i];
					x=i;
				}
				
			}
			// for (int i=0;i<n;i++){
			// 	cout<<servings[i]<<" ";
			// }
			// cout<<endl;
			int i;
			for (i=0;i<n;i++){
				int requirement=mini*req[i];
				// cout<<mini<<" ";
				// cout<<req[i]<<" ";
				// cout<<requirement<<" "<<endl;
				// int q;
				// cin>>q;

				if (requirement*1.1<qty[i][qty[i][p]]){
					break;
				}
				
			}
			if (i==n){
				//cout<<"hello";
				kits++;
				for (int j=0;j<n;j++){
					qty[j][p]++;
					maxi=max(maxi,qty[j][p]);
				}

			}
			else{
				qty[x][p]++;
				maxi=max(maxi,qty[x][p]);
			}

		}
		cout<<kits;
		// My code

		cout<<endl;

	}
	
	return 0;
}
