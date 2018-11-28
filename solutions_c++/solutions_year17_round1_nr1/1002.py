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
int L[30],R[30],U[30],D[30],n,m;
char ch[30][30],ans[30][30];

bool extend(int tmp , int d){
	if(d==0){
		if(U[tmp]==0)
			return false;
		for(int i=L[tmp] ; i<=R[tmp] ; i++)
			if(ans[U[tmp]-1][i] != '?')
				return false;
		U[tmp]--;
		for(int i=L[tmp] ; i<=R[tmp] ; i++)
			ans[U[tmp]][i] = char('A'+tmp);
		return true;
	}

	if(d==1){
		if(R[tmp]==m)
			return false;
		for(int i=U[tmp] ; i<=D[tmp] ; i++)
			if(ans[i][R[tmp]+1] != '?')
				return false;
		R[tmp]++;
		for(int i=U[tmp] ; i<=D[tmp] ; i++)
			ans[i][R[tmp]] = char('A'+tmp);
		return true;
	}

	if(d==2){
		if(D[tmp]==n)
			return false;
		for(int i=L[tmp] ; i<=R[tmp] ; i++)
			if(ans[D[tmp]+1][i] != '?')
				return false;
		D[tmp]++;
		for(int i=L[tmp] ; i<=R[tmp] ; i++)
			ans[D[tmp]][i] = char('A'+tmp);
		return true;
	}
	if(d==3){
		if(L[tmp]==0)
			return false;
		for(int i=U[tmp] ; i<=D[tmp] ; i++)
			if(ans[i][L[tmp]-1] != '?')
				return false;
		L[tmp]--;
		for(int i=U[tmp] ; i<=D[tmp] ; i++)
			ans[i][L[tmp]] = char('A'+tmp);
		return true;
	}
	return false;
}
int main(){
	ios_base::sync_with_stdio (0);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;cin>>T;
	for(int Case=1 ; Case<=T; Case++){
		memset(ans,'?',sizeof ans);
		cout<<"Case #"<<Case<<": "<<endl;
		for(int i=0 ; i<30 ; i++){
			D[i]=R[i]=-1;
			L[i]=U[i]=100;
		}
		cin>>n>>m;
		for(int i=0 ; i<n ; i++)
			for(int j=0 ; j<m ; j++){
				cin>>ch[i][j];
				if(ch[i][j]!='?'){
					int tmp = ch[i][j]-'A';
					L[tmp] = min(L[tmp],j);
					U[tmp] = min(U[tmp],i);
					R[tmp] = max(R[tmp],j);
					D[tmp] = max(D[tmp],i);
				}
			}
		for(int tmp=0 ; tmp<26 ; tmp++)if(R[tmp]!=-1){
			for(int i=U[tmp] ; i<=D[tmp] ; i++)
				for(int j=L[tmp] ; j<=R[tmp] ; j++)
					ans[i][j] = char('A' + tmp);
		}
		while(true){
			bool test = false;
			for(int tmp=0 ; tmp<26 ; tmp++)
				for(int i=0 ; i<4 ; i++)
					test |= extend(tmp,i);
			if(!test)
				break;
		}
		for(int i=0 ; i<n ; i++,cout<<endl)
			for(int j=0 ; j<m ; j++)
				cout<<ans[i][j];
	}
	return 0;
}

