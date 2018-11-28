//============================================================================
// Name        : Bathroom.cpp
// Author      : Fezo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;
const int MaxN = 1005;
int T,n,k;
int L[MaxN],R[MaxN];
bool empty[MaxN];
int main() {
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	cin >> T;
	int t=1;
	while(T--){
		cin >> n >> k;
		for(int i=0;i<n;i++){
			L[i] = i;
			R[i] = n-i-1;
			empty[i] = true;
		}

		int lResult=0,rResult=0;
		while(k--){
			int maxi=-1,selectedStall=-1;
			for(int i=0;i<n;i++){
				if(!empty[i]) continue;
				int mini = min(L[i],R[i]);
				if(mini>maxi){
					selectedStall = i;
					maxi = mini;
				}else if(mini==maxi){
					int m1 = max(L[i],R[i]);
					int m2 = max(L[selectedStall],R[selectedStall]);
					if(m1>m2){
						selectedStall = i;
					}
				}
			}
			empty[selectedStall] = false;
			lResult = L[selectedStall];
			rResult = R[selectedStall];
			int prev = -1;
			for(int i=0;i<n;i++){
				L[i] = max(0,i-prev-1);
				if(!empty[i]){
					prev = i;
				}
			}
			prev = n;
			for(int i=n-1;i>=0;i--){
				R[i] = max(0,abs(i-prev)-1);
				if(!empty[i]){
					prev = i;
				}
			}
			/*
			for(int i=0;i<n;i++){
				cout << L[i] << " " << R[i] << endl;
			}
			for(int i=0;i<n;i++){
				cout << empty[i] << " ";
			}
			cout << endl;
			*/
		}
		cout <<"Case #" << t << ": " << max(lResult,rResult) << " "  << min(lResult,rResult)  << endl;
		t++;
	}


	return 0;
}
