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
    int t, n ,m,j, ans =0;
    string s;
    int a[2000]={0};

    cin >> t;
    for (int k = 1; k <= t; ++k) {
        ans=0;
        cin>>s>>m;
        n = s.length();
        for(int i=0; i<n; i++ ){
            if(s[i]=='+'){
                a[i]=1;
            }else{
                a[i]=0;
            }
        }
        int flag = 1 ;
        for(int i=0; i<n; i++ ){
            if(a[i]==0){
                ans++;
                j=0;
                while( i+j<n && j<m ){
                    a[i+j]^=1;
                    j++;
                }
                if(j!=m)
                    flag=0;
            }
        }

        if(flag)
            cout << "Case #" << k << ": " << ans << endl;
        else
            cout << "Case #" << k << ": " << "IMPOSSIBLE" << endl;
  }

	return 0;
}
