#include<iostream>
#include<string>
using namespace std;

string string_maker(string c1, string c2, string c3, string a1, string a2, string a3, int n1,int n2,int n3,string ans){
	
	if (n1==0) return ans;
	string h = ans.append(a1);
	int nn2 = n2, nn3 = n3;
	if (n2!=0){
			h = h.append(a2);
			nn2= nn2-1;}
	if(n3 == n1){
		h = h.append(a3);
		nn3=nn3-1;
	}
	return string_maker(c1,c2,c3,c1,c2,c3,n1-1,nn2,nn3,h);
}

int main(){
	long T;
	cin>>T;
	for (int i=0;i<T;i++){
		int n,r,o,y,b,g,v;
		cin>>n>>r>>o>>y>>g>>b>>v;
		if ((b<o) || (r<g) || (y<v) || ((b-o)>((r-g)+(y-v))) || ((r-g)>((b-o)+(y-v))) || ((y-v)>((r-g)+(b-o))) || (b==o&&o!=0&&(r!=0||y!=0))||
		(r==g&&g!=0&&(b!=0||y!=0)) ||(y==v&&v!=0&&(r!=0||b!=0)) )
			cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
		else if (b==o&&o!=0){
			string ans = "";
			for (int j=0;j<b;j++){
				ans=ans.append("BO");
			}
			cout<<"Case #"<<i+1<<": "<<ans<<endl;
		}
		else if (r==g&&g!=0){
			string ans = "";
			for (int j=0;j<g;j++){
				ans=ans.append("RG");
			}
			cout<<"Case #"<<i+1<<": "<<ans<<endl;
		}
		else if (y==v&&v!=0){
			string ans = "";
			for (int j=0;j<v;j++){
				ans=ans.append("VY");
			}
			cout<<"Case #"<<i+1<<": "<<ans<<endl;
		}
		else {
			string oo="B",gg="R",vv="Y";
			for(int j=0;j<o;j++){
				oo=oo.append("OB");
			}
			for(int j=0;j<g;j++){
				gg=gg.append("GR");
			}
			for(int j=0;j<v;j++){
				vv=vv.append("VY");
			}
			int B=b-o,R=r-g,Y=y-v;
			if (B>=R && B>=Y) cout<<"Case #"<<i+1<<": "<<string_maker("B","R","Y",oo,gg,vv,B,R,Y,"")<<endl;
			else if (R>=B && R>=Y) cout<<"Case #"<<i+1<<": "<<string_maker("R","B","Y",gg,oo,vv,R,B,Y,"")<<endl;
			else cout<<"Case #"<<i+1<<": "<<string_maker("Y","R","B",vv,gg,oo,Y,R,B,"")<<endl;
		}

	}
}