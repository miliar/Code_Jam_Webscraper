#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<queue>
#include<map>
#include<cstring>
#include<set>
#include<stack>
using namespace std;
#define uii long long int
#define M(a,b) (a>b ? a : b)
#define m(a,b) (a>b ? b : a)
#define it(a)  ::iterator a
#define slld(a) uii a;scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define plld(a) printf("%lld",a)
#define MAX 10000
#define MOD 1000000007
#define powOf2(a) !(a&a-1)
#define mod(a) (a>0 ? a : (-1*a))
#define tc(a) uii a; for(scanf("%lld",&a);a--;)
#define swap(a,b) a = a^b; b = a^b;a = a^b;
int main(){
    uii T_case = 1;
    tc(T){			
	slld(N);slld(K);
	cout<<"Case #"<<T_case<<": ";
	T_case++;
	bool A[N+2];
	A[0] = true;
	A[N+1] = true;
	for(uii i = 1;i<N;i++){
		A[i] = false;
	}
	uii M1 = N;
	uii M2 = N;
	uii M;
	uii L ,R;
	priority_queue<uii> S;
	S.push(N);
	while(K!=0){
		M = S.top();
		S.pop();
		//cout<<M<<endl;
		if(M>1){
			L = (M%2==0 ? (M/2)-1 : (M/2));
			R = (M%2==0 ? (M/2) : (M/2));
			S.push(L);
			S.push(R);
		}
		else{
			L = 0;
			R = 0;
		}


		K--;
	}
	cout<<M(L,R)<<" "<<m(L,R)<<endl;
			
    }     
   




	return 0;
}


