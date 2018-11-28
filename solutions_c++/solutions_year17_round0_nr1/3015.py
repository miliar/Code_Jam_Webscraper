#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define INF 0x3F3F3F3F
#define ii pair<int,int>
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define vii vector<pair<int,int> > 
#define vll vector<long long int>
#define PI acos(-1.0)

int main(){
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	int tc;
	cin >> tc;
	for(int kase=1; kase<=tc; kase++){
		string panc;
		int k;
		cin >> panc >> k;
		
		int resp = 0;
		for(int i=0; panc[i+(k-1)]; i++)
			if(panc[i]=='-'){
				for(int j=i; j<i+k; j++)
					panc[j] = (panc[j]=='-'?'+':'-');
				resp++;
			}
		
		bool noMinus=true;
		for(int i=0; panc[i] && noMinus; i++)
			if(panc[i]=='-')
				noMinus = false;
		
		printf("Case #%d: ", kase);
		if(noMinus)
			printf("%d\n", resp);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
