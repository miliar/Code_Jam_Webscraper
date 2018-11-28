#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std ;

typedef long long LL;

LL N,K,NL,NR,CL,CR,AnsN;

LL maxLL(LL a,LL b){return a>b?a:b;}
LL minLL(LL a,LL b){return a<b?a:b;}

void Solve(){
	NL=N;
	NR=N+1;
	CL=1;
	CR=0;
	for(;;){
		if(K<=CR){
			AnsN=NR;
			return;
		}else if(K<=CL+CR){
			AnsN=NL;
			return;
		}else{
			K-=CL+CR;
			LL N1=(NL-1)/2,N2=NL-1-(NL-1)/2,N3=(NR-1)/2,N4=NR-1-(NR-1)/2;
			NL=minLL(minLL(N1,N2),minLL(N3,N4));
			NR=maxLL(maxLL(N1,N2),maxLL(N3,N4));
			LL C1=(NL==N1?CL:0)+(NL==N2?CL:0)+(NL==N3?CR:0)+(NL==N4?CR:0);
			LL C2=(NR==N1?CL:0)+(NR==N2?CL:0)+(NR==N3?CR:0)+(NR==N4?CR:0);
			CL=C1;
			CR=C2;
		}
		//cerr<<"K="<<K<<" NL="<<NL<<" NR="<<NR<<"\n";
	}
}

int main(){
	int Test; cin>>Test;
	for(int i=1;i<=Test;i++){
		cin>>N>>K;
		Solve();
		cout<<"Case #"<<i<<": "<<AnsN-1-(AnsN-1)/2<<" "<<(AnsN-1)/2<<"\n";
	}
}