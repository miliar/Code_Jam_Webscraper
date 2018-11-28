#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<string>

#define INF 99999999

using namespace std;

int t;
int n,r,o,y,g,b,v;

string greens, violets, oranges;

void std_oranges(){
	oranges = "";
	if(o == 0)return;
	
	oranges = "B";
	for(int i = 0; i < o; i++){
		oranges += "OB";	
	}
	b -= (o + 1);
	o = 0;
}
void std_greens(){
	greens = "";
	if(g == 0)return;
	
	greens = "R";
	for(int i = 0; i < g; i++){
		greens += "GR"; 
	}
	r -= (g+1);
	g = 0;	
}
void std_violets(){
	violets = "";
	if(v == 0)return;
	
	violets = "Y";
	for(int i = 0; i < v; i++){
		violets += "VY";	
	}
	y -= (v + 1);
	v = 0;		
}

string ogon;

void dodaj_ogon(char c){
	ogon += c;
	if(c == 'B')b--;	
	else if(c == 'Y')y--;
	else r--;
}	

bool dobry(string s){
	for(int i = 1; i < s.size(); i++){
		if(s[i] == s[i-1])
			return false;
	}
	return true;
}

bool zrob_std_colors(char first){
	int stary_b = b;
	int stary_y = y;
	int stary_r = r;
	ogon = first;
	
	while(b > 0 || r > 0 || y > 0){
		if(ogon[ogon.size() - 1] == 'Y'){
			if(b > r){
				dodaj_ogon('B');
			}
			else if(b < r){
				dodaj_ogon('R');	
			}
			else{
				if(first == 'B'){
					dodaj_ogon('B');
				}
				else{
					dodaj_ogon('R');	
				}
			}
		}
		else if(ogon[ogon.size() - 1] == 'B'){
			if(r > y){
				dodaj_ogon('R');
			}
			else if(r < y){
				dodaj_ogon('Y');	
			}
			else{
				if(first == 'R'){
					dodaj_ogon('R');
				}
				else{
					dodaj_ogon('Y');	
				}
			}
		}
		else{
			if(b > y){
				dodaj_ogon('B');
			}
			else if(b < y){
				dodaj_ogon('Y');	
			}
			else{
				if(first == 'B'){
					dodaj_ogon('B');
				}
				else{
					dodaj_ogon('Y');	
				}
			}		
		}	
	}
	ogon += first;
	bool zle = 0;
	
	if(b < 0 || y < 0 || r < 0)
		zle = 1;
	
	r = stary_r;
	b = stary_b;
	y = stary_y;
	
	if(zle == 1)return false;	
	
	return dobry(ogon);
}

string two_color(char f, char s, int n){
	string res = "";
	for(int i = 0; i < n; i++){
		res += f;
		res += s;
	}
	return res;
}

void impossible(){
	cout << "IMPOSSIBLE"<<endl;	
}
string utnij(string s){
	return s.substr(1, s.size() - 2);	
}

int main(){
	ios_base::sync_with_stdio(0);
	
	cin >> t;
	
	for(int test = 1; test <= t; test++){
		cin >> n >> r >> o >> y >> g >> b >> v;
	//	zle = 0;
		
		cout << "Case #"<<test<<": ";
		
		string res = "";
		
		if(o == 0 && g == 0 && v == 0){
			if(b > 0){
				b--;
				if(zrob_std_colors('B')){
					res = ogon;
				}
				b++;
			}
			if(y > 0){
				y--;
				if(zrob_std_colors('Y')){
					res = ogon;
				}
				y++;
			}
			if(r > 0){
				r--;
				if(zrob_std_colors('R')){
					res = ogon;
				}
				r++;
			}
			if(res == "")
				impossible();
			else
				cout << res.substr(0,res.size() - 1) << endl;
		
		//	cout << "po petli: b: "<<b<<" y: "<<y<<" r: "<<r<<endl;
		}
		else if(o == 0 && g == 0){
			if(r == 0 && b == 0){
				if(y == v){
					cout<<two_color('Y','V',y);	
				}
				else{
					impossible();	
				}
			}
			else{
				std_violets();
				if(y < 0){
					impossible();
				}
				else{
					if(zrob_std_colors('Y'))
						cout<<violets+utnij(ogon)<<endl;
					else 
						impossible();	
				}
			}
		}
		else if(o == 0 && v == 0){
			if(b == 0 && y == 0){
				if(g == r){
					cout <<two_color('G','R',g);	
				}
				else{
					impossible();	
				}
			}
			else{
				std_greens();
				if(r < 0){
					impossible();
				}
				else{
					if(zrob_std_colors('G'))
						cout<<greens+utnij(ogon)<<endl;
					else
						impossible();
				}
			}
		}
		else if(g == 0 && v == 0){
			if(r == 0 && y == 0){
				if(o == b){
					cout <<two_color('O','B',o);	
				}
				else{
					impossible();	
				}
			}
			else{
				std_oranges();
				if(b < 0){
					impossible();
				}
				else{
					if(zrob_std_colors('O'))
						cout <<oranges + utnij(ogon)<<endl;
					else
						impossible();	
				}
			}
		}
		else{
			//1. fajne:
			std_violets();
			std_greens();
			std_oranges();
			
			if((r < 0) || (y < 0) || (b < 0)){
				impossible();	
			}
			else{
				
			}
		}
	}
	
	cout << endl;
	return 0;
}
