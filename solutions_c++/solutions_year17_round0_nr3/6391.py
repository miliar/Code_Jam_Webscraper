#include<bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i=(int)a; i<(int)b; i++)
#define INF 0x3f3f3f3f

int main(){
	
	//freopen("C.in", "r", stdin);
	//freopen("Cout.txt", "w", stdout);
	
	int n, t, f;
	int bi = 1;
	cin>>n;
	
	while(n--){
		
		cin>>t>>f;
		
		int c = 0;
		
		priority_queue<pair<int, pair<int, int> > > q;
		
		q.push({t, {-1, t}});
		
		while(c < f){
			
			int a = -q.top().second.first;
			int b = q.top().second.second;
			int tam = q.top().first;
			int m = (a+b)/2;
			c++;
			
			//cout << a << " - " << b << " = " << m << endl;
			
			if(c==f){
				cout << "Case #" << bi++ << ": ";
				int aa = m-a;
				int bb = b-m;
				cout << max(aa, bb) << " " << min(aa, bb) << endl;
			}
			
			q.pop();
			
			q.push({b-m, {-(m+1), b}});
			q.push({m-a, {-a, m-1}});
		}
			
	}
	
	return 0;
}
