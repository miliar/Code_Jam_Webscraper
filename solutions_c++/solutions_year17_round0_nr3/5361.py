#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<map>
#include<ctime>
using namespace std;
int T,n,m;

void work(){
	map<int,int> a;
	map<int,int>::iterator iter;
	int number,weight,v1,v2;
	a[n]=1;
	while(m>0){
		iter = --a.end();
		number = iter->first;
		weight = iter->second;
		//cout<<number<<" "<<weight<<endl;
		v2 = (number-1)/2; v1=max(0, number-1-v2);
		if(weight>=m){
			printf("%d %d\n",v1,v2);
			return;
			}
		else{
			if(a.count(v1)!=1) a[v1]=weight;
			else a[v1]+=weight;
			if(a.count(v2)!=1) a[v2]=weight;
			else a[v2]+=weight;
			a.erase(number);
			m-=weight;
			}
		}
	}
int main(){
	freopen("C-small-2-attempt1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(int k=1;k<=T;k++){
		printf("Case #%d: ",k);
		scanf("%d%d",&n,&m);
		work();
		}
	return 0;
	}
