#include <iostream>
#include <vector>
using namespace std;
int main(){
	int zes;
	cin>>zes;
	for(int k = 0; k < zes;k++){
		long long size;
		long long guys;
		cin>>size>>guys;
		vector<long long> V;
		vector<long long> S;
		V.push_back(size);
		S.push_back(1);
		int i = 0;
		while(1){
			if(V[i] == 1) break;
			long long a,b;
			if(V[i] % 2 == 1){
				a = b = V[i]/2;
			}else{
				a = V[i]/2;
				b = V[i]/2 - 1;
			}
			bool w_a = 0;
			for(int j = i; j < V.size(); j++){
				if(V[j] == a){
					S[j] += S[i];
					w_a = 1;
				}
			}
			if(!w_a){
				V.push_back(a);
				S.push_back(S[i]);
			}
			
			bool w_b = 0;
			for(int j = i; j < V.size(); j++){
				if(V[j] == b){
					S[j] += S[i];
					w_b = 1;
				}
			}
			if(!w_b){
				V.push_back(b);
				S.push_back(S[i]);
			}
			i++;
		}
		i = 0;
		long long amm = 0;
		while(amm < guys){
			amm += S[i];
			i++;
		}
		long long result = V[i - 1];
		cout<<"Case #"<<k + 1<<": ";
		if(V[i - 1] % 2 == 1){
			cout<<V[i - 1]/2<<" "<<V[i - 1]/2<<endl;;
		}else{
			cout<<V[i - 1]/2<<" ";
			cout<<V[i - 1]/2 - 1<<endl;
		}
	}
}
