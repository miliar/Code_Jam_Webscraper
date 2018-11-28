#include<bits/stdc++.h>

using namespace std;

// Shortcuts for "common" data types in contests
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
// To simplify repetitions/loops, Note: define your loop style and stick with it!
#define s(i) scanf("%d",&i)
#define sl(i) scanf("%ld",&i)
#define sll(i) scanf("%lld",&i)
#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define NREP(i,a,b) \
for (int i = int(a); i >= int(b); i--)
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000 // 2 billion

// VIOLET AND YELLOW , RED AND GREEN , ORANGE AND BLUE

string calculate(int x , int y , int z,bool *ch){
	//printf("%d %d %d\n",x,y,z);
	if( x + y < z )
	{
		//printf("ENDING HERE");
		*ch = false;
		return "";
	}
	string ans = "";
	while( z > 0 ){
		ans += "3";
		if( x + y > z ){
			ans += "21";
			x--;
			y--;
		}
		else if( x > 0  ){
			ans += "1";
			x--;
		}
		else if( y > 0 ){
			ans += "2";
			y--;
		}
		z--;
	}
	return ans;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T ; 
    s(T) ; 
    REP( t ,  1 , T  ){
    	bool ch = true;
    	//cout << ch << endl;
    	int N ; 
    	s(N) ; 
    	int R , O , Y , G , B , V ;
    	s(R) ; s(O) ; s(Y) ; s(G) ; s(B) ; s(V) ; 
    	if( V > Y - 1 && V > 0 ){
    		if( V == Y && O == 0 && G == 0 && B == 0 && R == 0 ){
    			string ans = "";
    			REP( i , 0 , V - 1) {
    				ans += "VY";
    			}
    			printf("Case #%d: ",t);
    			cout << ans << endl;
    			continue;
    		}
    		ch = false;
    	}
    	if( G > R - 1 && G > 0 ){
    		if( G == R && O == 0 && V == 0 && B == 0 && Y == 0 ){
    			string ans = "";
    			REP( i , 0 , G - 1 ) {
    				ans += "GR";
    			}
    			printf("Case #%d: ",t);
    			cout << ans << endl;
    			continue;
    		}
    		ch = false;
    	}
    	if( O > B - 1 && O > 0){
    		if( O == B && G == 0 && V == 0 && R == 0 && Y == 0 ){
    			string ans = "";
    			REP( i , 0 , O - 1) {
    				ans += "OB";
    			}
    			printf("Case #%d: ",t);
    			cout << ans << endl;
    			continue;
    		}
    		ch = false;
    	}
    	//cout << ch << endl;
    	bool Yellow = false , Red = false , Blue = false ; 
    	if( V > 0 ){
    		Yellow = true;
    		Y -= V;
    	}
    	if( G > 0 ){
    		Red = true;
    		R -= G;
    	}
    	if( O > 0 ){
    		Blue = true;
    		B -= O;
    	}
    	pair < int , char > a[5];
    	a[0] = pair<int,char>(Y,'Y');
    	a[1] = pair<int,char>(R,'R');
    	a[2] = pair<int,char>(B,'B');
    	sort( a , a + 3 ) ;
    	string res = "";
    	string ans = calculate(a[0].first , a[1].first , a[2].first ,&ch ) ; 
    	//cout << ans << endl;
    	//cout << ch << endl;
    	REP( i , 0 , ans.size() - 1 ){
    		char val; 
    		if( ans[i] == '3' ) {
    			val = a[2].second;
    		}
    		if( ans[i] == '2' ){
    			val = a[1].second;
    		}
    		if( ans[i] == '1' ) {
    			val = a[0].second;
    		}
    		if( val == 'B' ) {
    			if( Blue == true ){
    				REP( i , 0 , O - 1 ){
    					res += "BO";
    				}
    				Blue = false;
    			}
    			res += "B";
    		}
    		else if( val == 'Y' ) {
    			if( Yellow == true ){
    				REP( i , 0 , V - 1 ){
    					res += "YV";
    				}
    				Yellow = false;
    			}
    			res += "Y";
    		}
    		else if( val == 'R' ){
    			if( Red == true ){
    				REP( i , 0 , G - 1 ){
    					res += "RG";
    				}
    				Red = false;
    			}
    			res += "R";
    		}
    	}
    	printf("Case #%d: ",t);
    	if( ch == true ){
    		cout << res << endl;
    	}
    	else {
    		cout << "IMPOSSIBLE" << endl;
    	}
    }
    return 0;
}
