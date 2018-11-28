




#include <iostream>
#include <vector>
//#include <string>
using namespace std;
 
int main() {
 
	int t, j;
	int last;
	v1ector<int> v1;
	long long int n;
	cin>>t;
	for(int i = 1;i<=t;++i){
		cin>>n;
		cout<<"Case #"<<i<<": ";
		while(n > 0){
			v1.push_back(n%10);
			n = n/10;
		}
		int s = v1.size();
		last = -1;
		for(j = 0;j<s-1;++j){
			if(v1[j] >= v1[j+1] && (v1[j] == 0 || v1[j+1] == 0)){
				v1[j] = 9;
			}else if(v1[j] < v1[j+1]){
				v1[j] = 9;
				--v1[j+1];
				last = j;
			}
		}
 
		for(j = last;j>=0;--j)
			v1[j] = 9;
		if(v1[s-1] != 0)
			cout<<v1[s-1];
		for(j = s-2;j>=0;--j)
			cout<<v1[j];
		cout<<endl;//<<last<<endl;
		v1.clear();
	}
	return 0;
}