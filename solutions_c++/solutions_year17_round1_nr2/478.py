#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> pi;
int main(){
	
	int test,t=0,n,k,i,j,l,ans;
	int	lo,hi,qty;
	int recipe[55],ptr[55];
	bool fail;
	vector<pi> have[55];
	pi *curr;
	scanf("%d",&test);
	
	for( t=0 ; t<test ;){
		ans=fail=0;
		scanf("%d%d",&n,&k);
		for( i=0 ; i<n ; i++ ) scanf("%d",recipe+i);
		
		for( i=0 ; i<n ; i++ ){
			have[i].clear();
			for( j=0 ; j<k ; j++ ){
				scanf("%d",&qty);
				lo = qty - qty / 11;
				hi = qty + qty / 9;
				// lowest multiple of needed ingredient larger than lower bound
				lo = (lo + recipe[i]-1)/recipe[i];
				// highest multiple of needed ingredient lower than upper bound
				hi /= recipe[i];
				if( lo<=hi ) have[i].emplace_back(lo,hi);
			}
			if( have[i].size()==0 ) fail=true;
			sort(have[i].begin(),have[i].end());
		}
		
		if( !fail ){
			memset(ptr,0,sizeof(ptr));
			// try create 1 to 1st ingredient's limit portion
			for( i=1 ; ptr[0]<have[0].size() ; i++ ){
				for( j=0 ; j<n ; j++ ){						
					if( ptr[j]==have[j].size() ) goto end;
					curr = &have[j][ptr[j]];
					
					// too little portion, increase portion
					if( i < curr->first ) goto skip;
					// too much portion, increase ingredient then try again
					if( i > curr->second ) ptr[j--]++;
										
				}
				// everything is enough
				ans++;
				for( j=0 ; j<n ; j++ ) ptr[j]++;
				// try again with same portion
				i--;
				skip:;
			}
		}
		end:
		printf("Case #%d: %d\n",++t,ans);	
	}
	return 0;
}

