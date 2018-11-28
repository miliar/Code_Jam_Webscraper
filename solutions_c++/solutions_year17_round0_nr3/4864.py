#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef pair<ll, ll> pii;


#define se second
#define fi first
#define pb push_back
#define mp make_pair

void print(int t) {
	cout<<"Case #"<<t<<": ";
}

void print(int t, int ans) {
	cout<<"Case #"<<t<<": "<<ans<<endl;
}

int main() {
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int T = 1; T<=t; T++) {
    	long long int n,k;
    	cin>>n>>k;
    	priority_queue<long long int, vector<long long int>, less<long long int>> pq;
    	pq.push(n);
    	for(long long int i = 0; i <k-1; i++) {
    		long long int t = pq.top();
    		//cout<<t<<endl;
    		pq.push(t/2);
    		pq.push((t-1)/2);
    		pq.pop();
    	}
    	print(T);
    	long long int t = pq.top();
    	cout<<t/2<<" "<< (t-1)/2<<endl;
    }
}