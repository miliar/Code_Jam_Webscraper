#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
#include<math.h>

#define ll long long
using namespace std;

ll n,m;
map<ll,ll>mp;

void sol(){
	mp.clear();
	mp[n]=1;
	while(true){
		if(mp.rbegin()->second>=m){
			printf("%I64d %I64d\n",(mp.rbegin()->first-1)-(mp.rbegin()->first-1)/2,(mp.rbegin()->first-1)/2);
			return;
		}
		mp[(mp.rbegin()->first-1)/2]+=mp.rbegin()->second;
		mp[(mp.rbegin()->first-1)-(mp.rbegin()->first-1)/2]+=mp.rbegin()->second;
		m-=mp.rbegin()->second;
		mp.erase(mp.rbegin()->first);
	}

}


int st[1007];


int fr(int i){
	int j=0;
	i++;
	while(st[i]!=1){
		i++;
		j++;
	}
	return j;
}


int fl(int i){
	int j=0;
	i--;
	while(st[i]!=1){
		i--;
		j++;
	}
	return j;
}

void silly(){
	int i,j;
	for(i=0;i<1007;i++)st[i]=0;
	st[0]=1;
	st[n+1]=1;
	int mni,mn,mx;
	for(i=0;i<m;i++){
		mn=-1,mx=-1;
		for(j=1;j<=n;j++){
			if(st[j]==0){
				int x=min(fl(j),fr(j)),y=max(fl(j),fr(j));
				if(x>mn||(x==mn&&y>mx)){
					mni=j;
					mn=x;
					mx=y;
				}
			}
		}
		st[mni]=1;
	}
	printf("%d %d\n",max(fr(mni),fl(mni)),min(fr(mni),fl(mni)));
}

int main(){
#pragma comment(linker, "/STACK:1073741824")
#ifdef _DEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#else
	//freopen("input_file.txt","r",stdin);
	//freopen("output_file.txt","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%I64d%I64d",&n,&m);
		printf("Case #%d: ",i+1);
		//printf("Case #%d:\n",i+1);
		//silly();
		sol();
	}
	return 0;
}