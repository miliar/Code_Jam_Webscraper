#include<bits/stdc++.h>
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(auto i = (c).begin(); i != (c).end(); i++) 
#define F(i,n) for(int i=0;i<n;i++)
#define VE(i,v) for(int i = 0;i < sz(v);i++)
using namespace std;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned int ui;
const double PI  =3.141592;

int main()
{
//std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	int T;
	cin >> T;
	for(int tc= 1; tc<= T; tc++)
	{
		string S;
		cin>> S;
		vector<char> cS(all(S));
		stack<char> Q;
		int cnt = sz(S);
		int index = 0;
		Q.push(cS[index]);
		index++;
		cnt--;
		int dittoCnt = 0;
		while(cnt>0)
		{
			if(cS[index]>=Q.top())
			{
				Q.push(cS[index]);
				index++;
				cnt--;
			}
			else
			{
				char last = Q.top();
				Q.pop();
				cnt++;
				last--;
				while((sz(Q)!=0) && (last < Q.top()))
				{
					last = Q.top();
					Q.pop();
					cnt++;
					last--;
				}
				if(last!='0')
				{
					Q.push(last);
				}
				cnt--;
				break;

			}
		}
		string ans ="";
		while(sz(Q)!=0)
		{
			ans = Q.top()+ans;
			Q.pop();
		}
		for(int j = cnt; j>0;j--)
			ans = ans +'9';
		cout <<"Case #"<<tc<<": "<<ans<<"\n";




	}
}
		



