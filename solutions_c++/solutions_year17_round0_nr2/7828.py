#include<bits/stdc++.h>

#define s(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)

#define MP           make_pair
#define PB           push_back
#define REP(i, n)    for(int i = 0; i < n; i++)
#define INC(i, a, b) for(int i = a; i <= b; i++)
#define DEC(i, a, b) for(int i = a; i >= b; i--)
#define CLEAR(a)     memset(a, 0, sizeof a)

using namespace std;

typedef long long          LL;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int, int>     II;
typedef vector<II>         VII;

LL nextTidy(LL inp){
	VI digits;
	while(inp>0){
		digits.push_back(inp%10);
		inp/=10;
	}
	reverse(digits.begin(), digits.end());
	for(int i=1;i<digits.size();i++)
	if(digits[i]<digits[i-1]){
		for(int j=i;j<digits.size();j++)
			digits[j] = digits[j-1];
		break;
	}
	LL num = 0;
	for(int i=0;i<digits.size();i++)
		num = num*10 + digits[i];
	return num;
}
LL solve(){
	LL inp;
	sl(inp);
	LL f=1,l=inp,m;
	while(f<l){
		m = (f+l+1)/2;
		if(nextTidy(m)<=inp)
			f=nextTidy(m);
		else l=m-1;
	}
	return f;
}
int main()
{
	int t;
	s(t);
	REP(tt,t){
		printf("Case #%d: ",tt+1);
		printf("%lld\n",solve());
	}
    return 0;
}
