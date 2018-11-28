#include<iostream>
#include<stdint.h>
#include<vector>
#include<algorithm>
using namespace std;
int const infty = 30000;
vector<short> ItV(int64_t H){
	vector<short> Q;
	while(H>0){
		Q.push_back(H%10);
		H/=10;
	}
	reverse(Q.begin(),Q.end());
	return Q;
}
void prinv(vector<short> A){
	int i=0;
	while(A[i]==0) i++;
	while(i<A.size()){
		if(A[i]>9){cout<<"9";}
		if(A[i]<=9){cout<<A[i];}
		i++;
		}
	cout<<"\n";
	return;
}

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	int64_t N;
	int tenpow,smallest;
	vector<short> ans;
	cin>>T;
	for(int idddd =1; idddd<=T; idddd++){
		tenpow=1;
		smallest=N%10;
		cin >> N;
		ans=ItV(N);
		cout << "Case #" <<idddd <<": ";
		prinv(ans);
	}
	
	return 0;
}