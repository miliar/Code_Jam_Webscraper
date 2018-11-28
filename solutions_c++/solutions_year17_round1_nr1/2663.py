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

int n , m  ;

set <char> possibleInitials;
char a[50][50];
int dp[50][50] , numOfChars;

void preprocess(){
	REP( i , 0 , n - 1 ){
		REP( j , 0 , m - 1 ){
			if( i - 1 >= 0 )
				dp[i][j] += dp[i - 1][j];
			if( j - 1 >= 0 )
				dp[i][j] += dp[i][j - 1];
			if( i - 1 >= 0 && j - 1 >= 0 )
				dp[i][j] -= dp[i - 1][j - 1]; 
		}
	}
}

int calculateSum(int i,int j,int k,int l){
	int ans = dp[k][l];
	if( j - 1 >= 0 )
		ans -= dp[k][j - 1];
	if( i - 1 >= 0 )
		ans -= dp[i - 1][l];
	if( i - 1 >= 0 && j - 1 >= 0 )
		ans += dp[i - 1][j - 1];
	return ans;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t ; 
    s(t);
    REP( T , 1 , t ){
    	possibleInitials.clear();
    	s(n);s(m); 
    	REP( i , 0 , n - 1 ){
    		scanf("%s",a[i]);
    	}
    	REP( i , 0 , n - 1 ){
    		REP( j , 0 , m - 1 ){
    			possibleInitials.insert(a[i][j]);
    		}
    	}
    	set<char>::iterator it = possibleInitials.begin();
    	while( it != possibleInitials.end() ) {
    		numOfChars = 0 ;
    		REP( i , 0 , n - 1 ){
    			REP( j , 0 , m - 1 ){
    				if( a[i][j] == '?' ){
    					dp[i][j] = 0 ;
    				}
    				else if( a[i][j] == *it ){
    					dp[i][j] = 1;
    					numOfChars++;
    				}
    				else 
    					dp[i][j] = -1;
    			}
    		}
    		preprocess();
    		int mini = INF , sx = -1 , sy = -1 , ex = -1 , ey = -1;
    		REP( i , 0 , n - 1 ){
    			REP( j , 0 , m - 1 ){
    				REP( k , i , n - 1 ){
    					REP( l , j , m - 1 ){
    						if(calculateSum(i , j , k , l) == numOfChars){
    							if( ( k - i + 1 ) * ( l - j + 1 ) < mini ){
    								mini = (k - i + 1) * (l - j + 1);
    								sx = i , sy = j , ex = k , ey = l ; 
    							}
    						}
    					}
    				}
    			}
    		}
    		REP( i , sx , ex ){
    			REP( j , sy , ey ){
    				a[i][j] = *it;
    			}
    		}
    		it++;
    	}
    	it = possibleInitials.begin();
    	while( it != possibleInitials.end() ) {
    		numOfChars = 0 ;
    		REP( i , 0 , n - 1 ){
    			REP( j , 0 , m - 1 ){
    				if( a[i][j] == '?' ){
    					dp[i][j] = 0 ;
    				}
    				else if( a[i][j] == *it ){
    					dp[i][j] = 1;
    					numOfChars++;
    				}
    				else 
    					dp[i][j] = -1;
    			}
    		}
    		preprocess();
    		int mini = -1 * INF , sx = -1 , sy = -1 , ex = -1 , ey = -1;
    		REP( i , 0 , n - 1 ){
    			REP( j , 0 , m - 1 ){
    				REP( k , i , n - 1 ){
    					REP( l , j , m - 1 ){
    						if(calculateSum(i , j , k , l) == numOfChars){
    							if( ( k - i + 1 ) * ( l - j + 1 ) > mini ){
    								mini = (k - i + 1) * (l - j + 1);
    								sx = i , sy = j , ex = k , ey = l ; 
    							}
    						}
    					}
    				}
    			}
    		}
    		REP( i , sx , ex ){
    			REP( j , sy , ey ){
    				a[i][j] = *it;
    			}
    		}
    		it++;
    	}
    	printf("Case #%d:\n",T);
    	REP(i , 0 ,n - 1){
    		REP( j , 0, m - 1 ){
    			printf("%c",a[i][j]);
    		}
    		printf("\n");
    	}

    }
    return 0;
}
