#include<bits/stdc++.h>
#define LIM 5555
using namespace std;
int R ,B ,Y , O , G , V , n;
int c[LIM];

bool cmp(char x,char y){
	return c[x] > c[y];
}
string RAW(int nR,int nB,int nY){
	string Id , ret;
	c['R'] = nR ; c['B'] = nB ; c['Y'] = nY;
	Id = "RBY";
	sort(Id.begin() , Id.end() , cmp);
	vector < string > all;
	for(int i = 1 ; i <= c[Id[0]] ; i++){
		string x; x += Id[0];
		all.push_back(x);
	}
	c[Id[0]] = 0;
	for(int i = 0 ; i < all.size() ; i++){
		if(c[Id[1]] > 0){
			all[i] += Id[1]; c[Id[1]]--;
		}
		else{
			all[i] += Id[2]; c[Id[2]]--;
		}
	}
	for(int i = 0 ; i < c[Id[2]] ; i++) all[i] += Id[2];
	c[Id[2]] = 0;
	for(int i = 0 ; i < all.size() ; i++)	ret += all[i];
	assert(c['R'] == 0 && c['B'] == 0 && c['Y'] == 0);
	return ret;
}

string Get(int nO,int nG,int nV){
	vector < string > nR , nB , nY;
	/*Green*/
	for(int i = 1 ; i <= nG ; i++){
		if(i < nG){
			nR.push_back("RGR");
			R -= 2 ; G -= 1;
		}
		else{
			string s = "";
			for(int j = 1 ; j <= G ; j++) s += "RG";
			s += "R";
			R -= (G + 1); G = 0;
			nR.push_back(s);
		}
	}
	/*Orange*/
	for(int i = 1 ; i <= nO ; i++){
		if(i < nO){
			nB.push_back("BOB");
			B -= 2 ; O -= 1;
		}
		else{
			string s = "";
			for(int j = 1 ; j <= O ; j++) s += "BO";
			s += "B";
			B -= (O + 1); O = 0;
			nB.push_back(s);
		}
	}	
	/*Violet*/
	for(int i = 1 ; i <= nV ; i++){
		if(i < nV){
			nY.push_back("YVY");
			Y -= 2 ; V -= 1;
		}
		else{
			string s = "";
			for(int j = 1 ; j <= V ; j++) s += "YV";
			s += "Y";
			Y -= (V + 1); V = 0;
			nY.push_back(s);
		}
	}
	for(int i = 1 ; i <= R ; i++)	nR.push_back("R"); 
	for(int i = 1 ; i <= Y ; i++)	nY.push_back("Y");
	for(int i = 1 ; i <= B ; i++)	nB.push_back("B");
	R = 0 ; Y = 0 ; B = 0;
	assert(R == 0 && Y == 0 && B == 0 && V == 0 && O == 0 && G == 0);
	string cur , ans;
	cur = RAW(nR.size() , nB.size() , nY.size());
	for(int i = 0 ; i < cur.size() ; i++){
		if(cur[i] == 'R'){
			ans += nR.back(); nR.pop_back();
		}
		else if(cur[i] == 'Y'){
			ans += nY.back(); nY.pop_back();
		}
		else{
			ans += nB.back() ; nB.pop_back();
		}
	}
	assert(ans.size() == n);
	return ans;
}

void solve(int Tc){
	scanf("%d %d %d %d %d %d %d",&n,&R,&O,&Y,&G,&B,&V);
	string ans = "IMPOSSIBLE";
	if(R == G && R + G == n){
		ans = "";
		for(int i = 1 ; i <= R ; i++)	ans += "RG";
	}
	if(B == O && B + O == n){
		ans = "";
		for(int i = 1 ; i <= B ; i++)	ans += "BO";
	}
	if(Y == V && Y + V == n){
		ans = "";
		for(int i = 1 ; i <= Y ; i++)	ans += "YV";		
	}
	for(int nO = 0 ; nO <= O ; nO++){
		if(O + nO > B || ( ((O > 0)^(nO > 0)) == 1) )	continue;
		for(int nG = 0 ; nG <= G ; nG++){
			if(G + nG > R || ( ((G > 0)^(nG > 0)) == 1) )	continue;
			for(int nV = 0 ; nV <= V ; nV++){
				if(V + nV > Y || ( ((V > 0)^(nV > 0)) == 1) )	continue;
				int cB = B - O , cR = R - G , cY = Y - V;
				if(cB > cR + cY) continue;
				if(cR > cB + cY)	continue;
				if(cY > cR + cB)	continue;
				ans = Get(nO , nG , nV);
				break;
			}
		}
	}
	printf("Case #%d: ",Tc);
	cout<<ans<<'\n';
}

int main(){
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int Tc;
	scanf("%d",&Tc);
	for(int i = 1 ; i <= Tc ; i++) solve(i);
}
