#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<string>
#include<iomanip>

#define MIDN 1440
#define INF 99999999
#define MAXN 1003

using namespace std;

int t;
int n;

struct act{
	int pocz, kon;	
};

bool operator<(const act &a, const act &b){
	if(a.pocz < b.pocz)return 1;
	return 0;	
}

act jamie[MAXN];
act cameron[MAXN];

//vector<act> cameron;
vector<act> jamie_time;
act pom;

int aJ, aC;

int il_czasu_jamie;
int best_ind, best_dlug, dlugosc;
int res;
int main(){
	ios_base::sync_with_stdio(0);
	
	cin >> t;
	
	for(int test = 1; test <= t; test++){
		cin >> aC >> aJ;
		
		for(int i = 0; i < aC; i++){
			cin >> cameron[i].pocz >> cameron[i].kon;
		}
		for(int i = 0; i < aJ; i++){
			cin >> jamie[i].pocz >> jamie[i].kon;	
		}
		
	//	sort(jamie, jamie+aJ);
		if(((aC == 0) && (aJ == 1)) || ((aC == 1) && (aJ == 0))){
			res = 2;	
		}
		else{
			
			if(aC == 0){
				for(int i = 0; i < aJ; i++){
					cameron[i] = jamie[i];
				}
				aC = aJ;
			}
			sort(cameron, cameron + aC);
			if(aC == 1 && aJ == 1){
				res = 2;	
			}
			else{
				if(((cameron[1].kon - cameron[0].pocz) <= 720) || ((MIDN - cameron[1].pocz + cameron[0].kon) <= 720)){
					res = 2;	
				}
				else{
					res = 4;	
				}
			}
		}
		cout << "Case #"<<test<<": "<<res;
		
		cout << endl;	
	}
	
	cout << endl;
	return 0;
}
