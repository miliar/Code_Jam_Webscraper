#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

/*void print(vector<bool> p){
	for (int i=0; i<p.size(); i++){
		cout<<p[i];
	}
	cout<<endl;
}*/

int main(){
	
	int T, K;
	string S;
	
	cin>>T;
	for (int testcase=1; testcase<=T; testcase++){
		//cout<<"Reading testcase "<<testcase<<endl;
		cin>>S;
		cin>>K;
		//cout<<S<<endl;
		//cout<<K<<endl;
		
		int N=S.size();
		vector<bool> p(N);
		for(int i=0;i<N;i++){
			if (S[i]=='+'){
				p[i]=1;
			}
			else {
				p[i]=0;
			}
		}
		//print(p);
		
		//cout<<"Processing"<<endl;
		
		int otoc=0;
		for (int i=0;i < S.size()-K+1; i++){
			if (p[i]==0){
				for (int j=0;j<K;j++){
					p[i+j]=!p[i+j];
				}
				otoc++;
			}
		}
		//print(p);
		//cout<<otoc<<endl;
		bool dobre=1;
		for (int i=N-K+1;i<N; i++){
			if (p[i]==0) dobre=0;
		}
		
		//cout<<"Odpoved"<<endl;
		cout<<"Case #"<<testcase<<": ";
		if (dobre==0){
			cout<<"IMPOSSIBLE"<<endl;
		}
		else cout<<otoc<<endl;
	}
}