#include <bits/stdc++.h>

using namespace std;
#define pb push_back
#define mp make_pair
typedef long long int ll;

int r,c;

vector<string> cak;
vector<bool> f;

ifstream in("A-large.in");
ofstream out("output");

bool dikeyg(int in, int jn, int sal, int sus, int v){
	if(v==-1)
		return 0;
	if(v==r)
		return 0;
	for(int i = sal;i<=sus;i++){
		if(cak[v][i]!='?'){
			return 0;
		}
	}
	for(int i = sal;i<=sus;i++){
		cak[v][i] = cak[in][jn];
	}
	return 1;
}

bool yatayg(int in, int jn, int sal, int sus, int v){
	if(v==-1)
		return 0;
	if(v==c)
		return 0;
	for(int i = sal;i<=sus;i++){
		if(cak[i][v]!='?'){
			return 0;
		}
	}
	for(int i = sal;i<=sus;i++){
		cak[i][v] = cak[in][jn];
	}
	return 1;
}

void dikey(int in, int jn){
	int sal = in, sus = in;
	for(int i = in-1;i>=0;i--){
		if(cak[i][jn]=='?'){
			cak[i][jn] = cak[in][jn];
			sal = i;
		}else{
			break;
		}
	}
	for(int i = in+1;i<r;i++){
		if(cak[i][jn]=='?'){
			cak[i][jn] = cak[in][jn];
			sus = i;
		}else{
			break;
		}
	}
	if(sal==in&&sus==in)
		return;
	int v = jn +1;
	while(yatayg(in, jn, sal, sus, v)){
		v++;
	}
	v = jn-1;
	while(yatayg(in,jn, sal, sus, v)){
		v--;
	}

}

void yatay(int in, int jn){
	int sal = jn, sus = jn;

	for(int i = jn-1;i>=0;i--){
		if(cak[in][i]=='?'){
			cak[in][i] = cak[in][jn];
			sal = i;
		}else{
			break;
		}
	}
	for(int i = jn+1;i<c;i++){
		if(cak[in][i]=='?'){
			cak[in][i] = cak[in][jn];
			sus = i;
		}else{
			break;
		}
	}
	if(sus==jn&&sal==jn)
		return;
	int v = in +1;
	while(dikeyg(in, jn, sal, sus, v)){
		v++;
	}
	v = in-1;
	while(dikeyg(in,jn, sal, sus, v)){
		v--;
	}

}

void solve(int in, int jn){
	if(in>0&&in<r){
		if(cak[in-1][jn]=='?'){
			//out<<"yukari"<<endl;
			dikey(in,jn);
			return;
		}
	}
	if(in>=0&&in<(r-1)){
		if(cak[in+1][jn]=='?'){
			//out<<"asagi"<<endl;
			dikey(in,jn);
			return;
		}
	}

	if(jn>0&&jn<c){
		if(cak[in][jn-1]=='?'){
			//out<<"sola"<<endl;
			yatay(in,jn);
			return;
		}
	}

	if(jn>=0&&jn<(c-1)){
		if(cak[in][jn+1]=='?'){
			//out<<"saga"<<endl;
			yatay(in,jn);
			return;
		}
	}
}

void bsol(int in, int jn){
	for(int i = in+1;i<r;i++){
		if(cak[i][jn]!='?'&&!f[cak[i][jn]-'A']){
			dikey(i,jn);
			f[cak[i][jn]-'A'] = 1;
			return;
		}
	}
	for(int i = in-1;i>=0;i--){
		if(cak[i][jn]!='?'&&!f[cak[i][jn]-'A']){
			dikey(i,jn);
			f[cak[i][jn]-'A'] = 1;
			return;
		}
	}
	for(int i = jn-1;i>=0;i--){
		if(cak[in][i]!='?'&&!f[cak[in][i]-'A']){
			yatay(in,i);
			f[cak[in][i]-'A'] = 1;
			return;
		}
	}
	for(int i = jn+1;i<c;i++){
		if(cak[in][i]!='?'&&!f[cak[in][i]-'A']){
			yatay(in,i);
			f[cak[in][i]-'A'] = 1;
		}
	}
}


int main() {
	
	int t;
	in>>t;

	string ro;
	for(int i = 1;i<=t;i++){
		out<<"Case #"<<i<<": "<<endl;
		in>>r>>c;
		
		cak.clear();
		f.clear();

		f.resize(27,0);
		
		cak.resize(r+1);

		
		
		for(int i = 0;i<r;i++)
			in>>cak[i];
		for(int i = 0;i<r;i++){
			for(int j = 0;j<c;j++){
				if(cak[i][j]=='?'){
					bsol(i,j);
				}
			}
		}
		for(int i = 0;i<r;i++)
			out<<cak[i]<<endl;

	}


	
	out.close();
	return 0;
}