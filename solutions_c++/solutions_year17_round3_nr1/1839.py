#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <time.h>
#include <bits/stdc++.h>


using namespace std;

struct tuple{
	long long r;
	long long h;
};
int acompare(tuple a, tuple b){
	return (a.r * a.h > b.r * b.h);
}
int ccompare(tuple a, tuple b){
	return (a.r > b.r);
}
int bcompare(tuple a, tuple b){
	return (a.r < b.r || (a.r == b.r and a.h > b.h));
}

int main(){
	cout.precision(10);
	int t;
	cin >>t ;
	int i;
	for(i=0;i<t;i++){
		int n,k,j,l;
		double pi = 3.1415926535897;
		cin >> n >> k;
		long long r[n],h[n];
		tuple prod[n];
		for(j=0;j<n;j++){
			cin >> r[j] >> h[j];
			prod[j].r = r[j];
			prod[j].h = h[j];
		}
		double result = 0;
		double temp = 0;
		sort(prod,prod+n,ccompare);
		for(j=0;j<=n-k;j++){
			temp = pi * ((double)prod[j].r)*((double)prod[j].r);
			//cout << "yes";
			sort(prod+j+1,prod+n,acompare);
			for(l=j;l<j+k;l++)temp += 2*pi*(double)prod[l].r*(double)prod[l].h;
			result = max(result, temp);
			sort(prod+j+1,prod+n,ccompare);
		}
		printf("Case #%d: %lf\n", i+1,result);
		/*tuple chosen[k];
		for(j=0;j<k;j++)chosen[j] = prod[n-j-1];
		sort(chosen,chosen+k,bcompare);
		//for(j=0;j<k;j++)cout << chosen[j].h << endl;
		int m = 0;
		double result,temp=0; 
		for(j=0;j<k-1;j++)temp+= 2*pi*(double)chosen[j].r*(double)chosen[j].h;
		//cout << temp << endl;
		double curr = pi * ((double)chosen[k-1].r)*((double)chosen[k-1].r) + 2*pi * (double)chosen[k-1].r * (double)chosen[k-1].h;
		//cout << curr << endl;

		for(j=0;j<n-k;j++){
			if(k>1)
			if((pi * ((double)prod[j].r)*((double)prod[j].r) + 2*pi * (double)prod[j].r * (double)prod[j].h)> curr and prod[j].r >= chosen[k-2].r )curr = pi * ((double)prod[j].r)*((double)prod[j].r) + 2*pi * (double)prod[j].r * (double)prod[j].h;
			else{
				if((pi * ((double)prod[j].r)*((double)prod[j].r) + 2*pi * (double)prod[j].r * (double)prod[j].h)> curr ){
					curr =  pi * ((double)prod[j].r)*((double)prod[j].r) + 2*pi * (double)prod[j].r * (double)prod[j].h;
				}
			}
		}
		result = curr + temp;
		printf("Case #%d: %lf\n", i+1,result);*/
		//cout << "Case #" << i+1 << ": " << result << endl;
	}
}