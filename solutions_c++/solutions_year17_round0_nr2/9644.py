#include <bits/stdc++.h>
using namespace std;
 
int main() {
 
	int t;
	int last;
	vector<int> v;
	long long int n;
	scanf("%d",&t);
	for(int z = 1;z<=t;z++){
	    int e;
		scanf("%lld",&n);
		cout<<"Case #"<<z<<": ";
		while(n > 0){
			v.push_back(n%10);
			n = n/10;
		}
		int l = v.size();
		e = -1;
		for(int i = 0;i<l-1;i++){
			if(v[i] >= v[i+1] && (v[i] == 0 || v[i+1] == 0)){
				v[i] = 9;
			}else if(v[i] < v[i+1]){
				v[i] = 9;
				--v[i+1];
				e = i;
			}
		}
 
		for(int i = e;i>=0;i--)
			v[i] = 9;
		if(v[l-1] != 0)
			printf("%d",v[l-1]);
		for(int i = l-2;i>=0;i--)
			printf("%d",v[i]);
		printf("\n");//<<last<<endl;
		v.clear();
	}
	return 0;
}
