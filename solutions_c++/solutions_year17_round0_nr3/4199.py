#include<bits/stdc++.h>
using namespace std;

typedef long long LL;
#define MOD 1000000007

LL mpow(LL a, LL n) {
	LL ret=1;
	LL b=a;
	while(n) {
		if(n&1)
			ret=(ret*b)%MOD;
		b=(b*b)%MOD;
		n>>=1;
	}
	return (LL)ret;
}




int main() {
    int t;
    LL n ,temp , x,ans1,ans2;

    cin >> t;
    for (int k = 1; k <= t; ++k) {
        cin>>n>>x;
        priority_queue<LL> q;
        q.push(n);
        for(int i=1; i<x; i++ ){
            LL t = q.top()-1;
            q.push(ceil(t/2.0));
            q.push(t/2);
            q.pop();
        }
        cout << "Case #" << k << ": ";
        ans1 = q.top()-1;
        ans2 = ans1/2;
        ans1 = ceil(ans1/2.0);
        cout<<ans1<<" "<<ans2;
        cout<< endl;
    }

	return 0;
}
