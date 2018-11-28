#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<vector>
#include<stack>
#define gc getchar_unlocked
using namespace std;
typedef long long int int64;
int main()
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int64 i,j,k,n,m,t,a1,cnt=1,a2,v,ls,rs;
cin>>t;
while(t--) {
	scanf("%lld %lld",&n,&k);
	priority_queue<int64> q;
	q.push(n);
	i=0;ls=rs=0;
	while(!q.empty()){
		v = q.top();
		q.pop();
		//cout<<i<<" size: "<<v<<endl;
		i++;
		if(i==k){
			if(v%2==0){
				if(v/2>0)rs=v/2;
				if((v/2)-1>0)ls=(v/2)-1;
			} else {
				if(v/2>0)
				ls=rs=v/2;
			}
			break;
		}
		if(v%2==0){
			if (v/2>0) {q.push(v/2);}
			if (((v/2)-1)>0){q.push((v/2)-1);}
			//cout<<"pushed :"<<v/2<<" "<<((v/2)-1)<<endl;
		} else {
			if(v/2>0){
				q.push(v/2);
				q.push(v/2);
			}
			//cout<<"pushed :"<<v/2<<" "<<v/2<<endl;
		}
	}
	printf("Case #%lld: %lld %lld\n",cnt,max(ls,rs),min(ls,rs));
	cnt++;	
}
return 0;
}
 