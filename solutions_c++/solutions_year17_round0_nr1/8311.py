//arpit717
#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	ll;
typedef unsigned long long int ULL;

#define loop(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
//Works for forward as well as backward iteration

FILE *fin = freopen("A-large.in","r",stdin);
FILE *fout = freopen("A-large-out.txt","w",stdout);
//const int N = int(1e5)+10;
const int LOGN = 20;
const int INF = int(1e9);

void solve(){

	string s;
	int k,cnt=0;
	cin>>s>>k;
	loop(i,0,s.size()-k+1){
		if(s[i]=='-'){
			cnt++;
			loop(j,0,k)s[i+j]=(s[i+j]=='-'?'+':'-');
		}
	}
	loop(i,s.size()-k+1,s.size()){
		if(s[i]=='-'){
			cnt=-1;break;
		}
	}
	if(cnt==-1)cout<<"IMPOSSIBLE\n";
	else cout<<cnt<<endl;
}

int main()
{
	int t;
	cin>>t;
	loop(i,1,t+1){
		cout<<"Case #"<<i<<": ";
		solve();
	}

    return 0;
}
