#include <bits/stdc++.h>
using namespace std;

void f(int A[],int n){
	if(n==0){
		A[0] += 1;
		return;
	}
	if(n%2==1){
		A[n/2] += 2;
		f(A,n/2);
		f(A,n/2);
	}
	else{
		A[n/2] += 1;
		A[n/2-1] += 1;
		f(A,n/2);
		f(A,n/2-1);
	}
}


int main(){

	int t;
	int n,k;
	scanf("%d",&t);
	for(int cases = 1;cases<=t;cases++){
		scanf("%d %d",&n,&k);
		int A[n+1] = {0};
		f(A,n);
		int count = 0;
		int j = n;
		int l,s;
		if(count<k-1){
			while(count<k-1){
				count += A[j];
				j--;
			}
			j++;
		}
		if(j%2==1){
			l = j/2;
			s = j/2;
		}
		else{
			l = j/2;
			s = j/2-1;
		}
		printf("Case #%d: ",cases);
		printf("%d %d\n",max(l,s),min(l,s));

/*

		list<pair<int,int> > X;
		X.push_back(make_pair(1,n));
		int j = k;
		while(X.size() && k!=1){
			pair<int,int> s = X.front();
			X.pop_front();
			int p = (s.first + s.second)/2;
			if(A[p]==0){
				A[p] = 1;
				k--;
				int a1 = s.first;
				int a2 = (s.first + s.second)/2 - 1;
				int b1 = (s.first + s.second)/2 + 1;
				int b2 = s.second;
				if(a2-a1>=0 && b2-b1>=0){
					if(a2-a1 > b2-b1){
						list<pair<int,int> > :: iterator itr;
						itr = X.begin();
						while(itr!=X.end() &&  ((*itr).second-(*itr).first) > (a2-a1) ){
							itr++;
						}
						X.insert(itr,make_pair(a1,a2));
						itr = X.begin();
						while(itr!=X.end() &&  ((*itr).second-(*itr).first) > (b2-b1) ){
							itr++;
						}
						X.insert(itr,make_pair(b1,b2));
					}
					else if(a2-a1 <= b2-b1){
						list<pair<int,int> > :: iterator itr;
						itr = X.begin();
						while(itr!=X.end() &&  ((*itr).second-(*itr).first) > (b2-b1) ){
							itr++;
						}
						X.insert(itr,make_pair(b1,b2));
						itr = X.begin();
						while(itr!=X.end() &&  ((*itr).second-(*itr).first) > (a2-a1) ){
							itr++;
						}
						X.insert(itr,make_pair(a1,a2));
					}
				}
				else if(a2-a1>=0){
					list<pair<int,int> > :: iterator itr;
					itr = X.begin();
					while(itr!=X.end() &&  ((*itr).second-(*itr).first) > (a2-a1) ){
						itr++;
					}
					X.insert(itr,make_pair(a1,a2));
				}
				else if(b2-b1>=0){
					list<pair<int,int> > :: iterator itr;
					itr = X.begin();
					while(itr!=X.end() &&  ((*itr).second-(*itr).first) > (b2-b1) ){
						itr++;
					}
					X.insert(itr,make_pair(b1,b2));
				}
			}
		}
		pair<int ,int> P = X.front();
		int a = P.first;
		int b = P.second;
		int answer = (a+b)/2;

		j = a;
		while(A[j]==0){
			j--;
		}

		int v = b;
		while(A[v]==0){
			v++;
		}

		printf("Case #%d: ",cases);
		printf("%d %d\n",max(a-j,v-b),min(a-j,v-b));

*/

/*

		for(int p=1;p<=k;p++){
			int L[n+1] = {-1};
			int S[n+1] = {-1};
			int j,m;
			for(int i=1;i<=n;i++){
				j = i;
				m = i;
				while(j>=0){
					if(A[j]==1){
						break;
					}
					else{
						j--;
					}
				}
				while(m<=n+1){
					if(A[m]==1){
						break;
					}
					else{
						m++;
					}
				}
				L[i] = i-j;
				S[i] = m-i;
			}
			int answer;
			for(int i=1;i<=n;i++){
				if(A[i]==0){
					answer = i;
					break;
				}
			}
			for(int i=1;i<=n;i++){
				if(min(L[answer],S[answer])<min(L[i],S[i])){
					answer = i;
				}
				else if(min(L[answer],S[answer]) == min(L[i],S[i])){
					if(max(L[answer],S[answer])<max(L[i],S[i])){
						answer = i;
					}
				}
			}
			A[answer] = 1;
			if(p==k){
				printf("Case #%d: ",cases);
				printf("%d %d\n",max(L[answer]-1,S[answer]-1),min(L[answer]-1,S[answer]-1));
			}
		}
*/
	}

	return 0;
}