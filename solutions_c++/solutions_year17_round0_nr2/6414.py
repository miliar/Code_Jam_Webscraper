#include <bits/stdc++.h>
#define FIO ios_base::sync_with_stdio(0)
#define all(X) X.begin(),X.end()
#define rall(X) X.rbegin(),X.rend()
#define FOR(a,n) for(long long int  a=0;a<n;a++)
#define FORI(a,b,c) for(long long int a=b;a<=c;a++)
#define FORD(a,b,c) for(long long int a=b;a>=c;a--)
#define ITER(a,b) for(auto &a : b)
#define INC(a,b,c,d) for(long long int a=b;a<=c;a+=d)
#define DEC(a,b,c,d) for(long long int a=b;a>=c;a-=d)

#define SORT(a) sort(all(a))
#define RSORT(a) sort(rall(a))
#define MP make_pair
#define PB push_back
#define PF push_front
#define DB pop_back
#define DF pop_front
#define cx first
#define cy second
#define MOD 10
#define MADD(a,b) (a+b>=M):a+b-MOD?a+b
#define MDEC(a,b)  MADD(a-b,MOD)


using namespace std;
typedef long long int ll;
typedef long double ld;
typedef pair<ld,ld> point;
typedef pair<point,point> line;

/****** Geometry*****/

pair<bool,point> intersection(line a,line b){
	ld A1 = a.cy.cy - a.cx.cy;
	ld B1 = a.cx.cx - a.cy.cx;
	ld A2 = b.cy.cy - b.cx.cy;
	ld B2 = b.cx.cx - b.cy.cx;
	ld C1 = A1*a.cx.cx + B1*a.cx.cy;
	ld C2 = A2*b.cx.cx + B2*b.cx.cy;
	ld det = A1*B2 - B1*A2;
	if(det==0.0)
		return {false,{{0.0},{0.0}}};
	else return {true,{(B2*C1-B1*C2)/det,(A1*C2-C1*A2)/det}};


}

/****** Geo-End *****/

/******** Math based Functions ******/
ll binpow(ll a, ll b, ll c)
{
    ll r =1 ;
    while (b)
    {
        if (b&1) r*=a;
        a*=a;
        r%=c;
        a%=c;
        b>>=1;
    }
    return r%c;
}

ll inverse(ll a, ll m)
{
    return binpow(a, m-2, m);
}
/*** Math Section Ends***/

string s;

int main()
{
     #ifndef ONLINE_JUDGE
          freopen("in.txt","r",stdin);
          freopen("out.txt","w",stdout);
     #endif
	ll n;
	cin>>n;
	getchar();
	FOR(z,n){
		cin>>s;
		//s = '0'+s;
		//cout<<s<<" ";
		ll flag=0;
		for(ll i= s.size()-1;i>=0;i--){
		if(flag)	{
			s[i] = '9';
			flag= 0;

			if(s[i-1]!='0')s[i-1] = s[i-1] - 1;
			else flag = 1;
			continue;
		}

		if(i>0){
			if(s[i]<s[i-1]||(s[i]==s[i-1]&&s[i]=='0')){
				FORI(z,i,s.size()-1)	s[z] = '9';

							if(s[i-1]!='0')s[i-1] = s[i-1] - 1;
							else flag = 1;
			}

		}

	}
		cout<<"Case #"<<z+1<<": ";
		ll u=0;
		while(s[u]=='0')u++;
		for(;u<s.size();u++)
			putchar(s[u]);
		putchar('\n');
	//	system("pause");
	}


    return 0;
}
