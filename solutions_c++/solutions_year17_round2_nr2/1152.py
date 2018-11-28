#include <bits/stdc++.h>
using namespace std;
int u, t=1, n, i, p, r[6], c[6];	//R O Y G B V
char dic[6]={'R','O','Y','G','B','V'};
bool flag;
int mx(){
	pair<int, pair<int, int>> tmp[3]={{c[0],{r[0],0}}, {c[2],{r[2],2}}, {c[4],{r[4],4}}};
	sort(tmp, tmp+3);
	if(tmp[2].second.second==p)
		return tmp[1].second.second;
	return tmp[2].second.second;
}
int main(){
	for(cin>>u; t<=u; t++){
		i=0, flag=true;
		for(cin>>n; i<6; i++)
			cin>>c[i];
		for(i=0; i<6; i++)
			if(c[i]*2>n)
				flag=false;
		int tmp=6;
		p=7, p=mx(), tmp-=p;
		r[p]=3;
		p=mx(), tmp-=p;
		r[p]=2;
		r[tmp]=1;
		cout<<"Case #"<<t<<": ";
		if(!flag){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		i=0, p=7;
		for(i=0; i<n; i++){
			p=mx();
			cout<<dic[p];
			c[p]--;
		}
		cout<<endl;
	}
	return 0;
}
