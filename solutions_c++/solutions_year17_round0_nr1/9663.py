#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cstring>
using namespace std;
int arr[1001];
int farr[1001];
int getAns(string str,int k){
	memset(arr,0,sizeof arr);
	memset(farr,0,sizeof farr);
	int n = str.length();
	for(int i=0;i<n;i++){
		if(str[i]=='-')
			arr[i]=1;
	}
	int ans =0;
	int flip=0;
	for(int i=0;i<n;i++){
		flip = (farr[i]+flip)%2;
		if(arr[i]!=flip){
			if(i+k-1<=n-1){
				ans++;
				flip = (flip+1)%2;
				if(i+k<n)
				farr[i+k]=1;
			}
			else{
				return 100000;
			}
			//cout<<i<<" "<<ans<<endl;
		}
	}
	return ans;
}

int main() {
	int t;
	cin>>t;
	for(int test =0;test<t;test++){
		string str;
		int k;
		cin>>str>>k;
		string strRev = str;
		reverse(strRev.begin(),strRev.end());
		int ans = min(getAns(str,k), getAns(strRev ,k));
		//int ans = getAns(str,k);
		if(ans == 100000)
			cout<<"Case #"<<test+1<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<test+1<<": "<<ans<<endl;
	}
	return 0;
}