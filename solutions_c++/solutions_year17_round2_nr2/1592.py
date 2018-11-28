#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair

using namespace std;

ll n,a,b,c,x,y,z;
char ach,bch,cch;

bool isok(ll p,ll q,ll r){

	if(q+r<p)return false;
	if(p+r<q-1)return false;
	if(p+q<r-1)return false;

	return true;
}

void ssort(){
	ach='R';
	bch='Y';
	cch='B';
	ll t;
	char tch;
	if(a<b){
		t=a;
		a=b;
		b=t;

		tch=ach;
		ach=bch;
		bch=tch;
	}

	if(b<c){
		t=b;
		b=c;
		c=t;

		tch=bch;
		bch=cch;
		cch=tch;
	}

	if(a<b){
		t=a;
		a=b;
		b=t;

		tch=ach;
		ach=bch;
		bch=tch;
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	ll t;
	int flag,ff;
	cin>>t;
	string s;
	ll cc;
	for(cc=1;cc<=t;cc++){
		cout<<"Case #"<<cc<<": ";
		s.clear();
		cin>>n>>a>>x>>b>>y>>c>>z;
		flag=0;
		ssort();

		if(!isok(a,b,c)){
			flag=1;
			goto next;
		}

		while(a>0 || b>0 || c>0){
			ff=0;
			int sz=s.size();
			char ch;
			if(sz>=1){
				ch=s[sz-1];
			}
			else{
				ch='Z';
			}

			if(a>=1 && ach!=ch && isok(a-1,b,c)){
				s.pb(ach);
				a--;
				ff=1;
				goto ne;
			}

			if(b>=1 && bch!=ch && isok(a,b-1,c)){
				s.pb(bch);
				b--; 
				ff=1;
				goto ne;
			}

			if(c>=1 && cch!=ch && isok(a,b,c-1)){
				s.pb(cch);
				c--;
				ff=1;
				goto ne;
			}
			
			ne:
			if(ff==0){
				flag=1;
				break;
			}
		}

		next:

		if(flag==1){
			cout<<"IMPOSSIBLE\n";
		}
		else{
			cout<<s<<endl;
		}
	}

	return 0;
}