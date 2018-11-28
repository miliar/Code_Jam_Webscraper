/**************************************************************************************************************
   *  Md. Abdulla Al Mamun (Nayon)
   *  ID: 1306001
   *  Session: 2013-2014
   *  Department of Computer Science and Engineering
   *  Begum Rokeya University, Rangpur (BRUR)
***************************************************************************************************************/
#include <bits/stdc++.h>

using namespace std;

#define PI acos(-1.0)
#define EPS 1e-9
#define INF 1 << 28
#define sq(a) ((a) * (a))
#define toRad(a) ((a)*(PI)/180)
#define toDeg(a) ((a)*180/(PI))
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define ppb pop_back
#define mp(a, b) make_pair(a, b)
#define endl '\n'
#define MAX 100000
#define MOD 1000000007
#define what_is(x) cerr << #x << " is " << x << endl;

inline bool isEq(double a, double b){ return (abs(a - b) < EPS); }

typedef pair<int, int> pii;
typedef long long ll;

//#define isValid(a, b) ((a >= 0 && a < b) ? 1 : 0)
//int dr[]  =  {0, -1, -1, -1,  0,  1, 1, 1};
//int dc[]  =  {1,  1,  0, -1, -1, -1, 0, 1};

char num[100];
bool isTidy(ll n)
{
	sprintf(num, "%lld", n);
	int len = strlen(num);
	for(int i = 0; i < len-1; i++){
		if(num[i] > num[i+1])
			return false;
	}
	return true;
}

void doo(int i)
{
	if(num[i+1] == '\0')
		return;
	else if(num[i] > num[i+1]){
		doo(i+1);
		//num[i] = num[i+1];
		num[i]--;
		num[i+1] = '9';
	}
	else{
		char ch = num[i];
		doo(i+1);
		if(ch > num[i+1]){
			num[i] = num[i+1];
		}
	}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	//freopen("view.txt", "w", stdout);
	//ios_base::sync_with_stdio(false); cin.tie(NULL);
//	for(int i = 0; i <= 10000; i++)
//		if(isTidy(i))
//			cout << i << endl;
//		else
//			cout << "\t" << i << endl;

//	char ss[] = "6581";
//	ll n = 6587;
//	strcpy(num, ss);
//	doo(0);
//	for(int i = 0; ss[i] != '\0'; i++){
//		if(num[i] != ss[i]){
//			for(i++; ss[i] != '\0'; i++)
//				num[i] = '9';
//		}
//	}
//	cout << num << endl;
//	ll n2 = strtoll(num, NULL, 10);
//	if(n2 > n)
//		while(n2 > n)
//			n2--;
//	cout << n2 << endl;
	ll t, n, n2;
	cin >> t;
	char ss[100];
	for(ll kas = 1; kas <= t; kas++){
		cin >> n;
		sprintf(ss, "%lld", n);
		strcpy(num, ss);
		doo(0);
		for(int i = 0; ss[i] != '\0'; i++){
			if(num[i] != ss[i]){
				for(i++; ss[i] != '\0'; i++)
					num[i] = '9';
			}
		}
		//cout << num << endl;
		n2 = strtoll(num, NULL, 10);
		if(n2 > n)
			while(n2 > n)
				n2--;
		cout << "Case #" << kas << ": " << n2 << endl;
	}
	return 0;
}
