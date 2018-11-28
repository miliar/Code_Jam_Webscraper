#include <iostream>
#include <queue>
#include <map>
using namespace std;

struct node{
	int Hd,Ad,Hk,Ak;
	int turn;
};
int code(node x){
	return x.Hd*1000000+x.Ad*10000+x.Hk*100 + x.Ak;
}
map<int,bool> vsted;
struct cmp{
	bool operator() (node a, node b){
		return a.turn > b.turn;
	}
};

int main(){
	int t; cin >> t;
	for (int i=0;i<t;i++){
		vsted.clear();
		int hd,ad,hk,ak,b,d;
		cin >> hd >> ad >> hk >> ak >> b >> d;
		priority_queue<node,vector<node>,cmp> q;
		q.push((node){hd,ad,hk,ak,0});
		bool found = false;
		while (!q.empty()){
			node x = q.top(); q.pop();
			if (vsted[code(x)]) continue;
			if (x.Hk<= 0) {
				found = true;
				cout << "Case #" << i+1 << ": " << x.turn << endl;
				break;
			}
			if (x.Hd <= 0) continue;
			//if (x.Hd > x.Ak){
				q.push((node){x.Hd-x.Ak,x.Ad,x.Hk-x.Ad,x.Ak,x.turn+1}); //attack
				q.push((node){x.Hd-x.Ak,x.Ad+b,x.Hk,x.Ak,x.turn+1}); //buff
		//	}
			if (d!=0 && x.Ak != 0){
				int Ak = x.Ak-d;
				if (Ak < 0) Ak = 0;
				q.push((node){x.Hd-Ak,x.Ad,x.Hk,Ak,x.turn+1}); //debuff
			}
			q.push((node){hd-x.Ak,x.Ad,x.Hk,x.Ak,x.turn+1}); //heal
			vsted[code(x)] = true;
		}
		if (!found) cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
	}	
}
