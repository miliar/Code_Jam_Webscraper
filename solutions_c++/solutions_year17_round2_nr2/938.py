#include <bits/stdc++.h>

using namespace std;
int main(){
	int tc,tci=1;cin>>tc;
	while(tc-->0){
		int n,r,o,y,g,b,v;cin>>n>>r>>o>>y>>g>>b>>v;
		int tr,to,ty,tg,tb,tv;tr=r;to=o;ty=y;tg=g;tb=b;tv=v;
		string ans="";
		y-=v;b-=o;r-=g;
		int ma=max(r,max(b,y));
		if(r+y+b-ma<ma||r<0||b<0||g<0){
			cout<<"Case #"<<tci++<<": "<<"IMPOSSIBLE"<<endl;
			continue;
		}
		if(ma==r){
			int dif=(y+b-r);
			assert(dif>=0);
			for(int i=0;i<dif;i++){ans+="RBY";}
//			y-=dif;b-=dif;r-=dif;
			for(int i=0;i<y-dif;i++){ans+="RY";}
			for(int i=0;i<b-dif;i++){ans+="RB";}
		}else if(ma==y){
			int dif=(r+b-y);
			assert(dif>=0);
			for(int i=0;i<dif;i++)ans+="YBR";
//			y-=dif;b-=dif;r-=dif;
			for(int i=0;i<b-dif;i++)ans+="YB";
			for(int i=0;i<r-dif;i++)ans+="YR";
		}else{
			int dif=(r+y-b);
			assert(dif>=0);
			for(int i=0;i<dif;i++)ans+="BYR";
//			y-=dif;b-=dif;r-=dif;
			for(int i=0;i<r-dif;i++)ans+="BR";
			for(int i=0;i<y-dif;i++)ans+="BY";
		}
		if(v>0){
			if(y==0&&ans.size()>0){
				cout<<"Case #"<<tci++<<": "<<"IMPOSSIBLE"<<endl;
				continue;
			}else if(y==0){
				for(int i=0;i<v;i++)ans=ans+"VY";
			}else{
				int brk;
				for(int i=0;i<ans.size();i++)if(ans[i]=='Y')brk=i;
				string ans1=ans.substr(0,brk+1);
				for(int i=0;i<v;i++)ans1=ans1+"VY";
				ans1=ans1+ans.substr(brk+1);
				ans=ans1;
			}
		}
		if(o>0){
			if(b==0&&ans.size()>0){
				cout<<"Case #"<<tci++<<": "<<"IMPOSSIBLE"<<endl;
				continue;
			}else if(b==0){
				for(int i=0;i<o;i++)ans=ans+"OB";
			}else{
				int brk;
				for(int i=0;i<ans.size();i++)if(ans[i]=='B')brk=i;
				string ans1=ans.substr(0,brk+1);
				for(int i=0;i<o;i++)ans1=ans1+"OB";
				ans1=ans1+ans.substr(brk+1);
				ans=ans1;
			}
		}
		if(g>0){
			if(r==0&&ans.size()>0){
				cout<<"Case #"<<tci++<<": "<<"IMPOSSIBLE"<<endl;
				continue;
			}else if(r==0){
				for(int i=0;i<g;i++)ans=ans+"GR";
			}else{
				int brk;
				for(int i=0;i<ans.size();i++)if(ans[i]=='R')brk=i;
				string ans1=ans.substr(0,brk+1);
				for(int i=0;i<g;i++)ans1=ans1+"GR";
				ans1=ans1+ans.substr(brk+1);
				ans=ans1;
			}
		}
		cout<<"Case #"<<tci++<<": "<<ans<<endl;
		int cr=0,cb=0,cy=0,co=0,cg=0,cv=0;
		for(int i=0;i<ans.size();i++){
			assert(ans[i]!=ans[(i+1)%ans.size()]);
			if(ans[i]=='R')cr++;
			if(ans[i]=='G')cg++;
			if(ans[i]=='Y')cy++;
			if(ans[i]=='B')cb++;
			if(ans[i]=='O')co++;
			if(ans[i]=='V')cv++;
		}
		if(cr!=tr||cg!=tg||cv!=tv||co!=to||cb!=tb||cy!=ty){
			cout<<"ERROR"<<endl;
			break;
		}
	}
	return 0;
} 
