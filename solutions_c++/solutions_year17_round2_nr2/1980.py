#include <bits/stdc++.h>

using namespace std;
#define ll long long
template<class T> void p(vector<T>& a){ for(int i = 0;i < a.size();i++) cout << a[i] << " "; cout << endl; }
#define vi vector<int>
#define vl vector<ll>
#define vb vector<bool>
#define f(i,a,b) for(i = a;i < b;i++)
#define rf(i,a,b) for(i = a;i >= b;i--)

//comparator function for priority queue
class comp{
public:
  bool operator()(pair<int,int> a, pair<int,int> b){  //overloading "()" operator 
    if(a.first < b.first) return true;
    else return false;
  }
};

int main(){
	int t_,t;
	cin >> t;
	f(t_,0,t){
		cout << "Case #" << t_ + 1 << ": ";
		int n,r,o,y,g,v,b,i,j = 0;
		cin >> n >> r >> o >> y >> g >> b >> v;
	    priority_queue<pair<int,char> ,vector<pair<int,char> >,comp > pq;
		pq.push(make_pair(r,'R'));
		pq.push(make_pair(o,'O'));
		pq.push(make_pair(y,'Y'));
		pq.push(make_pair(g,'G'));
		pq.push(make_pair(b,'B'));
		pq.push(make_pair(v,'V'));
		pair<int,char> x = pq.top();
		//cout << x.first << endl;
		if(x.first > (n/2)){
			cout << "IMPOSSIBLE\n";
			continue;
		}
		string s(n,'#');
		f(i,0,6){
			x = pq.top();
			pq.pop();
			while(x.first != 0){
				x.first--;
				s[j] = x.second;
				j += 2;
				j %= n;
				if(j == 0) j++;
			}
		}
		cout << s << endl;
	}
	return 0;
}
