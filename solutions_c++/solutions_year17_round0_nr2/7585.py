/*			Arjun Sanjeev
			IIIT-Hyderabad		

	********************************************
	*	"Never regret anything in life.	   *
	*	 If it's good, it's wonderful.	   *
	*	 If it's bad, it's experience."    *
	********************************************	*/

#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define let(x,a) __typeof(a) x(a)
#define all(a) (a).begin(),(a).end() 
#define endl '\n'
#define present(c,x) ((c).find(x) != (c).end()) 
#define tr(v,it) for(let(it,v.begin()); it != v.end(); it++)
#define rtr(v,it) for(let(it,v.rbegin()); it != v.rend(); it++)

#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#define LL long long int
#define PII pair<int,int>
#define VI vector<int>
#define inf INT_MAX

using namespace std;

int main()
{
	int t;
	cin>>t;
	string s;
	for(int i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		cin>>s;
		for(int j=0;j<s.length()-1;j++)
		{
			if(s[j]>s[j+1])
			{
				s[j]--;
				char temp=s[j];
				for(int k=j+1;k<s.length();k++)
				{
					s[k]='9';
				}
				for(int k=j-1;k>=0;k--)
				{
					if(s[k]!=temp+1) break;
					s[k]=temp;
					s[k+1]='9';
				}
			}
		}
		int k=0;
		while(s[k]=='0')
		{
			s=s.substr(1);
			k++;
		}
		cout<<s<<endl;
	}
	return 0;
}