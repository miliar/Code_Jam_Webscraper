#include <iostream>
#include <string>

#define MAXN 1000

using std::cin;using std::cout;

int T,K;

bool bits[MAXN];


int main(){
	cin>>T;
	for(int i=0;i<T;i++){
		std::string S;
		cin>>S>>K;
		int L = S.length();
		
		for(int j=0;j<L;j++){
			bits[j]=0;
			if(S[j]=='-')
				bits[j]=1;
		}
		
		int result = 0;
		for(int j=0;j+K<=L;j++){
			if(bits[j]==1){
				result++;
				for(int k=j;k<j+K;k++)
					bits[k]=!bits[k];
			}
		}
		for(int j=L-K+1;j<L;j++){
			if(bits[j]==1){
				result=-1;
				break;
			}
		}
		
		cout<<"Case #"<<i+1<<": ";
		if(result==-1)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<result<<'\n';
		
		
	}
    return 0;
}
