#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	int j;
	for(j=0;j<t;j++)
	{
		vector <int> ans;
		int N;
		int i,k;
		cin>>N;
		ans.push_back(N);
		
		int y,z;
		cin>>k;
		for(i=0;i<k;i++){
			int x,ind=0;
				x = ans[0];
				ind++;
			x--;
			y = ceil((float)x/2);
			z = x/2;
		
			ans.push_back(y);
			ans.push_back(z);
			int ww;
			ans.erase(ans.begin());
			
			sort(ans.begin(),ans.end());
			reverse(ans.begin(),ans.end());
		}
		int a1= ans.size()-1,a2 = a1-1;
		printf("Case #%d: %d %d\n",j+1,y,z);
		ans.erase(ans.begin(),ans.begin()+ans.size()-1);
	}
	return 0;
}