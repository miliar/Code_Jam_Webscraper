#include<iostream>

using namespace std;

int main(){
	int T;
	cin>>T;

	char *S = new char[1024];
	int K;

	int i,j,k;
	int n,e;
	for(i=0;i<T;i++){
		cin>>S>>K;
		for(n=0;S[n]!='\0';n++);
		e = 0;
		for(j=0;j<n;j++){
			if(S[j]=='-'){
				if(j+K>n) break;
				else {
					for(k=j;k<j+K;k++){
						S[k] = (S[k]=='-'? '+' : '-');
					}
					e = e + 1;
				}
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(j<n)
			cout<<"IMPOSSIBLE";
		else
			cout<<e;
		cout<<endl;
	}

	return 0;
}
