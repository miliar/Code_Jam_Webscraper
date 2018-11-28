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

    int n, f, cnt, c;
    string temp;

    cin>>n;

    c = 0;
    while (n){
    	n --;
    	c ++;
    	cnt = 0;
    	cin>>temp>>f;
    	for (int i=0; i<=temp.size()-f; i++){
    		if (temp[i] == '-'){
    			cnt ++;
    			for (int j=i; j<i+f; j++){
    				if (temp[j] == '-')
    					temp[j] = '+';
    				else
    					temp[j] = '-';
    			}
    		}
    	}

    	bool ok = true;
    	for (int i=0; i<temp.size(); i++){
    		if (temp[i] == '-'){
    			cout<<"Case #"<<c<<": "<<"IMPOSSIBLE"<<"\n";
    			ok = false;
    			break;
    		}
    	}
    	if (ok == true)
    		cout<<"Case #"<<c<<": "<<cnt<<"\n";
    }

    return 0;
}
