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

int main()
{
	freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    LL t,j,ans,flag,i,len,k,K;	
    string s;
    cin >> t;
   
    for(i = 1;i <= t;i++)
    {
        ans = 0;
		flag = 0;
		cin >> s >> K;
		len = s.size();
		for(j = 0;j < len-K+1;j++)
		{
			if(s[j] == '-')
			{
				s[j] = '+';
				for(k = 1;k <= K-1;k++)
				{
					if(s[j+k] == '-')
					s[j+k] = '+';
					else
					s[j+k] = '-';
				}
			 ans++;
			}
		}
		for(j = 0;j < len;j++)
		{
			if(s[j] == '-')
			{
				flag = 1;
				break;
			}
		}
		if(flag)
		cout << "Case #"<<i<<": "<< "IMPOSSIBLE"<< endl;
		else
		cout << "Case #"<<i<<": "<< ans<< endl;

		
	}
	return 0;
}
// 1
// 0
// 6
// 0
// 288603514
// 1
