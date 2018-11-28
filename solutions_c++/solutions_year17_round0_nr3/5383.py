/*input
5
4 2
5 2
6 2
1000 1000
1000 1
*/
#include <bits/stdc++.h>
#define X first
#define Y second
#define REP(i,n) for(int i=0;i<n;i++)
#define ENDL printf("\n")
#define PI pair<long long,long long>
using namespace std;
map <long long,long long> M;
long long a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z;
int main(){
	scanf(" %I64d",&t);
	for(l=1;l<=t;l++){
		printf("Case #%I64d: ",l);
		scanf(" %I64d %I64d",&n,&k);
		M[n]=1;
		map<long long,long long>::iterator it;
		while(1){
			it = M.end();
			it--;
			k-=(*it).Y;
			m = ((*it).X)-1;
			if(k<=0){
				printf("%I64d %I64d\n",m/2+(m%2),m/2);
				break;
			}
			M.erase(it);
			M[m/2]+=(*it).Y;
			M[m/2+(m%2)]+=(*it).Y;
		}
		M.clear();
	}
	return 0;
}