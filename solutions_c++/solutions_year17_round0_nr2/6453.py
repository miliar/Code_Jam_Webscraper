//============================================================================
// Name        : tidynumbers.cpp
// Author      : Ajay Kedare
// Version     :
// Copyright   : Your copyright notice
// Description : Tidy Number calculation
//============================================================================

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    long long int T, N;
    cin >> T;


    int j=0;
    while(T--){
    	j++;
    	cin >> N;
    	long long int n = N;

    	vector<int> arr;
    	while(n>0){
    		arr.push_back(n%10);
    		n/=10;
    	}
    	std::reverse(arr.begin(),arr.end());

    	for (int i=arr.size()-1; i >= 0; i-- ) {
    		if (arr[i] < arr[i-1] || arr[i] == 0){
    			int k=i+1;

    			arr[i] = 9;
    			while(arr[k]<arr[k-1]) {
    				arr[k] = 9;
    				k++;
    			}
    			if (arr[i-1]-1 == -1){
    				arr[i-1] = 0;
    			} else if(arr[i-1]-1 == 0){
    				if(i == 1 )
    					arr.erase(arr.begin()+i-1);
    				else
    					arr[i-1] = 0;
    			} else
    				arr[i-1]-=1;
    		}
    	}

    	cout << "Case #"<<j<<": ";
    	for (int i =0; i < arr.size(); i++ ){
    		cout << arr[i];
    	}
    	cout<<endl;
    }
    return 0;
}
