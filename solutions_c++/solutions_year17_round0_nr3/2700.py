#include<iostream>

using namespace std;

int main(){
	int t; cin >> t;
	for(int tc = 1; tc <= t; tc++){
		long long n, k; cin >> n >> k;
		long long mx, mn;
		mx = n / 2;
		if(n % 2 == 0) mn = mx - 1;
		else mn = mx;
		if(k == 1) {
			cout << "Case #"<<tc<< ": " << mx << " " << mn << endl;
			continue;
		}
		long long ppp = 1;
		long long tot = 1;		
		long long a_mx, b_mx, a_mn, b_mn;
		long long a_cnt = 1;
		long long b_cnt = 0;
		bool flag = true;
		while(mx == mn){	
			 // first pair
			a_mx = mx / 2;
			if (mx % 2 == 0) a_mn = a_mx - 1;
			else a_mn = a_mx;
			if( k <= tot + ppp) { cout << "Case #" << tc << ": " << a_mx << " " << a_mn << endl;flag = false; break;}

			// 2nd pair
			b_mx = mn / 2;
			if (mn % 2 == 0) b_mn = b_mx - 1;
			else b_mn = b_mx;	
			if(k <= tot + ppp + ppp) { cout << "Case #" << tc << ": " << b_mx << " " << b_mn << endl; flag = false;break;}
			a_cnt = ppp;
			b_cnt = ppp;
			mx = max(a_mx, b_mx);
			mn = min(a_mn, b_mn);
			tot += ppp + ppp;
			ppp *= 2;

		}

		
		if(!flag) continue;
		a_mx = mx/2;
		a_mn = mx - a_mx - 1;
		if( k <= tot + ppp) { cout << "Case #" << tc << ": " << a_mx << " " << a_mn << endl;flag = false; continue;}
		b_mx = mn/2;
		b_mn = mn - b_mx - 1;
		if(k <= tot + ppp + ppp) { cout << "Case #" << tc << ": " << b_mx << " " << b_mn << endl; flag = false;continue;}
		mx = max(a_mx, b_mx);
		mn = min(a_mn, b_mn);
		a_cnt = ppp;
		b_cnt = ppp;
		tot += ppp + ppp;
		ppp *= 2;

		
		while(flag){
			if(a_mx == b_mx){
                                b_cnt = b_cnt;
                                a_cnt = ppp+ppp - b_cnt;
                        }else{
                                a_cnt = a_cnt;
                                b_cnt = ppp+ppp - a_cnt;
                        }	
			// first pair
			a_mx = mx / 2;
			if (mx % 2 == 0) a_mn = a_mx - 1;
			else a_mn = a_mx;
			
			
			// 2nd pair
			b_mx = mn / 2;
			if (mn % 2 == 0) b_mn = b_mx - 1;
			else b_mn = b_mx;
			

//			cout << "("<<a_mx<<","<<a_mn<<") | ("<<b_mx<<","<<b_mn<<") | " << a_cnt << " | " << b_cnt << endl;
			
			if (tot + a_cnt >= k) { cout << "Case #" << tc << ": " << a_mx << " " << a_mn << endl; break;}
			if(tot + a_cnt + b_cnt >= k)  { cout << "Case #" << tc << ": " << b_mx << " " << b_mn << endl; break;}
			mx = max(a_mx, b_mx);
			mn = min(a_mn, b_mn);
			
			tot += ppp + ppp;
			ppp *= 2;
		}
	}
	return 0;
}
