#include <iostream>
#include <map>

using namespace std;

int main(){
	int t;
	cin >> t;
	int x=1;
	while(t--){
		long long n;
		int k;
		cin >> n >> k;
		map<long long,int> M;
		M[n]=1;
		long long ant;
		while(k>0){
			int key=M.rbegin()->first;
			key--;
			int count=M.rbegin()->second;
			k-=count;
			if(key&1){
				if(M.find(key/2)!=M.end()){
					M[key/2]+=count;
				} else {
					M[key/2]=count;
				}
				if(M.find(key/2+1)!=M.end()){
					M[key/2+1]+=count;
				} else {
					M[key/2+1]=count;
				}
			} else {
				if(M.find(key/2)!=M.end()){
					M[key/2]+=count*2;
				} else {
					M[key/2]=count*2;
				}
			}
			ant=key;
			M.erase(key+1);
		}
		cout << "Case #" << x << ": ";
		cout << (ant+1)/2 << " ";
		cout << ant/2 ;
		cout << endl;
		x++;
	}
	return 0;
}
