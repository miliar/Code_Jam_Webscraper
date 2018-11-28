#include <bits/stdc++.h>
using namespace std;
long long calc(long long n,long long k){
	long long  npl = pow(2,floor(log(k)/log(2)));
	long long  nsl = n - npl + 1;
	long long  pos = ceil(1.0*nsl/npl);
	long long  neg = floor(1.0*nsl/npl);
	long long int ngs = nsl - neg*npl;
	if(k - npl + 1 <= ngs){
		return pos;
	}else{
		return neg;
	}
}


void solve(int tt)
{
        long long n,k,ans;
        cin >> n >> k;
        ans = calc(n,k);
		cout << "Case #" << tt << ": ";
		if(ans <= 1)
			cout << 0 << " " << 0 << endl;
		else
	      cout << (long long)ceil(1.0*(ans-1)/2) << " " <<(long long)floor(1.0*(ans-1)/2) << endl;


}
int main()
{
   freopen("test.in","r",stdin);
  freopen("res.txt","w",stdout);
   int T;
   cin >> T;
   for(int i = 1 ; i <= T ; i++)
      solve(i);
    return 0;
}
