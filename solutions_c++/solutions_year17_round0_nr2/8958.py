#include<bits/stdc++.h>
using namespace std;
vector<int> ans;
inline bool Check(int i)
{
	int x = i%10;
	i/=10;
	int y;
	while(i > 0)
	{
		y = x;
		x = i%10;
		if(x>y)    return false;
		i /= 10;
	}
	return true;
}
inline void build()
{
	for(int i=1;i<=1000;i++)
	    if(Check(i))
		    ans.push_back(i); 
}
inline void input()
{
	int t,N,kase=1;
	cin >> t;
	while(t--)
	{
		cin >> N;
		cout << "Case #" << kase++ << ": " << *(upper_bound(ans.begin(),ans.end(),N)-1) << endl;
	}
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    build();
    input();
    return 0;
}

