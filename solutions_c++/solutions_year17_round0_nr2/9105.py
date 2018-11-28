#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<utility>
#include<set>
#include<stack>
#include<list>
#include<deque>
#include<bitset>
#include<iomanip>
#include<cstring>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<climits>
#include<cmath>
#include<cctype>
typedef long long int LL;
#define pb push_back
#define mp make_pair


        #define forp(i,a,b) for(LL i = a;i <= b;i++)
        #define forn(i,b,a) for(LL i = b;i >= a;i--)
#define ff first
#define ss second
#define pll pair<long long int,long long int>
#define pii pair<int,int>
#define vll vector<long long int>
#define vii vector<int>
#define gi(n) scanf("%d",&n)
#define gll(n) scanf("%lld",&n)
#define gstr(n) scanf("%s",n)
#define gl(n) cin >> n
#define oi(n) printf("%d",n)
#define oll(n) printf("%lld",n)
#define ostr(n) printf("%s",n)
#define ol(n) cout << n
#define os cout<<" "
#define on cout<<"\n"
#define o2(a,b) cout<<a<<" "<<b
#define all(n) n.begin(),n.end()
#define present(s,x) (s.find(x) != s.end())
#define cpresent(s,x) (find(all(s),x) != s.end())
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
using namespace std;
typedef unsigned long long int ULL;
LL mod = 1000000007;
LL change(LL x)
{
	
	LL a = 9,b = 9,pos = -1,i = 1,y = x;
	while(x > 0)
	{
		a = b;
		b = x%10;
		x /= 10;
		if(b > a)
		{
			pos = i;
		}
		else if(b == a && pos == i-1)
		{
			pos = i;
		}
		i++;
	}
	if(pos == -1)
		return y;
	else
	{
		ULL num = ((int)(y/pow(10,pos-1))-1)*pow(10,pos-1) + pow(10,pos-1);
		num -= 1;
		return num;
	}
}
int main()
{
	freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    ULL t,x,i;	
    cin >> t;
    for(i = 1;i <= t;i++)
    {
		cin >> x;
		x = change(x);
		cout << "Case #"<<i<<": "<< x<< endl;
	}
	return 0;
}
// 1
// 0
// 6
// 0
// 288603514
// 1
