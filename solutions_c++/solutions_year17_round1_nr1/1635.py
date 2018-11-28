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
#include <algorithm>
#include <iomanip>

using namespace std;

#define mp make_pair
#define pb push_back

int main() {

    std::ios::sync_with_stdio(false);

    int tc;

    cin>>tc;

    for (int t=0; t<tc; t++){

    	int n, m;
    	char niza[26][26];

    	cin>>n>>m;

    	for (int i=0; i<n; i++){
    		for (int j=0; j<m; j++){
    			cin>>niza[i][j];
    		}
    	}

    	for (int i=0; i<n; i++){
    		for (int j=0; j<m; j++){
    			if (niza[i][j] != '?'){
    				for (int z=j-1; z>=0; z--){
    					if (niza[i][z] == '?')
    						niza[i][z] = niza[i][j];
    					else
    						break;
    				}
    				for (int z=j+1; z<m; z++){
    					if (niza[i][z] == '?')
    						niza[i][z] = niza[i][j];
    					else
    						break;
    				}
    			}
    		}
    	}

    	for (int i=1; i<n; i++){
            for (int j=0; j<m; j++){
                if (niza[i][j] == '?')
                    niza[i][j] = niza[i-1][j];
            }
    	}

    	for (int i=n-2; i>=0; i--){
            for (int j=0; j<m; j++){
                if (niza[i][j] == '?')
                    niza[i][j] = niza[i+1][j];
            }
    	}

    	cout<<"Case #"<<t+1<<":"<<"\n";

    	for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                cout<<niza[i][j];
            }
            cout<<"\n";
    	}

    }

    return 0;
}
