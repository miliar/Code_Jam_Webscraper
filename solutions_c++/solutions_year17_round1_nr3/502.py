#include<iostream>
#include<queue>

#define MAXN 101

using namespace std;

struct str{
	int hd, ad, hk, ak;
};
int Hd,Ad,Hk,Ak,D,B;

str gen(int a, int b, int c, int d){
	str x;
	x.hd = a;
	x.ad = b;
	x.hk = c;
	x.ak = d;
	return x;
}

int t, res;
queue<str> Q;
vector<str> V;
int tab[MAXN][MAXN][MAXN][MAXN];

str akt, new_sit;

void wrzuc(str sit){
	if(tab[sit.hd][sit.ad][sit.hk][sit.ak] == 0){
		//cout << " Wrzucam: "<<sit.hd<<","<<sit.ad<<","<<sit.hk<<","<<sit.ak<<endl;
		tab[sit.hd][sit.ad][sit.hk][sit.ak] = (tab[akt.hd][akt.ad][akt.hk][akt.ak] + 1);
		Q.push(sit);
		V.push_back(sit);
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin >> t;
	for(int test = 0; test < t; test++){
		
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		tab[Hd][Ad][Hk][Ak] = 1;
		
		Q.push(gen(Hd,Ad,Hk,Ak));
		res = (-1);
		while(!Q.empty()){
			akt = Q.front();
			Q.pop();
			
			new_sit = akt;
			
			//1. zadaj obrazenia:
			new_sit.hk = akt.hk - akt.ad;
			if(new_sit.hk <= 0){
				res = tab[akt.hd][akt.ad][akt.hk][akt.ak];
				break;
			}
			else{
				new_sit.hd = akt.hd - akt.ak;
				if(new_sit.hd > 0){
					wrzuc(new_sit);
				}
			}
			
			//2. wylecz sie:
			new_sit = akt;
			new_sit.hd = Hd - akt.ak;
			if(new_sit.hd > 0){
				wrzuc(new_sit);
			}
			//3. buff ataku
			new_sit = akt;
			
			new_sit.ad = min(100, akt.ad + B);
			new_sit.hd = akt.hd - akt.ak;
			
			//cout<<"hd: "<<new_sit.hd<<endl;
			if(new_sit.hd > 0){
				wrzuc(new_sit);
			}
			//4. debuff knighta
			new_sit = akt;
			
			new_sit.ak = max(0, akt.ak - D);
			new_sit.hd = akt.hd - new_sit.ak;
			if(new_sit.hd > 0){
				wrzuc(new_sit);
			}
		}
		cout << "Case #"<<test+1<<": ";
		if(res == (-1))cout << "IMPOSSIBLE"<<endl;
		else cout<<res<<endl;
		//posprzataj i clear na queue
		tab[Hd][Ad][Hk][Ak] = 0;
		for(int i = 0; i < V.size(); i++){
			akt = V[i];
			tab[akt.hd][akt.ad][akt.hk][akt.ak] = 0;
		}
		while(!Q.empty()){
			Q.pop();
		}
	}

return 0;
}