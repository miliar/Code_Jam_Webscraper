//It's all about what U BELIEVE
#include<iostream>
#include<vector>
#include<algorithm>
#include<bitset>
#include<stdio.h>
#include<map>
#include<stack>
#include<queue>
#include<deque>
#include<cstring>
#include<cmath>
#include<set>
#define endl '\n'
#define fo(s , y , z) for(int y = s ; y < (int)z ; y++)
#define lne if(line)puts("");else line = 1;
#define pb push_back
#define pob pop_back
#define gcu getchar_unlocked
#define modulo 1000000007
#define wtm while(t--)
#define wnm while(n--)
#define lsone(Z) (Z&-Z)
#define readf freopen("/home/ebram96/Desktop/in" , "r" , stdin);
#define writef freopen("/home/ebram96/Desktop/out" , "w" , stdout);
using namespace std;
typedef vector<int> vi;
typedef vector<string> vstr;
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long long ll;
typedef pair<int , int> pairii;
typedef pair<ull , ull> pairull;
typedef set<int> seti;
typedef set<ull> setull;
typedef queue<int> qint;
typedef deque<int> dqint;
//int dx[]={-1,-1,0,1,1, 1, 0,-1};
//int dy[]={ 0, 1,1,1,0,-1,-1,-1};
int main()
{
	//readf
	freopen("/home/ebram96/Desktop/in" , "r" , stdin);
	freopen("/home/ebram96/Desktop/out" , "w" , stdout);
	int t , sz , ind , c = 1;
	string n;
	bool sorted;
	scanf("%d",&t);
	wtm
	{
		cin>>n;
		sz = n.size();
		sorted = 0;
		while(!sorted)
		{
			sorted = 1;
			fo(1,y,sz)if(n[y]<n[y-1])
			{
				sorted = 0;
				ind = y;
				break;
			}
			if(sorted)break;
			fo(ind , y , sz)
				n[y] = '9';
			n[--ind]--;
			while(ind&&n[ind]<'0')
				n[ind--] = '9';
		}
		if(n[0]=='0'&&sz>1)n.erase(0,1);
		printf("Case #%d: %s\n",c++,n.c_str());
	}
}
