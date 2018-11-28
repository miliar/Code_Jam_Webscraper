#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define sqr(a) ((a)*(a))
#define RAND(a,b) ((a)+rand()%((b)-(a)+1))
#define rsz resize
#define forr(i,a,b) for(int i=(a);i<(b);i++)
#define forn(i,n) forr(i,0,n)
#define dforn(i,n) for(int i=n-1;i>=0;i--)
#define forall(it,v) for(auto it=v.begin();it!=v.end();it++)
#define pb push_back
#define mp make_pair
#define lb lower_bound
#define ub upper_bound
#define fst first
#define snd second
using namespace std;
using namespace __gnu_pbds;

typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> ordered_set;
typedef long long ll;
typedef pair<int,int> ii;

int main()
{
	//freopen("input.in","r",stdin);
	//freopen("B-largeOutput.txt","w",stdout);
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	forn(T,t)
	{
		string s;
		cout << "Case #" << T+1 << ": ";
		int pos=0;
		cin >> s;
		while(pos<s.size() && (pos==0 || s[pos-1]<=s[pos])) pos++;
		if(pos==s.size()) cout << s;
		else
		{
			pos--;
			while(pos>0 && s[pos]==s[pos-1]) pos--;
			s[pos]--;
			forn(i,pos) cout << s[i];
			if(pos!=0 || s[pos]!='0') cout << s[pos];
			forr(i,pos+1,s.size()) cout << '9';
		}
		cout << "\n";
	}
	return 0;
}	



