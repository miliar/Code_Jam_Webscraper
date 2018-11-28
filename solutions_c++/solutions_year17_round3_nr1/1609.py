#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
double pi = 3.14159265358979323846;

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for(int z = 1; z <= t; z++){
		
		int n,k;
		cin>>n>>k;
		ll r[n];
		ll h[n];
		double contri[n];
		double globalmax = 0.0;
		for(int i =0 ;i<n;i++){
			cin>>r[i]>>h[i];
			contri[i] = 2.0 * pi * r[i] * h[i];
			//cout<<contri[i]<<" "; 
		}
		//cout<<endl;
		for(int i =0 ;i<n;i++){
			double tempmax = contri[i];
			//cout<<tempmax<<" ";
			tempmax += (double)(pi * r[i] * r[i]); 
			//cout<<i<<" "<<tempmax<<" ";
			double newarr[n -1];
			int idx = 0;
			for(int j = 0; j < n; j++){
				if(j == i)continue;
				newarr[idx] = contri[j];
				idx++;
			}
			sort(newarr, newarr + (n-1));
			for(int j = n-2; j>=(n-k); j--){
				tempmax += newarr[j];
			}
			if(tempmax >= globalmax){
				globalmax = tempmax;
			}
			//cout<<tempmax<<endl;
		}




		cout<<"Case #"<<z<<": ";
		printf("%.6f\n", globalmax);
		
	}
	


}

