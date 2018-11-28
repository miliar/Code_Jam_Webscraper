#include<iostream>
#include<queue>

#define MAXN 1003

using namespace std;

class interval{
	public:
	int a, b;
	interval(int q, int w): a(q), b(w){}
	interval(){
		a = b = 0;
	}
};

int l1, l2;
bool operator<(const interval &f, const interval &s){
	l1 = (f.b - f.a);
	l2 = (s.b - s.a);
	
	if(l1 < l2){
		return 1;
	}
	if(l1 == l2){
		if(f.a > s.a)
			return 1;
		return 0;
	}
	return 0;
}

int t, k, n;
int y, z;

priority_queue<interval> PQ;
interval beg_interval, cur_interval, new_interval1, new_interval2;

int cur_pos;

int main(){
	ios_base::sync_with_stdio(0);
	
	cin >> t;
	
	for(int test = 1; test <= t; test++){
		cin >> n >> k;
		
		beg_interval = interval(1,n);
		PQ.push(beg_interval);
		
		for(int i = 0; i < k; i++){
			cur_interval = PQ.top();
			
			PQ.pop();
			
			cur_pos = (cur_interval.a + cur_interval.b) / 2;
			new_interval1 = interval(cur_interval.a, cur_pos - 1);
			new_interval2 = interval(cur_pos + 1, cur_interval.b);
			
			PQ.push(new_interval1);
			PQ.push(new_interval2);
			
			if(i == (k-1)){
				
				y = max(cur_pos - cur_interval.a, cur_interval.b - cur_pos);
				z = min(cur_pos - cur_interval.a, cur_interval.b - cur_pos);
				
				cout << "Case #"<<test<<": "<<y << " " << z << "\n";
			}
		}
		while(!PQ.empty()){
			PQ.pop();
		}
	}
	cout << endl;
	
	
	return 0;	
}