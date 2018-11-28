/*ckpeteryu Code Jam 2017 Round1B - Problem A */
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

int nt;

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);
	//const clock_t begin_time = clock();
	scanf("%d",&nt);
	FOE(k,1,nt){
		int D,N;
		scanf("%d%d",&D,&N);
		double mxSpan=0;
		double ret=0;
		FOR(i,0,N){
			int c,m;
			scanf("%d%d",&c,&m);
			double span=1.0*(D-c)/m;
			if(span>mxSpan){
				ret=D/span;
				mxSpan=span;
			}
		}
		printf("Case #%d: %.6f\n",k,ret);
	}	
	//std::cout <<endl<< float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	return 0;
}