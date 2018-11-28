/*ckpeteryu Code Jam 2017 Round1A - Problem A */
#include<iostream>
#include<iomanip>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<climits>
#include<cmath>
#include<bitset>
#include<string>
#include<ctime>
#include<typeinfo>
#include<functional>
#include<map>
#include<set>
#include<vector>
#include<stack>
#include<queue>
//#include<regex>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define FOD(i,s,e) for(int i=(s);i>=(int)(e);i--)
#define FORVEC(i,a) for(int i=0;i<(int)((a).size());i++)
#define pb push_back
#define mp make_pair
#define CLR(s,x) memset(s,x,sizeof(s))
#define LL long long unsigned int

int nt,R,C;
char m[26][26];

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);
	//const clock_t begin_time = clock();	
	scanf("%d",&nt);
	FOE(k,1,nt){		
		scanf("%d%d",&R,&C);
		FOR(i,0,R){
			scanf("%s",m[i]);			
		}		
		FOR(i,0,R){			
			FOR(j,0,C){
				if(m[i][j]!='?'){					
					int nc=j;
					nc--;
					while(nc>=0 && m[i][nc]=='?'){
						m[i][nc]=m[i][j];
						nc--;
					}
					nc=j;
					nc++;
					while(nc<C && m[i][nc]=='?'){
						m[i][nc]=m[i][j];
						nc++;
					}
				}
			}			
		}
		FOR(j,0,C){			
			FOR(i,0,R){
				if(m[i][j]!='?'){					
					int nr=i;
					nr--;
					while(nr>=0 && m[nr][j]=='?'){
						m[nr][j]=m[i][j];
						nr--;
					}
					nr=i;
					nr++;
					while(nr<R && m[nr][j]=='?'){
						m[nr][j]=m[i][j];
						nr++;
					}
				}
			}			
		}
		printf("Case #%d:\n",k);
		FOR(i,0,R){
			printf("%s\n",m[i]);
		}		
	}	
	//std::cout <<endl<< float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	return 0;
}