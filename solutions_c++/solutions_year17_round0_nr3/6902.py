#include<iostream>
#include<math.h>
#include<string>
#include<vector>
using namespace std;
bool sortv(const vector<int>& v1, const vector<int>& v2) { return v1 > v2; }
int main() {
	freopen("i.txt","r",stdin);
	int n, a, b, p, f, x, y;
	vector<int> v;
	cin>>n;
	for(int i=1; i<=n; i++) {
		cin>>a>>b;
		f=a;
		for(int ii=0; ii<b; ii++) {
			if(f == 1) {
				x=0, y=0;
			} else {
				p=ceil(f/2.0);
				x=p-1;
				y=f-p;
				v.push_back(x);
				v.push_back(y);
			}
			sort(v.begin(), v.end());
			f = v[v.size()-1];
			v.pop_back();
		}
		cout<<"Case #"<<i<<": ";
		if(x>y) cout<<x<<" "<<y<<endl;
		else cout<<y<<" "<<x<<endl; 
		v.clear();
	}
	return 0;
}