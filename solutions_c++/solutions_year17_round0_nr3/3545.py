#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<bitset>
#include<ext/pb_ds/priority_queue.hpp>
using namespace std;

typedef unsigned long long LL;

struct data{
	LL siz,cnt; data(){}
	data(LL siz,LL cnt): siz(siz),cnt(cnt){}
	bool operator < (const data &B) const {return siz < B.siz;}
}D[4];

int T;

void Count(LL n,LL &l,LL &r)
{
	n -= 1LL;
	if (n & 1LL)
	{
		l = (n >> 1LL);
		r = (n + 1LL >> 1LL);
	}
	else l = r = (n >> 1LL);
}

void Print(int I,LL n)
{
	LL l,r; Count(n,l,r);
	printf("Case #%d: ",I);
	cout << max(l,r) << ' ' << min(l,r) << endl;
}

void Break(data x,data &y,data &z)
{
	if (!x.siz) {y = z = data(0,0); return;}
	LL now = x.siz - 1LL;
	if (!now) {y = z = data(0,0); return;}
	if (now & 1LL)
	{
		y = data(now >> 1LL,x.cnt);
		z = data(1LL + now >> 1LL,x.cnt);
	}
	else y = z = data(now >> 1LL,x.cnt);
	if (!y.siz) y.cnt = 0;
	if (!z.siz) z.cnt = 0;
}

void Solve(int I)
{
	LL n,k; cin >> n >> k;
	if (k == 1) {Print(I,n); return;}
	data A,B; Break(data(n,1),A,B); k -= 1LL;
	if (B < A) swap(A,B);
	for (;;)
	{
		if (A.cnt + B.cnt < k)
		{
			k -= (A.cnt + B.cnt);
			Break(A,D[0],D[1]);
			Break(B,D[2],D[3]);
			sort(D,D + 4); int cur = 0;
			for (int i = 1; i < 4; i++)
				if (D[i].siz == D[cur].siz) D[cur].cnt += D[i].cnt;
				else D[++cur] = D[i];
			if (cur == 1) A = D[0],B = D[1];
			else if (cur == 0) A = data(0,0),B = D[0];
			else if (cur == 2) A = D[1],B = D[2];
			continue;
		}
		if (!A.siz) Print(I,B.siz);
		else
		{
			bool flag; LL la,ra,lb,rb;
			Count(A.siz,la,ra); Count(B.siz,lb,rb);
			if (min(la,ra) < min(lb,rb)) flag = 1;
			else if (min(la,ra) > min(lb,rb)) flag = 0;
			else if (max(la,ra) < max(lb,rb)) flag = 1;
			else flag = 0; if (flag) swap(A,B);
			Print(I,A.cnt >= k ? A.siz : B.siz);
		}
		break;
	}
}

int main()
{
	#ifdef DMC
		freopen("DMC.txt","r",stdin);
		freopen("test.txt","w",stdout);
	#endif
	
	cin >> T; for (int i = 1; i <= T; i++) Solve(i);
	return 0;
}
