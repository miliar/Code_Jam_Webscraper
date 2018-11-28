#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>

using namespace std;

/*long long[] getSolution(long long N, long long K){
	if(K == -1){
		K++;
		N++;
	}

	if(K == 0){
		long long sol[2];
		sol[0] = sol[1] = floor(N/2);		
		if(N % 2 == 0)
		{
			sol[0] = ceil(N/2)
		}
		return sol;
	}

	if(N%2 == 0){
		return getSolution( (N - 2)/2, floor((K - 2)/2));
	}
	return getSolution(N/2, K/2);
}*/

int main(){
	int i,j,k,l;
	string str;
	long long K, N, T;
	long long *a, *le, *r;
	cin>>T;

	for(l = 0 ; l < T ; l++)
	{
		cout<<"Case #"<<l+1<<": ";
		cin>>N>>K;
		//long long sol[2] = getSolution(N, K - 1);
		a = new long long[N];
		le = new long long[N];
		r = new long long[N];

		for(i = 0 ; i < N ; i++)
		{
			a[i] = 0;
			le[i] = i;
			r[i] = N - i - 1;
		}
		
		long long maxval = 0;
		long long minval = 0;
		long long pos = 0;
		
		for(i = 0 ; i < K ; i++){
			maxval = minval = pos = 0;			
			for(j = 0 ; j < N ; j++)
			{
				long long minIndexVal = min(le[j], r[j]);
				long long maxIndexVal = max(le[j], r[j]);				
				if(minIndexVal > maxval || (minIndexVal == maxval && maxIndexVal > minval)){
					pos = j;
					maxval = minIndexVal;
					minval = maxIndexVal;
				}
			}
			a[pos] = 1;
			le[0] = 0;
			if(a[0] == 1)
				le[0] = -1;
			for(j = 1 ; j < N ; j++)
				if(a[j] == 1)
					le[j] = -1;
				else
					le[j] = le[j - 1]+1;

			r[N - 1] = 0;
			if(a[N - 1] == 1)
				r[N - 1] = -1;
			for(j = N - 2 ; j >= 0 ; j--)
				if(a[j] == 1)
					r[j] = -1;
				else
					r[j] = r[j + 1]+1;
		}
		cout<<minval<<"\t"<<maxval<<"\n";
		delete[] le;
		delete[] a;
		delete[] r;
	}
	return 0;
}
