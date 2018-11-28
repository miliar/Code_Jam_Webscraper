#include <bits/stdc++.h>

using namespace std;

long long n,k;

typedef pair <long long,long long> ii;

typedef pair <ii,long long> iii;

class Compare{

public:
    bool operator() (iii a, iii b){
        if(a.first.first < b.first.first) return true;
        else if(a.first.first == b.first.first){
        	return a.first.second > b.first.second;
        }
        else return false;
    }
};

void f(long long L, long long R){

	priority_queue <iii, vector <iii>, Compare> q;

	q.push(iii(ii(L-R-1,L),R));

	while(!q.empty()){
			
		k--;

		if(k == 0) break;

		iii aux = q.top(); q.pop();

		L = aux.first.second;
		R = aux.second;

		long long mid = (L+R)/2;

		q.push(iii(ii(mid-L-1,L),mid));
		q.push(iii(ii(R-mid-1,mid),R));

	}

	iii aux = q.top();

	L = aux.first.second;
	R = aux.second;

	long long mid = (L+R)/2;	
	
	printf("%lld %lld\n",max(R-mid-1,mid-L-1),min(R-mid-1,mid-L-1));

}

int main(){

	int t;

	scanf("%d", &t);

	for(int casos = 1; casos <= t; ++casos){

		scanf("%lld %lld", &n, &k);

		printf("Case #%d: ",casos);

		f(1,n+2);
	}

	return 0;
}