#include <bits/stdc++.h>

#define mt make_tuple
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<string> vs;

void test(){
    ll n, k;
    cin >> n >> k;
    ll a=1,b=0;
    /*if(2*k > n){
        cout << "0 0" << endl;
        return;
    }*/
    ll tel = 0;
    for(ll i = 0 ;  ; i++){
    	//cout << "i: " << i << " a: " << a << " b: " << b << endl;
    	if( tel < k && k <= 2*tel+1 ){
    		if( k-tel <= a){
    			cout << (n>>(i+1)) << " " << ((n>>(i+1)) -1+ (n>>i)%2) << endl;
    			return;
    		}
    		else{
    			cout << ((n>>(i+1))-1+ (n>>i)%2) << " " << ((n>>(i+1)) -1) << endl;
    			return;
    		}
    	}
    	tel = tel*2+1;
    	ll na, nb;
    	if( (n>>i)%2 == 0){
    		na = a;
    		nb = a+2*b;
    	}
    	else{
    		na = 2*a+b;
    		nb = b;
    	}
    	a = na; b = nb;
    }
}

int main(){
    int t;
    cin >> t;
    for( int i = 1;i<= t;i++){
        cout << "Case #" << i << ": ";
        test();
    }
	return 0;
}
