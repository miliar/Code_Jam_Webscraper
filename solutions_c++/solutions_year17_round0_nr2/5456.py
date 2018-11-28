/*
 * B.cpp
 * Copyright (C) 2017 vishalapr <vishalapr@vishal-Lenovo-G50-70>
 *
 * Distributed under terms of the MIT license.
 */

#include <bits/stdc++.h>
using namespace std;

#define whatis(x) cout << #x << " is " << x << endl;

#define MAX 1000001
#define MOD 1000000007
#define INF 1e18
#define PI 3.14159265359

#define STDSYNC std::ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define swap(VAR1,VAR2) VAR1=VAR1^VAR2;VAR2=VAR1^VAR2;VAR1=VAR1^VAR2

typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<int,int> mii;
typedef map<string,int> msi;
typedef priority_queue < ll , vector < ll > , greater < ll > > minheap;
typedef priority_queue < ll , vector < ll > , less < ll > > maxheap;

int main()
{
    STDSYNC;
    ll t=0,a,b,c,i,j,k,n,m,idx;
    string temp;
    ll set = -1;
    cin >> t;
    for(i=0;i<t;i++){
    	cin >> temp;
	idx = temp.length()-1;
	set = temp.length();
	while(idx>0){
	    if(temp[idx-1]>temp[idx]){
	    	set = idx;
		temp[idx-1] = temp[idx-1] - 1;
		temp[idx] = '9';
	    }
	    idx--;
	}
	ll setx = 0;
	cout << "Case #" << (i+1) << ": ";
	for(j=0;j<temp.length();j++){
		if(temp[j]!='0' || setx==1){
			if(j>=set)
				cout << '9';
			else
				cout << temp[j];
		}
		if(temp[j]!='0'){
			setx=1;
		}
	}
	cout << endl;
    }
    return 0;
}
