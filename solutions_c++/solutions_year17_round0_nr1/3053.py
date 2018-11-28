#include <bits/stdc++.h>

//LIFE IS NOT A PROBLEM TO BE SOLVED

using namespace std;

#define rep(i,a,b) for(int i = int(a); i < int(b) ; i++)
#define pb push_back
#define mp make_pair
#define F first
#define S second

typedef long long int ll;
typedef unsigned long long int ull;
typedef pair < int, int > ii;
typedef pair < int, ii > iii;

const int INF = 0x3f3f3f3f;
const ll LINF = 1LL<<58;

int main()
{
	
	freopen("A.in", "r", stdin);
	freopen("A.sol", "w", stdout);
	
	int T, z=1; cin >> T;
	
	while(T--){
		
		string s, aux; int k, ans, cnt;
		cin >> s >> k;
		
		ans=cnt; cnt=0; aux=s;
		
		//be +
		rep(i, 0, aux.size()-k+1){
			if(aux[i]=='-'){
				cnt++;
				rep(j, i, i+k){
					if(aux[j]=='-') aux[j]='+';
					else if(aux[j]=='+') aux[j]='-';
				}
			}
		}	
		rep(i, 0, aux.size()){
			if(aux[i]=='-'){
				cnt=INF;
				break;
			}
		}
		
		ans=cnt;
				
		printf("Case #%d: ", z++);
		if(ans==INF) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
		
	}
	
	return 0;
	
}
