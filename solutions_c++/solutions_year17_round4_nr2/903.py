#include<bits/stdc++.h>
using namespace std;

#define scl(x) scanf("%lld",&x)
#define sc(x)  scanf("%d",&x)
#define ll long long
#define lop(i,n) for(int i=0;i<n;++i)
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;


int t,n,m,c; // c=2
int out;
int prom;

void work1(vector<int> &A,vector<int> &B,int &sA,int &sB){
	priority_queue<ii> pq;
	for(int i=1;i<n;i++)
		if(B[i])pq.push(ii(A[i]+B[i],i));
	while(pq.size()&&A[0]){
		ii x=pq.top();
		pq.pop();
		int i=x.second;
		--B[i];--sB;
		--A[0];--sA;
		if(B[i]){
			pq.push(ii(A[i]+B[i],i));
		}
		out++;
	}
	int j=1;
	while(A[0]&&sB!=B[0]){
		while(!B[j])j++;
		--A[0];--sA;
		--B[j];--sB;
		out++;
	}
}


int main(){
#ifndef ONLINE_JUDGE
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
#endif
	sc(t);
	lop(C,t){
		out=0;
		prom=0;

		sc(n),sc(c),sc(m);
		vector<int> A(n,0),B(n,0);
		lop(i,m){
			int p,b;
			sc(p),sc(b);--p,--b;
			if(b==0)A[p]++;
			else B[p]++;
		}

		int sA=accumulate(A.begin(),A.end(),0);
		int sB=accumulate(B.begin(),B.end(),0);


		work1(A,B,sA,sB);
		work1(B,A,sB,sA);

		if(!sA||!sB){
			out+=sA+sB;
		}
		else if(sA==A[0]&&sB==B[0]){
			out+=A[0]+B[0];
		}
		else {
			if(sB>sA){
				swap(sA,sB);
				swap(A,B);
			}

			priority_queue<ii> pq;
			for(int i=1;i<n;i++)
				if(A[i])pq.push(ii(A[i]+B[i],i));

			int j=1;
			while(sA>sB){
				if(pq.size()){
					int i=pq.top().second;
					pq.pop();
					--A[i];--sA;
					out++;
					if(A[i])pq.push(ii(A[i]+B[i],i));
				}
				else {
					while(!A[j])j++;
					--A[j];--sA;
					out++;
				}
			}
			out+=sA;
			lop(i,n){
				if(A[i]>=B[i]&&A[i]>sB-B[i])prom+=A[i]-(sB-B[i]);
				else if(B[i]>=A[i]&&B[i]>sA-A[i])prom+=B[i]-(sA-A[i]);
			}
		}
		printf("Case #%d: %d %d\n",C+1,out,prom);
	}
}
