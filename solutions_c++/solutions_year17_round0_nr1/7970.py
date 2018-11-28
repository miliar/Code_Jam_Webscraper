#include <bits/stdc++.h>

#define fst first
#define snd second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main(){

	int t,k;
	cin >> t;
	for(int tc = 0; tc < t; tc++){
		string cad; 
		cin >> cad >> k;
		int flips = 0;
		for(int i = 0; i < cad.size()-k+1; i++){
			if(cad[i] == '-'){
				for(int j = i; j < i+k; j++)
					cad[j] = (cad[j]=='-' ? '+' : '-');
			flips++;
			}
		}
		bool ok = true;
		for(int i = 0; i < cad.size() and ok; i++)
			if(cad[i] != '+') ok = false;
	
		printf("Case #%d: ",tc+1);
		if(ok) printf("%d\n",flips);
		else printf("IMPOSSIBLE\n");
	}

	return 0;
}