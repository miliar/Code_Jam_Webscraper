#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <functional>
#include <set>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <unordered_map>

using namespace std;

int main()
{
		
    int T;
    cin>>T;
	
    for(int t=1;t<=T;t++){
		long long n,k;
		cin>>n>>k;

		map<long long,long long> mp;
		mp[-n]=1;

		long long L,R;
		long long cnt=0;
		for(auto it=mp.begin();it!=mp.end()&&cnt<k;mp.erase(it++)){
			long long x=-(it->first);
			L=(x-1)/2,R=(x-1)-L;
			cnt+=mp[-x];
			mp[-L]+=mp[-x];
			mp[-R]+=mp[-x];
		}

		printf("Case #%d: %lld %lld\n",t,max(L,R),min(L,R));

	}
    
    return 0;
}