#include<iostream>
#include<string>
#include <algorithm>
#include<vector>
using namespace std;

void print(vector<int> &v){
	bool leading =true;
	for(int i=0;i<v.size();i++){
		if(leading && v[i]>0){
			leading = false;
		}
		if(leading&&v[i] ==0)
			continue;
		cout<<v[i];
	}
	cout<<endl;
}

int main(){
	int t;
	cin>>t;
	for(int k=1;k<=t;k++){
		long long int n;
		cin>>n;
		vector<int> v;
		long long int temp =n;
		int d =0;
		while(temp>0){
			v.push_back(temp%10);
			temp=temp/10;
			d++;
		}
		reverse(v.begin(), v.end());
		if(v.size()==1){
			cout<<"Case #"<<k<<": "<<n<<endl;
			continue;
		}
		
		for(int i = d-1;i>0;i--){
			int x1 = v[i];
			int x2 = v[i-1];
		
			if(x2>x1){
				v[i-1] = v[i-1] - 1;
				for(int j=i;i<d;i++)
					v[i]=9;
			}		
		}

	cout<<"Case #"<<k<<": ";
	print(v);
	}
}
			
