#include<bits/stdc++.h>
using namespace std;

int t;
long long int n;
int v[22];
long long int resp;

long long int f(int u){
	long long int m=1;
	for(int i=1; i<=u; i++){
		m=m*10;
	}
	return m;
}


int main(){
	scanf("%d", &t);
	for(int c=1; c<=t; c++){
		scanf("%lld", &n);	
		long long int ind=1LL;
		int tam=0;
		while(n/ind!=0){
			tam++;
			if(ind==1) v[1]=n%10;
			else{
				long long int m=n-n%ind;	
				m=m/ind;
				v[tam]=m%10;
			}
			ind*=10;
		}
		for(int i=1; i<=tam/2; i++){
			swap(v[i], v[tam+1-i]);	
		}
	
		resp=n;
		for(int i=1; i<=tam-1; i++){
			if(v[i+1]<v[i]){
				while(v[i-1]==v[i]){
					i--;	
				}
				resp=n-n%(f(tam-i))-1LL;
				break;
			}
		}
		printf("Case #%d: %lld\n", c, resp);
	}
	
	return 0;
}	

