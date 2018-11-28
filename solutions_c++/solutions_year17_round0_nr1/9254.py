// UVa 10928.cpp
/*
ID:ahmeds1
PROG:milk3
LANG:C++
*/
//It's all about what U BELIEVE
#include<bits/stdc++.h>
#define endl '\n'
#define fo(s , y , z) for(int y = s ; y < z ; y++)
#define lne if(liAne)puts("");else line = 1;
#define pb push_back
#define gcu getchar_unlocked
#define modulo 1000000007
#define wtm while(t--)
#define wnm while(n--)
#define non if(!n)break;
#define lsone(Z) (Z&-Z)
#define clr(arr,val) memset(arr,val,sizeof arr)
#define readf freopen("in" , "r" , stdin);
#define writef freopen("/media/aahmedsamy/AhmedSamy/Programming/Codes/AC/out" , "w" , stdout);
using namespace std;
typedef vector<int> vi;
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long long ll;
typedef pair<int , int> pairii;
typedef pair<ull , ull> pairull;
typedef set<int> seti;
typedef set<ull> setull;
typedef queue<int> qint;
typedef deque<int> dqint;
typedef unsigned long long ull;
typedef long long ll;
typedef pair<int , int> pairii;
typedef pair<ull , ull> pairull;
typedef set<int> seti;
typedef set<ull> setull;
typedef queue<int> qint;
typedef deque<int> dqint;
//FILE *fin, *fout;
using namespace std;
bool reaaaaaaaaaadf=0;
//////////////////////////////////////////////////
bool func(char *str,int i,int len,int &p,int &m,int &ans){
	if(i+len>strlen(str))return 0;
	int end=i+len;
	for(; i<end ;i++){
		if(str[i]=='-'){
			str[i]='+';
			p++;
			m--;
		}else{
			str[i]='-';
			m++;
			p--;
		}
	}
	ans++;
	return 1;
}
int main()
{
	//readf; reaaaaaaaaaadf=1;
	//------------------------------------------------------------------------
	int n,test=1,p=0,m=0,len,ans=0;
	char str[1001];
	scanf("%d",&n);
	while(n--){
		m=0,p=0;
		printf("Case #%d: ",test++);
		scanf("\n");
		ans=0;
		for(int i=0 ; ;i++ ){
			scanf("%c",&str[i]);
			if(str[i]==' '){
				str[i]='\0';
				break;
			}
			if(str[i]=='+')p++;
			else m++;
		}
		scanf("%d",&len);
		int sz=strlen(str);
		for(int i=0 ; i < sz && m ; i++){
			if(m+p<len)break;
			if(str[i]=='-'){
				if(!func(str,i,len,p,m,ans))break;
			}
		}
		if(!m)printf("%d\n",ans);
		else puts("IMPOSSIBLE");
	}
	//------------------------------------------------------------------------
	if(reaaaaaaaaaadf)puts("REEEEAAAAAAAAAADF IS ONNNNNNNNNN");
	return 0;
}
