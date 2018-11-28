#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
const int N = 105;
int t,k,n,res;
string s;
bool check(vector<char> v){
	bool f = 1;
	rep(i,0,n-1) f &= (v[i]=='+');
	return f;
}
char get(char ch){
	return (ch == '-' ? '+' : '-');
}
void go(vector<char> &v,int p){
	rep(i,p,p+k-1){
		v[i]=get(v[i]);
	}
}
int main(){
	#ifdef srinu73
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	#endif // srinu73
	ios_base::sync_with_stdio(0);cin.tie(0);
	cin >> t;
	rep(nt,1,t){
		cout << "Case #" << nt << ": ";
		res = -1;
		cin >> s >> k;
		n = s.length();
		map< vector <char> , int> d;
        queue <vector <char> > q;
        vector <char> v;
        rep(i,0,n-1) v.push_back(s[i]);
        q.push(v);
    	d[v]=0;
        while(!q.empty()){
			vector<char> cur=q.front();q.pop();
			int d_cur = d[cur];
			if(check(cur)){
				res = d[cur];
				break;
			}
			rep(i,0,n-k){
				go(cur,i);
				if(!d.count(cur)){
					d[cur] = d_cur + 1;
					q.push(cur);
				}
				go(cur,i);
			}
        }
        if(~res) cout << res << "\n";
        else cout << "IMPOSSIBLE\n" ;
	}
}
