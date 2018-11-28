#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin>>t;
	for(int q = 1; q <= t; q++){
		cout<<"Case #"<<q<<": ";
		string a;
		int k;
		cin>>a>>k;
		int l = (int)a.size();
		int arr[l];
		for(int i = 0; i < l; i++){
			if(a[i] == '+'){
				arr[i] = 1;
			}else{
				arr[i] = 0;
			}
		}
		int ans = 0;
		for(int i = 0; i <= l-k; i++){
			if(arr[i] == 0){
				for(int j = 0; j < k; j++){
					arr[i+j] = 1 - arr[i+j];
				}
				ans++;
			}
		}
		bool pos = true;
		for(int i = l-k; i < l; i++){
			if(arr[i] == 0){
				pos = false;
				break;
			}
		}
		if(!pos){
			cout<<"IMPOSSIBLE"<<endl;
		}else{
			cout<<ans<<endl;
		}
	}
}