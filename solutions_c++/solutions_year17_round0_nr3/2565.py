#include <iostream>
#include <map>
#include <cstdio>

using namespace std;

int main(){
	freopen("C-large.in", "r", stdin);
	freopen("output-1.txt", "w", stdout);
	int t;
	cin>>t;
	for(int q = 1; q <= t; q++){
		cout<<"Case #"<<q<<": ";
		long long int n,k;
		cin>>n>>k;
		long long int l = k+1;
		int i = 0;
		while(l > 1){
			l = l/2;
			i++;
		}
		map<long long int, long long int>::iterator it;
		map<long long int, long long int> a[i+3];
		a[1][n] = 1; 
		for(int j = 2; j <= i+1; j++){
			for(it = a[j-1].begin(); it != a[j-1].end(); it++){
				if(it->first %2 == 1){
					a[j][(it->first)/2] += 2*(it->second);
				}else{
					a[j][(it->first)/2] += it->second;
					a[j][(it->first)/2 - 1] += it->second;
				}
			}
		}
		l = 1;
		l = ((l<<i) - 1);
		l = k - l;
		if(l == 0){
			it = a[i].begin();
			if(it->first <= 0){
				cout<<0<<" "<<0<<endl;
			}else{
				if(it->first%2 == 1){
					cout<<it->first/2 <<" "<<it->first/2<<endl;
				}else{
					cout<<(it->first/2)<<" "<<(it->first/2 - 1)<<endl;
				}
			}
		}else{
			long long int ans;
			map<long long int, long long int>::reverse_iterator rit;
			for(rit = a[i+1].rbegin(); rit != a[i+1].rend(); rit++){
				if(l > rit->second){
					l -= rit->second;
				}else{
					ans = rit->first;
					break;
				}
			}
			if(ans <= 1){
				cout<<0<<" "<<0<<endl;
			}else{
				if(ans%2 == 1){
					cout<<ans/2<<" "<<ans/2<<endl;
				}else{
					cout<<ans/2<<" "<<ans/2 - 1<<endl;
				}
			}
		}
	}
}