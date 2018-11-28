#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define MP make_pair

const int MAXM=1000;

int N,C,M;
int a[MAXM+1];
int b[MAXM+1];
int Link[MAXM+1];
bool used[MAXM+1];

void Init(){
	cin>>N>>C>>M;
	a[0]=0;
	b[0]=0;
	for(int i=1;i<=M;i++){
		int position,buyer; cin>>position>>buyer;
		if(buyer==1) a[++a[0]]=position;
		else b[++b[0]]=position;
	}
	sort(a+1,a+a[0]+1);
	sort(b+1,b+b[0]+1);
}

bool findp(int i){
	for(int j=1;j<=b[0];j++)
		if(a[i]!=b[j] && !used[j]){
			used[j]=true;
			if(Link[j]==-1 || findp(Link[j])){
				Link[j]=i;
				return true;
			}
		}
	return false;
}

void Solve(){
	for(int i=1;i<=b[0];i++) Link[i]=-1;
	
	int rused=0;
	for(int i=a[0];i>=1;i--){
		for(int j=1;j<=b[0];j++) used[j]=false;
		if(findp(i)) rused++;
	}
	
	int ans,cur;
	if(a[0]==rused){
		ans=rused+(b[0]-rused); cur=0;
	}else if(b[0]==rused){
		ans=rused+(a[0]-rused); cur=0;
	}else{
		int val;
		for(int i=1;i<=b[0];i++) if(Link[i]==-1) val=b[i];
		if(val>1){
			ans=rused+max(a[0]-rused,b[0]-rused);
			cur=min(a[0]-rused,b[0]-rused);
		}else{
			ans=rused+a[0]-rused+b[0]-rused;
			cur=0;
		}
	}
	cout<<ans<<" "<<cur<<"\n";
}

int main(){
	int Test; cin>>Test;
	for(int i=1;i<=Test;i++){
		Init();
		cout<<"Case #"<<i<<": ";
		Solve();
	}
}