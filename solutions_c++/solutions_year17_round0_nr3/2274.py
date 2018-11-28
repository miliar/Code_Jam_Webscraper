#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;

#define ll long long
#define mk(i,j) make_pair(i,j)
#define fs first
#define sd second


int binary(vector< pair<ll,ll> > &q, ll n){
	int ini = 0, fin = q.size(), mid;
	while(ini<fin){
		mid = (ini+fin)/2;
		if(q[mid].fs == n) return mid;
		if(q[mid].fs<n){
			fin = mid-1;
		}
		else{
			ini = mid+1;
		}
	}
	if(ini < q.size() && q[ini].fs==n) return ini;
	return -1;
}


void mypush(vector< pair<ll,ll> > &q, ll n, ll m){
	int index = binary(q,n);
	if(index<0){
		q.push_back( mk(n,m) );
		sort(q.begin(),q.end(), [](pair<ll,ll> x, pair<ll,ll> y){ return x.fs>y.fs; } );
	}
	else{
		q[index].sd+=m;
	}
}


int main(){
	int t;
	ll n, k, last;
	pair<ll,ll> aux;
	cin >> t;
	for(int tt=1;tt<=t;tt++){
		cout << "Case #" << tt << ": ";
		cin >> n >> k;
		vector< pair<ll,ll> > q;
		int top = 0;
		q.push_back( mk(n,1) );
		while(k>0){
			aux = q[top]; top++;
			last = aux.fs;
			if(last%2==1){
				mypush(q, last/2,2*aux.sd);
			}
			else{
				mypush(q, last/2, aux.sd);
				mypush(q,last/2-1,aux.sd);
			}
			k-=aux.sd;
		}
		if(last%2==1)
			cout << last/2 << " " << last/2 << endl;
		else
			cout << last/2 << " " << last/2 - 1 << endl;
			
	}
	return 0;
}
