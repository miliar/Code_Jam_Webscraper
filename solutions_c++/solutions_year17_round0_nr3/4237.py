#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <algorithm>
using namespace std;
bool wayToSort(int i, int j) { return i > j; }
int main() {

    freopen("C-small-2-attempt1.in","r",stdin);
    freopen("c.out","w",stdout);

	int t;
	cin>>t;

	long long n,k;
	long long temp;

	for(int i = 1; i <= t; i++){
	    cin>>n>>k;
	    vector<long long> tree;
	    tree.push_back(n);
	    for(int j = 0; j<=k; j++){
	        if(tree[j] % 2 == 0){
	            tree.insert( tree.begin() + (j*2 + 1), tree[j]/2 );
	            tree.insert( tree.begin() + (j*2 + 2), tree[j]/2 - 1);
	        }
	        else{
	            tree.insert( tree.begin() + (j*2 + 1), tree[j]/2 );
	            tree.insert( tree.begin() + (j*2 + 2), tree[j]/2 );
	        }
	    }
        /**int l;
	    for (int j = 0; j < tree.size(); j++){
            l = j;
		while (l > 0 && tree[l] > tree[l-1]){
			  temp = tree[l];
			  tree[l] = tree[l-1];
			  tree[l-1] = temp;
			  l--;
			  }
		}**/

		sort(tree.begin(), tree.end(), wayToSort);

        if(tree[k - 1]%2 == 0){
            cout<<"Case #"<<i<<": "<<tree[k - 1]/2<<" "<<tree[k - 1]/2 - 1<<endl;
        }
        else{
            cout<<"Case #"<<i<<": "<<tree[k - 1]/2<<" "<<tree[k - 1]/2<<endl;
        }
	}

	return 0;
}
