#include <bits/stdc++.h>
 
#define fst first
#define snd second
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define clr(a, v) memset( a , v , sizeof(a) )
#define pb push_back
#define mp make_pair
#define sz size()
#define FORN( i , s , n ) for( int i = (s) ; i < (n) ; i++ )
#define FOR( i , n ) FORN( i , 0 , n )
#define FORIT( i , x ) for( typeof x.begin() i = x.begin() ; i != x.end() ; i++ )
#define trace(x)    cout << #x << ": " << x << endl;
#define trace2(x, y) cout << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z) cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define read ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
 
using namespace std;
 
typedef long long int64;
typedef vector <int> vi;
typedef pair <int64,int64> ii;
typedef vector <string> vs;
typedef vector <ii> vii;


int main(){
	int numT;
	string s;
	cin>>numT;
	FORN(caso,1,numT+1){
		cout<<"Case #"<<caso<<": ";
		cin>>s;
		int pos=-1;
		FORN(i,1,s.sz){
			if(s[i]<s[i-1]){
				pos = i-1;
				break;
			}
		}

		if(pos==-1){
			cout<<s<<endl;
			continue;
		}

		for(; pos>0; pos--){
			if( s[pos] > s[pos-1] ) break;
		}

		s[pos]--;
		FORN(i,pos+1,s.sz) s[i]='9';


		if(s[0]=='0'){
			s.erase(0,1);
			cout<<s<<endl;
		}
		else cout<<s<<endl;
		
	}

	return 0;
}



