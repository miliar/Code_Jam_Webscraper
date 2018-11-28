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
int64 d[1100],k,n,ar[10];

vector<int64> getChild(int64 a){
	int64 i,j,vl,pw,w;
	for(i=0;i<n;i++)ar[i]=0;
	i=0;
	while(a>0){
		ar[i]=a%2;
		a/=2;
		i++;
	}
	//cout<<"baap array: ";
	//for(i=0;i<n;i++)cout<<ar[i]<<" ";cout<<endl;cout<<"children"<<endl;
	vector<int64> res;
	for(i=0;i+k-1<n;i++){
		for(j=i,w=0;w<k;w++,j++){
			ar[j]=!ar[j];
		}
		//for(j=0;j<n;j++)cout<<ar[j]<<" ";cout<<endl;
		vl=0;pw=1;for(j=0;j<n;j++){vl+=ar[j]*pw;pw*=2;}
		res.push_back(vl);
		for(j=i,w=0;w<k;w++,j++){
			ar[j]=!ar[j];
		}
	}
	return res;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
int64 i,j,m,w,sum,ans,t,tmp,ist,pr=-1,cnt=1,a1,v,vl,pw;
cin>>t;
char str[100];
while(t--) {
	scanf("%s %lld",str,&k);
	n=strlen(str);
	for(i=0;i<1100;i++)d[i]=-1;
	d[0]=0;
	queue<int64> q;q.push(0);
	while(!q.empty()){
		v = q.front();
		q.pop();
		//cout<<"bfs :"<<v<<endl;
		vector<int64> children = getChild(v);
		for(i=0;i<children.size();i++){
		//	cout<<v<<" and its child:"<<children[i]<<endl;
			if(d[children[i]]==-1){
				d[children[i]]=d[v]+1;
				q.push(children[i]);
			}
		}
	}
	//for(i=0;i<10;i++)cout<<i<<" "<<d[i]<<endl;
	vl=0;pw=1;
	for(i=0;i<n;i++){
		if(str[i]=='-')vl+=pw;
		pw*=2;
	}
	if(d[vl]==-1){
		printf("Case #%lld: IMPOSSIBLE\n",cnt);
	} else{
		printf("Case #%lld: %lld\n",cnt,d[vl]);	
	}
	cnt++;
	//cout<<str<<" "<<k<<endl;
}	
return 0;
}
 