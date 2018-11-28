#include <iostream>
#include <vector>
//#include <string>
using namespace std;

int main() {

	int t, j;
	int last;
	vector<int> v;
	long long int n;
	cin>>t;
	for(int i = 1;i<=t;++i){
		cin>>n;
		cout<<"Case #"<<i<<": ";
		while(n > 0){
			v.push_back(n%10);
			n = n/10;
		}
		int s = v.size();
		last = -1;
		for(j = 0;j<s-1;++j){
			if(v[j] >= v[j+1] && (v[j] == 0 || v[j+1] == 0)){
				v[j] = 9;
			}else if(v[j] < v[j+1]){
				v[j] = 9;
				--v[j+1];
				last = j;
			}
		}
		
		for(j = last;j>=0;--j)
			v[j] = 9;
		if(v[s-1] != 0)
			cout<<v[s-1];
		for(j = s-2;j>=0;--j)
			cout<<v[j];
		cout<<endl;//<<last<<endl;
		v.clear();
	}
	return 0;
}