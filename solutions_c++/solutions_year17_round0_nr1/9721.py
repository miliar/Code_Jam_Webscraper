//Template

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <deque>
#include <string>
#include <string.h>
#include <vector>
#include <stack>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <time.h>
#include <bitset>
#include <list>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;
typedef pair<pii,pii> ppi;
typedef pair<LL,LL> pll;
typedef pair<string,string> pss;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vii;
typedef vector<LL> vl;
typedef vector<vl> vvl;
typedef vector<string> vstr;
typedef vector<char> vc;

double EPS = 1e-9;
int INF = 2000000000;
long long INFF = 8000000000000000000LL;
double PI = acos(-1);
int dirx[8] = {-1,0,0,1,-1,-1,1,1};
int diry[8] = {0,1,-1,0,-1,1,-1,1};

#ifdef TESTING
	#define DEBUG fprintf(stderr,"====TESTING====\n")
	#define VALUE(x) cerr << "The value of " << #x << " is " << x << endl
	#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
	#define DEBUG 
	#define VALUE(x)
	#define debug(...)
#endif

#define FOR(a,b,c) for (int (a)=(b);(a)<(c);++(a))
#define FORN(a,b,c) for (int (a)=(b);(a)<=(c);++(a))
#define FORD(a,b,c) for (int (a)=(b);(a)>=(c);--(a))
#define FORSQ(a,b,c) for (int (a)=(b);(a)*(a)<=(c);++(a))
#define FORL(a,b,c) for (LL (a)=(b);(a)<=(c);++(a))
#define FORLSQ(a,b,c) for (int (a)=(b);(LL)(a)*(LL)(a)<=(c);++(a))
#define FORC(a,b,c) for (char (a)=(b);(a)<=(c);++(a))
#define REP(i,n) FOR(i,0,n)
#define REPN(i,n) FORN(i,1,n)
#define REPD(i,n) FORD(i,n,1)
#define MAX(a,b) a = max(a,b)
#define MIN(a,b) a = min(a,b)
#define SQR(x) ((x) * (x))
#define RESET(a,b) memset(a,b,sizeof(a))
#define fi first
#define se second
#define mp make_pai
#define pb push_back
#define ALL(v) v.begin(),v.end()
#define ALLA(arr,sz) arr,arr+sz
#define SIZE(v) (int)v.size()
#define SORT(v) sort(ALL(v))
#define REVERSE(v) reverse(ALL(v))
#define SORTA(arr,sz) sort(ALLA(arr,sz))
#define REVERSEA(arr,sz) reverse(ALLA(arr,sz))
#define PERMUTE next_permutation
#define TC(t) while(t--)
#define READ(n,data) {scanf("%d",&n); REPN(i,n) scanf("%d",&data[i]);}


inline string IntToString(int a){
    char x[100];
    sprintf(x,"%d",a); string s = x;
    return s;
}

inline int StringToInt(string a){
    char x[100]; int res;
    strcpy(x,a.c_str()); sscanf(x,"%d",&res);
    return res;
}

inline string GetString(void){
	char x[1000005];
	scanf("%s",x); string s = x;
	return s;
}

inline string uppercase(string s){
	int n = SIZE(s); 
	REP(i,n) if (s[i] >= 'a' && s[i] <= 'z') s[i] = s[i] - 'a' + 'A';
	return s;
}

inline string lowercase(string s){
	int n = SIZE(s); 
	REP(i,n) if (s[i] >= 'A' && s[i] <= 'Z') s[i] = s[i] - 'A' + 'a';
	return s;
}

inline void OPEN (string s) {
    freopen ((s + ".in").c_str (), "r", stdin);
    freopen ((s + ".out").c_str (), "w", stdout);
}


typedef struct IdxInt {
  int value;
  int index;
}IdxInt;

string s;
int a, b, c, d;
IdxInt senators[26];
int match;
int NCases;
string ALPH[26]={"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
                 "Q","R","S","T","U","V","W","X","Y","Z"};

/*For split string
char delim[]="/,();:\n";
char *token;
token=strtok(line, delim);
int i;
while((token=strtok(NULL, delim))!=NULL)
{ 
 token;                          
}
or if it is a fixed length just:
        scanf("%s delim %s",&s1, &s2);
*/

void splitString(char* line, char* delim, string **tokenout)
{
   char *token;
   token=strtok(line, delim);
   int i;
   while((token=strtok(NULL, delim))!=NULL)
   { 
     *tokenout[i]=(string)token;                          
   }
}
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int compareIndexed(const void * elem1, const void * elem2) {
  IdxInt * i1, *i2;
  i1 = (IdxInt*)elem1;
  i2 = (IdxInt*)elem2;
  return i2->value - i1->value;
}

void sortArray(IdxInt * array, size_t num) {
  qsort(array, num, sizeof(IdxInt), compareIndexed);
}

int sumDigit(IdxInt *digits)
{
    int sum=0;
    for (int i = 0; i < 26; ++i)
      sum+=digits[i].value;
    
    return sum;
}

void readsolve()
{

    int ans, k, sum=0;
    int p[1000];
    char N[100];
    scanf("%s %d",&N, &k);
    
    int length=strlen(N);
   
    for (int i = 0; i < length; ++i) 
    {
        if (N[i]=='-')p[i]=-1; 
        if (N[i]=='+')p[i]=1;
        //printf("%d",p[i]);
        sum+=p[i];
  
    }
    
	if (sum == length)
    { 
       printf("%d", 0);
       goto MARK;
    }
                 
        
    ans=0;
    for (int i = 0; i < length-k+1; i++)
    {
        if (p[i]==-1)
        {
          for (int j = i; j < i+k; j++)  p[j]=-1*p[j];
             
          ans++;

        }
       
    }
    
	sum = 0;
    for (int i = 0; i < length; ++i) 
    {
       	sum+=p[i];
       	//printf("%d",p[i]);
    }
    
	if (sum == length)
    {            
        printf("%d", ans);
    }
    else
	{
	  
      printf("IMPOSSIBLE");
    }
    MARK:printf("");
	
              
}


int main()
{
  freopen("A-small-attempt0.in","rt",stdin);
  freopen("A-small-attempt0.out","wt",stdout);
  scanf("%d", &NCases);

  REPN(cases,NCases)
  {
    printf("Case #%d: ", cases);
    readsolve();
    printf("\n");
    
  }
  return 0;
}
















