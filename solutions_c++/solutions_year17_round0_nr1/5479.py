/*
 * A.cpp
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
    ll t=0,a,b,c,i,j,k,n,m;
    cin >> n;
    string strs;
    for(i=0;i<n;i++){
    	cin >> strs;
	cin >> m;
	ll flips = 0;
	ll stas = 0;
	for(j=0;j<strs.length();j++){
		if(strs[j]=='-'){
			flips++;
			for(k=0;k<m;k++){
				if(j+k<strs.length() && strs[j+k]=='-')
					strs[j+k]='+';
				else if(j+k<strs.length())
					strs[j+k]='-';
				else
					stas = 1;
			}
		}
	}
	while(j<strs.length()){
		if(strs[j]=='-'){
			stas = 1;
		}
		j++;
	}
	cout << "Case #" << (i+1) << ": ";
	if(stas == 1)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << flips << endl;
    }
    return 0;
}
