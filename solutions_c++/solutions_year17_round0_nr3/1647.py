#include <stdio.h>
#include <map>

using namespace std;

typedef long long lli;

int main() {
	FILE* in=fopen("C-large.in","rt");
	FILE* out=fopen("Cout.txt","wt");
	int t;
	fscanf(in,"%d",&t);
	for(int tc=1;tc<=t;tc++) {
		fprintf(out,"Case #%d: ",tc);
		lli n, k;
		fscanf(in,"%lld %lld",&n,&k);
		if(k==1) {
			if(n%2==0) fprintf(out,"%lld %lld\n",n/2,n/2-1);
			else fprintf(out,"%lld %lld\n",n/2,n/2);
			continue;
		}
		int lv=0;
		while((1LL<<(lv+1))-1<k) lv++;
		k-=(1LL<<lv)-1;
		map<lli,lli> pre, aft;
		pre[n]=1;
		while(lv--) {
			aft.clear();
			for(map<lli,lli>::iterator it=pre.begin();it!=pre.end();it++) {
				lli num=it->first, cnt=it->second;
				if(num%2) {
					if(!aft.count(num/2)) aft[num/2]=0;
					aft[num/2]+=cnt*2;
				} else {
					if(!aft.count(num/2)) aft[num/2]=0;
					aft[num/2]+=cnt;
					if(!aft.count(num/2-1)) aft[num/2-1]=0;
					aft[num/2-1]+=cnt;
				}
			}
			pre.clear();
			for(map<lli,lli>::iterator it=aft.begin();it!=aft.end();it++) {
				pre[it->first]=it->second;
			}
		}
		lli tot=0, res;
		for(map<lli,lli>::iterator it=--aft.end();;it--) {
			tot+=it->second;
			if(tot>=k) {
				res=it->first;
				break;
			}
		}
		fprintf(out,"%lld %lld\n",res/2,res/2-(res%2==0?1:0));
	}
	return 0;
}
