#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <iostream>
#include <vector>
#include <cstring>
#include <stack>

using namespace std;

int main(){
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;test++){
		long long n;
		scanf("%lld",&n);
		vector<long long> v;
		while(n>0){
			v.push_back(n%10);
			n/=10;
		}
		reverse(v.begin(),v.end());
		
		for(int i=0;i+1<v.size();i++)
			if(v[i]>v[i+1]){
				int curr = v[i];
				int j = i;
				while(j-1>=0&&v[j-1]==curr) v[j--]=9;
				v[j]--;
				j=i+1;
				while(j<v.size()) v[j++]=9;
				break;
			}

		long long result = 0;
		for(int i=0;i<v.size();i++)
			result = result * 10 + v[i];
		
		printf("Case #%d: ",test);
		printf("%lld\n",result);
	}
	return 0;
}