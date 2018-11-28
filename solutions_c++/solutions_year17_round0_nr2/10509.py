#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
using namespace std;

void fill(int n,vector<int>& A){
	if(n==0) return;
	else{
		fill(n/10,A);
		A.push_back(n%10);
	}
}
int printvec(vector<int> A){
	int i=0;
	for(;i<A.size()-1;i++){
		if(A[i] >= A[i+1]) break;
	}
	return i;
}

int main() {
	// your code goes here
	int t,n,ans,f;
	vector<int> A;
	cin >> t;
	for(int cas=1;cas<=t;cas++){
		cin >> n;
		ans=0;f=0;
		fill(n,A);
		int index = printvec(A);
		int temp = index;
		//cout << "Case #" <<cas <<" temp : " << temp <<endl;
		while(index!= A.size()-1 && A[index]==A[index+1]) index++;
		if(index!= A.size()-1 && A[index]>A[index+1]) index = temp;
		else{
			while(index!=A.size()-1 && A[index]<A[index+1]) index++;
		}
		//cout << "Case #" <<cas <<" index : " << index <<endl;
		if(A.size() == 1 || index == A.size()-1 || f){
			cout << "Case #" <<cas <<": " << n <<endl;
			A.clear();
			continue;
		}
		for(int j=0;j<A.size();j++){
			ans = ans*10 + (j>index ? 0:A[j]);
		}
		cout << "Case #" <<cas <<": " << ans-1 <<endl;
		A.clear();
	}
	return 0;
}