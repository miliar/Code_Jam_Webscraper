#include <bits/stdc++.h>

using namespace std;

#define INTMAX 0x7FFFFFFF
#define INTMIN -0x80000000
#define LONGMAX 0x7FFFFFFFFFFFFFFF
#define LONGMIN -0x8000000000000000

int main(){
	int T;
	cin>>T;
	for(int tc=1; tc<=T; tc++){
		long long n, k;
		cin>>n>>k;
		
		long long s_nr, s_cnt;
		long long b_nr, b_cnt;
		
		s_nr = n-1, b_nr = n;
		s_cnt = 0, b_cnt = 1;
		
		long long len = 0;
		while(len==0){
			if(k<=b_cnt)
				len = b_nr;
			else if(k<=b_cnt+s_cnt)
				len = s_nr;
			k -= b_cnt + s_cnt;

			long long n_s_nr, n_s_cnt;
			long long n_b_nr, n_b_cnt;
			if(b_nr%2==1){
				n_b_nr = (b_nr-1)/2;
				n_s_nr = n_b_nr - 1;
				n_s_cnt = s_cnt;
				n_b_cnt = 2*b_cnt + s_cnt;
			}
			else{
				n_s_nr = (b_nr-1)/2;
				n_b_nr = n_s_nr + 1;
				n_s_cnt = 2*s_cnt + b_cnt;
				n_b_cnt = b_cnt;
			}
			s_nr = n_s_nr, s_cnt = n_s_cnt;
			b_nr = n_b_nr, b_cnt = n_b_cnt;
		}
		
		long long mini = (len-1)/2;
		long long maxi = len/2;
		//cout<<len<<endl;
		cout<<"Case #"<<tc<<": "<<maxi<<" "<<mini<<endl;
	}
}