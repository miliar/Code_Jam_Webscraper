#include <bits/stdc++.h>
using namespace std;
int main(){
	ifstream cin("input.in");
    ofstream cout("output.in");
	int t;
	cin>>t;
	for(int it=1;it<=t;it++){
		long long int n;
		vector<int>v;
		cin>>n;
		while(n){
			v.push_back(n%10);
			n/=10;
		}
		cout<<"\n";
		for(int i=1;i<v.size();i++){
			if(v[i]>v[i-1]){
				v[i]-=1;
				for(int j=0;j<i;j++)
					v[j]=9;
			}
		}
		for(int i=v.size()-1;i>=0;i--){
			n=n*10+v[i];
		}
		cout<<"Case #"<<it<<": "<<n<<endl;
	}
}