/* Segment tree */

#include <iostream>
#include <vector>
#include <utility>
#include <stdio.h>
#include <cstring>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <fstream>

using namespace std;

#define mp make_pair
#define pb push_back

int main() {

    std::ios::sync_with_stdio(false);

    int n;
    cin>>n;

    for (int t=0; t<n; t++){
    	long long broj, temp, pamti;
    	vector <int> vec;

    	cin>>broj;
    	temp = broj;

    	while (temp > 0){
    		vec.pb(temp % 10);
    		temp = temp / 10;
    	}

    	bool sc = false; //special case
    	reverse(vec.begin(), vec.end());
    	for (int i=1; i<vec.size(); i++){
    		if (vec[i] < vec[i-1]){
                pamti = i;
    			for (int j=i-1; j>=0; j--){
    				vec[j] --;
    				if ((j == 0) && (vec[j] == 0)){
    					sc = true;
    					break;
    				}
    				else if ((j == 0) && (vec[j] != 0)){
    				    pamti = 1;
    					break;
    				}
    				else if (vec[j] >= vec[j-1]){
    					pamti = j+1;
    					break;
    				}
    			}
    			for (int j=pamti; j<vec.size(); j++){
    				vec[j] = 9;
    			}
    			break;
    		}
    	}

    	cout<<"Case #"<<t+1<<": ";
    	if (sc == true){
    		for (int i=0; i<vec.size()-1; i++){
    			cout<<"9";
    		}
    		cout<<"\n";
    	}
    	else{
    		for (int i=0; i<vec.size(); i++){
    			cout<<vec[i];
    		}
    		cout<<"\n";
    	}
    }

    return 0;
}
