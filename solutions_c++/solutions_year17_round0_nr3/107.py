#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;
long long A[100005],B[100005];
map<long long, int> LEN;
int main(){
	int T,i,j,k,l,tt = 0,h,t;
	long long n,m;
	scanf("%d",&T);
	while(T--){
		tt++;
		scanf("%I64d%I64d\n",&n,&m);
		LEN.clear();
		h = 1;
		t = 1;
		A[1]=n;B[1]=1;
		LEN.insert(make_pair(n,1));
		while(m>B[h]){
			long long t1 = (A[h]-1)/2+(A[h]-1)%2, t2 = (A[h]-1)/2;
			if(LEN.find(t1)==LEN.end()){
				t++;
				A[t] = t1;
				B[t] = B[h];
				LEN.insert(make_pair(A[t],t));
			//	printf("A1 %d %d %I64d %I64d %I64d %I64d\n",h,t,A[h],B[h],A[t],B[t]);
			}else{
				B[LEN.find(t1)->second]+=B[h];
			}
			if(LEN.find(t2)==LEN.end()){
				t++;
				A[t] = t2;
				B[t] = B[h];
				LEN.insert(make_pair(A[t],t));
			//	printf("A2 %d %d %I64d %I64d %I64d %I64d\n",h,t,A[h],B[h],A[t],B[t]);
			}else{
				B[LEN.find(t2)->second]+=B[h];
			}
			m-=B[h];
			h++;
		}
		printf("Case #%d: ",tt);
		printf("%I64d %I64d\n",(A[h]-1)/2+(A[h]-1)%2,(A[h]-1)/2);
	}
	return 0;
}
