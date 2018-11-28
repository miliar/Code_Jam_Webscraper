#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define inf 1e18
#define pb push_back
#define mp make_pair
#define Int long long
#define fs first
#define sc second
#define pii pair<int, int>

int main(){

	Int t, n, k, o, e, tot, m, T, temp, Max, Min, O, E;

	cin>>T;

	for(t = 1; t <= T; t++){

		cin>>n>>k;
		
		o = (Int)(n%2 != 0);e = (Int)(n%2 == 0);tot = 1;
		m = n;

		while(tot < k){

			temp = (m-1)/2;

			if(temp%2 != 0){
				o = 2*o + e;
			}else{
				temp = e;
				e = 2*o + e;
				o = temp;
			}
			
			m /= 2;
			tot += o + e;

		}
		
		if(tot >= k){
			k -= (tot - o - e);
			if((m%2 == 0 && k > e) || (m%2 != 0 && k > o))
				m--;
		}
		Max = Min = m/2;
		if(m%2 == 0 && m)
			Min--;
		cout<<"Case #"<<t<<": "<<Max<<" "<<Min<<endl;
	}

	return 0;
}