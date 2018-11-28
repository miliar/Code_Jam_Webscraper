#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("B-small-attempt1.in","r",stdin);
	//freopen("out_b.txt","w",stdout);
	int t;
	char ans[1002];
	scanf("%d",&t);
	for(int T=1;T<=t;T++){
		int n,r,g,b,y,o,v;
		scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
		int idx=0;
		bool gg=g;
		while(g){
			ans[idx++]='R';
			ans[idx++]='G';
			g--,r--;
		}
		if(gg&&(o||b||y||v))ans[idx++]='R',r--;
		bool vv=v;
		while(v){
			ans[idx++]='Y';
			ans[idx++]='V';
			v--,y--;
		}
		if(vv&&(o||b||r||gg))ans[idx++]='Y',y--;
		bool oo=o;
		while(o){
			ans[idx++]='B';
			ans[idx++]='O';
			o--,b--;
		}
		if(oo&&(r||y||gg||vv))ans[idx++]='B',b--;
		char last;
		if(idx)last=ans[idx-1];
		else {
			if(r>=b&&r>=y)last=ans[idx++]='R',r--;
			else if(b>=r&&b>=y)last=ans[idx++]='B',b--;
			else last=ans[idx++]='Y',y--;
		}
		while((r>0||b>0||y>0)&&(idx<n)){
			if (last=='R'){
				if(b>y)last=ans[idx++]='B',b--;
				else if(y>b)last=ans[idx++]='Y',y--;
				else if(ans[0]=='Y')last=ans[idx++]='Y',y--;
				else last=ans[idx++]='B',b--;
			}
			else if(last=='B'){
				if(y>r)last=ans[idx++]='Y',y--;
				else if(r>y) last=ans[idx++]='R',r--;
				else if(ans[0]=='R')last=ans[idx++]='R',r--;
				else last=ans[idx++]='Y',y--;
			}
			else{//Y
				if(b>r)last=ans[idx++]='B',b--;
				else if(r>b)last=ans[idx++]='R',r--;
				else if(ans[0]=='R')last=ans[idx++]='R',r--;
				else last=ans[idx++]='B',b--;
			}
		}
		ans[idx]=0;
		if(ans[idx-1]==ans[0]||r<0||b<0||y<0)
			printf("Case #%d: IMPOSSIBLE\n",T);
		else printf("Case #%d: %s\n",T,ans);
	}

}
