#include <bits/stdc++.h>
using namespace std;

int main() {
	int T, n, r, o, y, g, b, v;
	bool flag = 0;
	string str;

	cin >> T;

	for (int t=1 ; t<=T ; ++t) {
		cout << "Case #" << t << ": ";

		cin >> n >> r >> o >> y >> g >> b >> v;

		str = "";
		flag = 0;

		r -= g;
		y -= v;
		b -= o;

		if (b < 0 || y < 0 || r < 0) {
			printf("IMPOSSIBLE\n");
			continue;
		}

		priority_queue < pair < pair <int, int>, char> > pq;
		if (r)
			pq.push({{r, r}, 'R'});
		if (y)
			pq.push({{y, y}, 'Y'});
		if (b)
			pq.push({{b, b}, 'B'});
		
		
		while(!pq.empty()){
			auto y = pq.top();
			--y.first.first;
			str += y.second;
			// fn(4);
			pq.pop();
			if(!pq.empty()){
				auto z = pq.top();
				--z.first.first;
				pq.pop();
				if(z.first.first != 0) pq.push(z);
				str += z.second;
			}
			if(y.first.first != 0) pq.push(y);
		}

		for(int i=0; i<str.length()-1 ; i++)
			if(str[i]==str[i+1])
				flag=1;

		if (flag || (str.length() && str[0]==str[str.length()-1])) {
			printf("IMPOSSIBLE\n");
			continue;
		}

		if(o >= 1){
			string temp="";
			for(int i=0;i<o;i++){
				temp += "BO";
			}
			if(b>=1){
				str.insert(str.find('B'), temp);
			}
			else if(n==(2*o) && b==0){
				str+=str;
			}
			else flag=1;
		}

		if(v>=1){
			string temp="";
			for(int i=1;i<=v;i++){
				temp+="YV";
			}
			if(y>=1)
				str.insert(str.find('Y'), temp);
			else if(n==(2*v) && y==0){
				str = temp + str;
			}
			else flag = 1;
		}

		if(g>=1){
			string temp="";
			for(int i=0;i<g;i++){
				temp+="RG";
			}
			if(r>=1){
				str.insert(str.find('R'), temp);
			}
			else if(n==(2*g) && r==0){
				str=temp+str;
			}
			else flag=1;
		}

		if (!flag)
			cout << str << endl;
		else
			cout << "IMPOSSIBLE\n";
	}
}