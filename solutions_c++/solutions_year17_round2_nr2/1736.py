#include <bits/stdc++.h>
#define fi "B-small-attempt0.in"
#define fo "B-small-attempt0.out"

using namespace std;

class Unicorn{
	public:
		string color;
		int value;
};

bool compare(Unicorn a, Unicorn b){ return a.value < b.value; }

int main(){
    freopen(fi, "r", stdin);
	freopen(fo, "w", stdout);    
    // code here
    int t, n, r, o, y, g, b, v, max1, max2, max3, cmax1, cmax2, cmax3, c;
    Unicorn u[3];
    string result;
    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++){
    	printf("Case #%d: ", tt);
		scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
		if(r - g < 0 || y - v < 0 || b - o < 0){
			printf("IMPOSSIBLE\n");
			continue;
		}
    	Unicorn ur;
		ur.color = "R";
		ur.value = r - g;
		u[0] = ur;
    	Unicorn uy;
		uy.color = "Y";
		uy.value = y - v;
		u[1] = uy;
    	Unicorn ub;
		ub.color = "B";
		ub.value = b - o;
		u[2] = ub;
		sort(u, u + 3, compare);
		if(u[2].value > u[1].value + u[0].value){
			printf("IMPOSSIBLE\n");
			continue;			
		}
		result = "";
		for(int i = 0; i < u[2].value; i++){
			result += u[2].color;
		}
		for(int i = 0; i < u[1].value; i++){
			result.insert(2 * i + 1, u[1].color);
		}
		for(int i = 0; i < u[0].value; i++){
			result.insert(u[2].value + u[1].value + i - 2 * i, u[0].color);
		}
		if(r - g){
			c = 0;
			while(g > 0){
				if(result[c] == 'R'){
					result.insert(c + 1, "GR");
					g--;
					c += 2;
				}
				c++;
			}
		}
		else{
			for(int i = 0; i < g; i++){
				result += "GR";
			}			
		}
		if(y - v){
			c = 0;
			while(v > 0){
				if(result[c] == 'Y'){
					result.insert(c + 1, "VY");
					v--;
					c += 2;
				}
				c++;
			}
		}
		else{
			for(int i = 0; i < v; i++){
				result += "VY";
			}			
		}
		if(b - o){
			c = 0;
			while(o > 0){
				if(result[c] == 'B'){
					result.insert(c + 1, "OB");
					o--;
					c += 2;
				}
				c++;
			}
		}
		else{
			for(int i = 0; i < o; i++){
				result += "OB";
			}			
		}
		printf("%s\n", result.c_str());
	}
    
	return 0;
}
