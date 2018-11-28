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
string func(string s,int i,int len){
	for(int i=0; i<len ;i++){
		s[i]='9';
	}
	s[len-1]='\0';
	return s;
}
int main()
{
	//readf; reaaaaaaaaaadf=1;
	//------------------------------------------------------------------------
	int n,test=1,f;
	string s;
	scanf("%d",&n);
	while(test<=n){
		cin>>s;
		int len=s.size();
		f=len-1;
		if(s[0]=='1' && s[1] < '1' && len > 1){
			s=func(s,0,len);
		}else {
			for(int i=1 ; i < len ;i++){
				if(s[i]<s[i-1]){
					if(i==len-1 && s[i]<s[i-1] && s[i-1]=='0'){
						s=func(s,0,len);
						break;
					}
					s[i]='9';
					if(f>i-1)s[i-1]--,f=i-1;
					for(int j=i-1 ; j>0 ; j--){
						if(s[j]<s[j-1]){
							s[j]='9';
							if(f>j-1)s[j-1]--,f=j-1;
						}
					}
				}
			}
		}
		printf("Case #%d: %s\n",test++,s.c_str());
	}
	//------------------------------------------------------------------------
	if(reaaaaaaaaaadf)puts("REEEEAAAAAAAAAADF IS ONNNNNNNNNN");
	return 0;
}
