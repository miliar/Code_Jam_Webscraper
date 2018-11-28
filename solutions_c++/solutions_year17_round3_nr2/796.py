#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;

bool comp(pair<int, int> a, pair<int, int> b){
	return a < b;
}

bool mycontain(pair<int, int> a, int b){
	if(b>=a.first && b<=a.second)return true;
	else return false;
}

int main(){
	int tt;
	cin >> tt;
	
	int m, n;
	for(int it = 0; it < tt; it ++){		
		cin >> m >> n;
		
		vector<pair<int, int> > p(m);
		vector<pair<int, int> > q(n);
		
		
		for(int i = 0; i < m; i ++)cin >> p[i].first >> p[i].second;
		for(int i = 0; i < n; i ++)cin >> q[i].first >> q[i].second;
		if(m > 0)sort(p.begin(), p.end(), comp);
		if(n > 0)sort(q.begin(), q.end(), comp);
		
		int count = 0;
		
		if(m<=1 && n <=1)count = 2;
		else if(m == 2){
			if(n == 0){
				if(p[1].first-p[0].second >= 720 || 1440-p[1].second+p[0].first>= 720)count = 2;
				else count = 4;
			}
			else if(n == 1){
				if(q[0].first >= p[0].second && q[0].second <= p[1].first){
					if(p[1].first-p[0].second >= 720)count = 2;
					else count = 4;
				}
				else{
					if(1440-p[1].second+p[0].first>= 720)count = 2;
					else count = 4;
				}
			}
			else{
				count=0;
			}
		}
		else{
			if(m == 0){
				if(q[1].first-q[0].second >= 720 || 1440-q[1].second+q[0].first>= 720)count = 2;
				else count = 4;
			}
			else{
				if(p[0].first >= q[0].second && p[0].second <= q[1].first){
					if(q[1].first-q[0].second >= 720)count = 2;
					else count = 4;
				}
				else{
					if(1440-q[1].second+q[0].first>= 720)count = 2;
					else count = 4;
				}
			}
		}
		
		cout << "Case #" << it + 1 << ": " << count << endl;
		
	}
	return 0;
} 
