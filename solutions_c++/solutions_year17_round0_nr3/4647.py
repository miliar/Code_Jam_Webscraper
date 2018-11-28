#include<stdio.h>
#include<vector>
#include <algorithm> 
#include <queue>

using namespace std;

struct Par {
	long long int Dist,Pos;
	bool operator<(const Par& o) const
    	{
		if(Dist > o.Dist) return false;
		if(Dist == o.Dist && Pos < o.Pos) return false;
        	return true;
    	}
};

priority_queue <Par> A;

Par Calcula(Par n){
	Par aux1, aux2;
	long long int Dist=n.Dist , Pos = n.Pos;
	long long D1,P1,D2,P2;
	D1=(Dist-1)/2;
	D2= D1;
	if(Dist%2==0) D2++;
	P1=Pos;
	P2=Pos+D1+1;
//	printf("Dist:%lld Pos:%lld\n",Dist,Pos);
//	printf("D1:%lld P1:%lld \nD2:%lld P2:%lld\n",D1,P1,D2,P2);
	if(D1>0){
		aux1.Dist=D1;
		aux1.Pos=P1;
		A.push(aux1);
	}
	if(D2>0){
		aux2.Dist=D2;
		aux2.Pos=P2;
		A.push(aux2);
	}
	aux1.Dist=D1;
	aux1.Pos=D2;
	return aux1;
}
void Clear(){
	while(!A.empty()) A.pop();
}
int main(){
	long long int T,contt,cont1,N,K;
	Par aux;
	scanf("%lld",&T);
	for(contt=1;contt<=T;contt++){
		scanf("%lld %lld",&N,&K);
		aux.Dist=N;
		aux.Pos=1;
		A.push(aux);
		//ImprimeA();
		for(cont1=0;cont1<K;cont1++){
			aux=A.top();
		//	printf("Par : Dist: %lld Pos: %lld\n", aux.Dist , aux.Pos);
			A.pop();
			aux=Calcula(aux);
		//	sort(A.begin(),A.end(),compara);
		//	ImprimeA();
		}
		if(aux.Dist < aux.Pos){
			N=aux.Dist;
			aux.Dist=aux.Pos;
			aux.Pos=N;
		}
		printf("Case #%lld: %lld %lld\n",contt,aux.Dist,aux.Pos);
		Clear();
	}
}
