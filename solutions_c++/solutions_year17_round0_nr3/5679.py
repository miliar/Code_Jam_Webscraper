/*
 * C.cpp
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

ll mark[100000];

int main()
{
    STDSYNC;
    ll t=0,a,b,c,i,j,k,l,n,m;
    cin >> t;
    for(i=0;i<t;i++){
    	cin >> n >> k;
	for(j=0;j<n;j++){
		mark[j]=0;
	}
	mark[n] = 1;
	ll ans1 = -1;
	ll ans2 = -1;
	for(j=0;j<k;j++){
		ll bdist = -1;
		ll cdist = -1;
		ll bleft = -1;
		ll bsel = -1;
		for(l=0;l<n;l++){
			if(mark[l]==0 && cdist==-1){
				cdist=1;
				bleft = l;
				if(cdist>bdist){
					bdist = cdist;
					bsel = (bleft+l)/2;
					ans1 = bleft;
					ans2 = l;
				}
			}
			else if(mark[l]==0){
				cdist++;
				if(cdist>bdist){
					bdist = cdist;
					bsel = (bleft+l)/2;
					ans1 = bleft;
					ans2 = l;
				}
			}
			else if(mark[l]==1){
				cdist = -1;
			}
		}
		mark[bsel]=1;
	}
	ll tempsel = (ans1+ans2)/2;
	cout << "Case #" << (i+1) << ": ";
	cout << max(tempsel-ans1,ans2-tempsel) << " ";
	cout << min(tempsel-ans1,ans2-tempsel) << endl;
    }
    return 0;
}
