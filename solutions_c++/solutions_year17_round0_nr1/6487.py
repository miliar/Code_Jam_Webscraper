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
    long long int T;
    cin >> T;

    int K;
    string s;

    int j=0;

    while(T--){
    	j++;
    	cin >> s;
    	cin >> K;
    	int count=0;

    	for (int i =0; i <= s.length()-K; i++){
    		if(s[i] == '-')
    		{
    			for(int j=0; j < K; j++){
    				s[i+j] = s[i+j] == '-'?'+':'-';
    			}
    			count++;
    		}
    	}
    	int isImpossible=0;
    	for (int i = s.length()-1; i > s.length()-K; i-- ){
    		if(s[i] == '-'){
    			isImpossible =1;
    			break;
    		}
    	}


    	cout <<"Case #"<<j<<": ";
    	if(isImpossible)
    		cout<<"IMPOSSIBLE"<<endl;
    	else
    		cout<<count<<endl;

    }
    return 0;
}
