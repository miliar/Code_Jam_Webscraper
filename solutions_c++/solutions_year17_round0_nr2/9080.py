/*
author-Prakhar Agrawal
handle-prakhar3agrwal
*/

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
int i,j,k,n,m,s,t,ans;
string x,y;
int indexToBeDecremented(string x){
	int l = x.length();
	int increase = 0;
	for(int i = 1; i<l ;i++){
		if(x[i]>x[i-1])
		increase = i;
		else if(x[i]<x[i-1])
		return increase + 1000;
	}
	return increase;
}

string trim(string x){
	if(x[0] != '0')
	return x;
	return x.substr(1);
}
int main()
{
cin>>t;
int k = 0;
while(t--){
	k++;
	cin>>x;
	n = x.length();
	j = indexToBeDecremented(x);
	if(j<1000){
		cout<<"Case #" << k << ": " << x<< endl;
		continue;
	}
	j = j-1000;
	x[j]--;
	for(i=j+1;i<n;i++)
	x[i] = '9';
	cout<<"Case #" << k << ": " << trim(x)<< endl;
}
}

