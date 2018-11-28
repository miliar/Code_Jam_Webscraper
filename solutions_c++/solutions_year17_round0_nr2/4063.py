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


LL small(LL x,vector<LL> &v){
    LL i = x;
    LL a = i/10 , b =i%10;
    while(a>b){
        i--;
        a = i/10 ; b =i%10;
    }
    if((x/10)>(i/10)){
        for(int k=v.size()-1; k>=0; k-- ){
            v[k]=9;
        }
    }
    return a*10+b;

}


int main() {
    int t;
    LL n ,temp , x;

    cin >> t;
    for (int k = 1; k <= t; ++k) {
        cin>>n;
        vector<LL> v;
        while(n!=0){
            temp = n%100;
            x = small(temp,v);
            v.push_back(x%10);
            n = n/100;
            n = n*100;
            n+=x;
            n/=10;
        }

        cout << "Case #" << k << ": ";
        for(int i=v.size()-1; i>=0; i-- ){
            cout<<v[i];
        }
        cout<< endl;
    }

	return 0;
}
