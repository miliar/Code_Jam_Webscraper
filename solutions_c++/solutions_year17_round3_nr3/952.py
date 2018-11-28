#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef pair<ll, ll> pii;

template<typename T>
using pq_gt = priority_queue<T, vector<T>, greater<T>>;
template<typename T>
using pq_lt = priority_queue<T, vector<T>, less<T>>;

#define se second
#define fi first
#define pb push_back
#define mp make_pair

long double prob[100];
long double conProb[100][100];

long double choose(int start, int num, int end, bool flag) {
	//cout<<start<<" "<<end<<endl;
	if(start + num > end) {
		return 0;
	}
	if(start == end) {
		//cout<<num<<endl;
		if(flag) {
			return num==0;
		}
		return 1;
	}
	if(conProb[start][num]!= 0) {
		return conProb[start][num];
	}
	long double cur = 0;
	//if(num >0)
	cur = prob[start] * choose(start+1, num-1, end, flag);
	//cout<<cur<<endl;
	cur += (1-prob[start]) * choose(start+1, num, end, flag);
	return conProb[start][num]  = cur;
}

int main() {
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    cout<<fixed<<setprecision(50);
    for(int testcase = 1; testcase <= t; testcase++) {
    	printf("Case #%d: ", testcase);
    	int n,k;
    	cin>>n>>k;
    	long double tr;
    	cin>>tr;
    	for(int i = 0; i < n; i++) {
    		cin>>prob[i];
    	}
    	sort(prob, prob+n, greater<long double>());
    	if(k==1) {
    		prob[0] += tr;
    	}
    	for(int i = k-1; i>0; i--) {
    		//cout<<i<<" " <<tr<<endl;
    		if(tr < (prob[i-1] - prob[i]) * (k-i) ) {
    			long double val = prob[i] + tr/(k-i);
    			for(int j = i; j <k; j++) {
    				prob[j] = val;
    			}
    			tr = 0;
    			break;
    		} else {
    			tr -= (prob[i-1] - prob[i]) * (k-i);
    			//cout<<tr<<endl;
    			if(i==1) {
    				long double temp = prob[0];
    				for(int j = 0; j < k; j++) {
    					prob[j] = temp + tr/k;
    				}
    				tr = 0;
    			}
    		}
    	}

    	if(prob[k-1] >= 1) {
    		cout<<1<<endl;
    		continue;
    	}
    	while(prob[n-1] == 0) {
    		n--;
    	}
    	if(n<k) {
    		cout<<0<<endl;
    		continue;
    	}
    	for(int i = 0; i < n; i++) {
    		for(int j = 0; j< n; j++) {
    			conProb[i][j] = 0;
    		}
    	}
    	long double ans = 1;
    	for(int i = 0; i < k; i++) {
    		ans *= prob[i]; //* (choose(k, k-i, n, false));
    	}
    	cout<<ans<<endl;
    }
}