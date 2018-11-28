#include <bits/stdc++.h>
#define fr(x) scanf("%d", &x)
using namespace std;

priority_queue<pair<pair<int,int>,char>> pq;

int main(){
	int t, n, r, o, y, g, b, v;
	bool flag=0;
	fr(t);
	string str;

	for(int t1=1; t1<=t ;++t1){
		printf("Case #%d: ", t1);
		fr(n);
		fr(r);
		fr(o);
		fr(y);
		fr(g);
		fr(b);
		fr(v);

		str="";
		flag=0;

		b-=o;
		y-=v;
		r-=g;

		if(b>0) pq.push({{b, b}, 'B'});
		if(r>0) pq.push({{r, r}, 'R'});
		if(y>0) pq.push({{y, y}, 'Y'});
		
		if(b<0) flag=1;
		if(y<0) flag=1;
		if(r<0) flag=1;
		
		while(!pq.empty()){
			auto y=pq.top();
			pq.pop();
			--y.first.first;
			str+=y.second;
			if(!pq.empty()){
				auto z=pq.top();
				pq.pop();
				--z.first.first;
				str+=z.second;
				if(z.first.first) pq.push(z);
			}
			if(y.first.first) pq.push(y);
		}

		for(int i=1; i<str.length(); ++i){
			if(str[i]==str[i-1]){
				flag=1;
			}
		}
		if(str.length() && str[0]==str[str.length()-1]) flag=1;

		if(o>0){
			string temp="";
			for(int i=1;i<=o;++i){
				temp+="BO";
			}
			if(b>0){
				str.insert(str.find('B'), temp);
			}
			else if(b==0 && n==(2*o)){
				str=temp+str;
			}
			else flag=1;
		}

		if(v>0){
			string temp="";
			for(int i=1;i<=v;++i){
				temp+="YV";
			}
			if(y>0){
				str.insert(str.find('Y'), temp);
			}
			else if(y==0 && n==(2*v)){
				str=temp+str;
			}
			else flag=1;
		}

		if(g>0){
			string temp="";
			for(int i=1;i<=g;++i){
				temp+="RG";
			}
			if(r>0){
				str.insert(str.find('R'), temp);
			}
			else if(r==0 && n==(2*g)){
				str=temp+str;
			}
			else flag=1;
		}

		if(flag) puts("IMPOSSIBLE");
		else cout<<str<<"\n";
	}
	return 0;
}