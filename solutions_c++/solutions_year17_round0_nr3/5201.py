#include <bits/stdc++.h>

using namespace std;

int main(){

	freopen("input3.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	cin >> t;
	for(int z=1;z<=t;z++){
		int n,k;
		int val=0;
		cin >> n >> k;
		queue <int> q;
		vector <int> sarr;
		q.push(n);
		int v=n;
		while(!q.empty()){
			v = q.front();
			sarr.push_back(v);
			q.pop();
			if(v==0)continue;
			if(v%2==0){
				if(v==2||v==0)continue;
				q.push(v/2-1);
				q.push(v/2);
			}
			else{
				if(v==1)continue;
				q.push(v/2);
				q.push(v/2);
			}
		}
		sort(sarr.rbegin(),sarr.rend());
		if(k==1){
			cout << "Case #" << z << ": ";
			if(n%2==0){
				cout << n/2 << " " <<  max(n/2-1,0) << endl;
			} 
			else{
				cout << n/2 <<  " " << n/2 << endl;	
			}
		}
		else if(k>=sarr.size()){
			cout << "Case #" << z << ": 0 0\n";
		}
		else{
			cout << "Case #" << z << ": ";
			if(sarr[k-1]%2==0){
				cout << sarr[k-1]/2 << " " <<max(sarr[k-1]/2-1,0) << endl;	
			}
			else{
				cout << sarr[k-1]/2 <<" "<< sarr[k-1]/2 << endl;	
			}
		}


		
		

	}
}