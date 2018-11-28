#include <iostream>

using namespace std;

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		long long N, K;
		cin>>N>>K;
		long long q[200]={0,};
		long long num[200]={0,};
		int start=0,end=1;
		q[0]=N;
		num[0]=1;
		long long number, f, s;
		for(start=0;K>0;start++){
			number=num[start];
			K-=number;
			f = q[start]/2;
			s = q[start]-1-q[start]/2;
			if(q[end-1]!=f){
				q[end++]=f;
			}
			num[end-1]+=number;
			if(q[end-1]!=s){
				q[end++]=s;
			}
			num[end-1]+=number;
		}
		cout<<"Case #"<<t<<": "<<f<<" "<<s<<endl;
	}
	return 0;
}
