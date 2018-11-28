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

void increment(string &str, int a){
	for(int i=a; str[i]; i++)
		str[i]++;
}
void decrement(string &str, int a){
	for(int i=a; str[i]; i++)
		str[i]--;
}

int main(){
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	int tc;
	cin >> tc;
	for(int kase=1; kase<=tc; kase++){
		string n, trie;
		cin >> n;
		for(int i=0; i<n.size(); i++)
			trie.pb('1');
		if(trie > n){
			trie.pop_back();
			for(int i=0; trie[i]; i++)
				trie[i] = '9';
		}
		else{
			for(int i=0; trie[i]; i++){
				while(trie[i]<='8' && trie<=n)
					increment(trie,i);
					
				if(trie>n)
					decrement(trie,i);
			}
			
		}
		
		printf("Case #%d: ", kase);
		cout << trie << endl;
	}
	return 0;
}
