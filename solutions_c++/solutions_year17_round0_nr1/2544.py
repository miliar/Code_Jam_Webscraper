/* In The Name Of God */
#include <bits/stdc++.h>

# define xx first
# define yy second
# define pb push_back
# define pp pop_back
# define eps 1e-9

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vint;

int main(){
	ios_base::sync_with_stdio (0);
	freopen("inp.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;cin>>T;
	for(int Case = 1 ; Case <= T ; Case++){
		int k,ans = 0;
		string s;cin>>s>>k;
		while(true){
			int pos;
			for(pos=0 ; pos<(int)s.size() ; pos++)if(s[pos]=='-')
				break;
			if(s[pos]!='-')
				break;
			if( (int)s.size() - pos < k){
				ans = -1;
				break;
			}
			for(int i=0 ; i<k ; i++)
				if(s[pos+i]=='-')
					s[pos+i]='+';
				else
					s[pos+i]='-';
			ans++;
		}
		cout<<"Case #"<<Case<<": ";
		if(ans!=-1)
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}	
	return 0;
}

